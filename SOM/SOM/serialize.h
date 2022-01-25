/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/*
 * @file serialize.h
 * @author nikoapos
 */

#ifndef SOM_SERIALIZE_H
#define SOM_SERIALIZE_H

#include "ElementsKernel/Exception.h"
#include "SOM/Distance.h"
#include "SOM/serialization/SOM.h"
#include <CCfits/CCfits>
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include <iostream>

namespace Euclid {
namespace SOM {

template <typename OArchive, typename DistFunc>
void somExport(std::ostream& out, const SOM<DistFunc>& som) {
  // Do NOT delete this pointer!!! It  points to the actual som
  const SOM<DistFunc>* ptr = &som;
  OArchive                 boa{out};
  boa << ptr;
}

template <typename DistFunc>
void somBinaryExport(std::ostream& out, const SOM<DistFunc>& som) {
  somExport<boost::archive::binary_oarchive>(out, som);
}

template <typename IArchive, typename DistFunc = Distance::L2>
SOM<DistFunc> somImport(std::istream& in) {
  IArchive bia{in};
  // Do NOT delete manually this pointer. It is wrapped with a unique_ptr later.
  SOM<DistFunc>* ptr;
  bia >> ptr;
  std::unique_ptr<SOM<DistFunc>> smart_ptr{ptr};
  // We move out to the result the som pointed by the pointer. The unique_ptr
  // will delete the (now empty) pointed object
  return std::move(*smart_ptr);
}

template <typename DistFunc = Distance::L2>
SOM<DistFunc> somBinaryImport(std::istream& in) {
  return somImport<boost::archive::binary_iarchive, DistFunc>(in);
}

template <typename DistFunc>
void somFitsExport(const std::string& filename, const SOM<DistFunc>& som) {

  // Create the output file and the array HDU
  int         n_axes = 3;
  std::size_t x;
  std::size_t y;
  std::tie(x, y)           = som.getSize();
  long         ax_sizes[3] = {long(x), long(y), long(som.getDimensions())};
  CCfits::FITS fits(filename, DOUBLE_IMG, n_axes, ax_sizes);

  // Write in the header the DistFunc type
  fits.pHDU().addKey("DISTFUNC", typeid(DistFunc).name(), "");

  // Create a valarray with the SOM data
  std::size_t           total_size = x * y * som.getDimensions();
  std::valarray<double> data(total_size);
  int                   i = 0;
  for (std::size_t w_i = 0; w_i < som.getDimensions(); ++w_i) {
    for (auto& w_arr : som) {
      data[i] = w_arr[w_i];
      ++i;
    }
  }
  fits.pHDU().write(1, total_size, data);
}

template <typename DistFunc = Distance::L2>
SOM<DistFunc> somFitsImport(const std::string& filename) {

  CCfits::FITS fits(filename, CCfits::Read);

  // Check that the type of the DistFunc is correct
  std::string dist_func_type;
  fits.pHDU().readKey("DISTFUNC", dist_func_type);
  if (dist_func_type != typeid(DistFunc).name()) {
    throw Elements::Exception() << "Incompatible DistFunc parameter. File contains SOM with " << dist_func_type
                                << " and is read as " << typeid(DistFunc).name();
  }

  // Get the dimensions of the data in the file
  if (fits.pHDU().axes() != 3) {
    throw Elements::Exception() << "Data array in file " << filename << " does not have 3 dimensions";
  }
  std::size_t dim = fits.pHDU().axis(2);
  std::size_t x = fits.pHDU().axis(0);
  std::size_t y = fits.pHDU().axis(1);

  // Read the data from the file
  std::valarray<double> data;
  fits.pHDU().read(data);

  // Copy the data in a SOM object
  SOM<DistFunc> result{dim, x, y};
  int               i = 0;
  for (std::size_t w_i = 0; w_i < dim; ++w_i) {
    for (auto& w_arr : result) {
      w_arr[w_i] = data[i];
      ++i;
    }
  }

  return result;
}

}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_SERIALIZE_H */
