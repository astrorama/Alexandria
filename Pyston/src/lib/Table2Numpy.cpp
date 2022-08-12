/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#include "Pyston/Table2Numpy.h"
#include <ElementsKernel/Exception.h>
#include <boost/python/list.hpp>
#include <boost/python/numpy.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include <boost/python/tuple.hpp>

namespace py = boost::python;
namespace np = boost::python::numpy;

namespace Pyston {

namespace {
/**
 * Generate a Python tuple describing the shape of the vectors stored on the given column.
 * For instance, for a column with vectors of three elements, this will return (3,)
 */
template <typename T>
py::tuple getVectorShape(const Euclid::Table::Table& table, size_t idx) {
  auto& first_row   = *table.begin();
  auto& first_value = boost::get<std::vector<T>>(first_row[idx]);
  auto  size        = first_value.size();

  // Make sure all entries have the same shape!
  for (auto& row : table) {
    if (size != boost::get<std::vector<T>>(row[idx]).size()) {
      throw Elements::Exception("All vectors on the column must have the same size");
    }
  }

  return py::make_tuple(size);
}

/**
 * Similar but for strings
 */
std::size_t getStringShape(const Euclid::Table::Table& table, size_t idx) {
  auto& first_row   = *table.begin();
  auto& first_value = boost::get<std::string>(first_row[idx]);
  auto  size        = first_value.size();

  // Make sure all entries have the same shape!
  for (auto& row : table) {
    if (size != boost::get<std::string>(row[idx]).size()) {
      throw Elements::Exception("All vectors on the column must have the same size");
    }
  }

  return size + 1;
}

/**
 * Generate a Python tuple describing the shape of the NdArray stored on the given column.
 * For instance, for a column with NdArray of 3x2 elements, this will return (3,2)
 */
template <typename T>
py::tuple getNdArrayShape(const Euclid::Table::Table& table, size_t idx) {
  auto& first_row   = *table.begin();
  auto& first_value = boost::get<Euclid::NdArray::NdArray<T>>(first_row[idx]);
  auto  shape       = first_value.shape();

  // Make sure all entries have the same shape!
  for (auto& row : table) {
    if (shape != boost::get<Euclid::NdArray::NdArray<T>>(row[idx]).shape()) {
      throw Elements::Exception("All NdArrays on the column must have the same shape");
    }
  }

  // Need to convert the std::vector to a Python tuple
  py::list pyshape;
  for (auto d : shape) {
    pyshape.append(d);
  }
  return py::tuple(pyshape);
}

/**
 * Generate a Python tuple with a type description of the column idx suitable for numpy.
 */
py::tuple numpyType(const Euclid::Table::Table& table, size_t idx) {
  auto& descr = table.getColumnInfo()->getDescription(idx);
  auto& name  = descr.name;

  std::type_index type = descr.type;

  if (type == typeid(int32_t)) {
    return py::make_tuple(name, "i4");
  } else if (type == typeid(int64_t)) {
    return py::make_tuple(name, "i8");
  } else if (type == typeid(float)) {
    return py::make_tuple(name, "f4");
  } else if (type == typeid(double)) {
    return py::make_tuple(name, "f8");
  } else if (type == typeid(std::string)) {
    return py::make_tuple(name, "S" + std::to_string(getStringShape(table, idx)));
  } else if (type == typeid(std::vector<int32_t>)) {
    return py::make_tuple(name, "i4", getVectorShape<int32_t>(table, idx));
  } else if (type == typeid(std::vector<int64_t>)) {
    return py::make_tuple(name, "i8", getVectorShape<int64_t>(table, idx));
  } else if (type == typeid(std::vector<float>)) {
    return py::make_tuple(name, "f4", getVectorShape<float>(table, idx));
  } else if (type == typeid(std::vector<double>)) {
    return py::make_tuple(name, "f8", getVectorShape<double>(table, idx));
  } else if (type == typeid(Euclid::NdArray::NdArray<int32_t>)) {
    return py::make_tuple(name, "i4", getNdArrayShape<int32_t>(table, idx));
  } else if (type == typeid(Euclid::NdArray::NdArray<int64_t>)) {
    return py::make_tuple(name, "i8", getNdArrayShape<int64_t>(table, idx));
  } else if (type == typeid(Euclid::NdArray::NdArray<float>)) {
    return py::make_tuple(name, "f4", getNdArrayShape<float>(table, idx));
  } else if (type == typeid(Euclid::NdArray::NdArray<double>)) {
    return py::make_tuple(name, "f8", getNdArrayShape<double>(table, idx));
  } else {
    throw Elements::Exception("Unknown type ") << type.name();
  }
}

/**
 * Get the size and a pointer to the content of a vector cell
 */
template <typename T>
std::tuple<off_t, const void*> getVectorCellData(const Euclid::Table::Row::cell_type& cell) {
  auto& v = boost::get<std::vector<T>>(cell);
  return std::make_tuple(sizeof(T) * v.size(), v.data());
}

/**
 * The same but for strings
 */
std::tuple<off_t, const void*> getStringCellData(const Euclid::Table::Row::cell_type& cell) {
  auto& v = boost::get<std::string>(cell);
  return std::make_tuple(v.size() + 1, v.data());
}

/**
 * Get the size and a pointer to the content of a NdArray cell
 */
template <typename T>
std::tuple<off_t, const void*> getNdArrayCellData(const Euclid::Table::Row::cell_type& cell) {
  auto& v = boost::get<Euclid::NdArray::NdArray<T>>(cell);
  return std::make_tuple(sizeof(T) * v.size(), &(*v.begin()));
}

/**
 * Numpy stores the rows in memory together. Given the buffer dst (within the numpy array), copy
 * the value stored on the given cell with the given description
 * @param dst
 *  Destination for the raw copy
 * @param descr
 *  Column description
 * @param cell
 *  Cell to copy into dst
 * @return
 *  Size in bytes of the cell content, so the caller may increment the pointer dst to copy the next cell
 */
off_t copyCell(void* dst, const Euclid::Table::ColumnDescription& descr, const Euclid::Table::Row::cell_type& cell) {
  std::type_index type      = descr.type;
  off_t           data_size = 0;
  const void*     data_ptr;

  if (type == typeid(int32_t)) {
    data_size = sizeof(int32_t);
    data_ptr  = &boost::get<int32_t>(cell);
  } else if (type == typeid(int64_t)) {
    data_size = sizeof(int64_t);
    data_ptr  = &boost::get<int64_t>(cell);
  } else if (type == typeid(float)) {
    data_size = sizeof(float);
    data_ptr  = &boost::get<float>(cell);
  } else if (type == typeid(double)) {
    data_size = sizeof(double);
    data_ptr  = &boost::get<double>(cell);
  } else if (type == typeid(std::string)) {
    std::tie(data_size, data_ptr) = getStringCellData(cell);
  } else if (type == typeid(std::vector<int32_t>)) {
    std::tie(data_size, data_ptr) = getVectorCellData<int32_t>(cell);
  } else if (type == typeid(std::vector<int64_t>)) {
    std::tie(data_size, data_ptr) = getVectorCellData<int64_t>(cell);
  } else if (type == typeid(std::vector<float>)) {
    std::tie(data_size, data_ptr) = getVectorCellData<float>(cell);
  } else if (type == typeid(std::vector<double>)) {
    std::tie(data_size, data_ptr) = getVectorCellData<double>(cell);
  } else if (type == typeid(Euclid::NdArray::NdArray<int32_t>)) {
    std::tie(data_size, data_ptr) = getNdArrayCellData<int32_t>(cell);
  } else if (type == typeid(Euclid::NdArray::NdArray<int64_t>)) {
    std::tie(data_size, data_ptr) = getNdArrayCellData<int64_t>(cell);
  } else if (type == typeid(Euclid::NdArray::NdArray<float>)) {
    std::tie(data_size, data_ptr) = getNdArrayCellData<float>(cell);
  } else if (type == typeid(Euclid::NdArray::NdArray<double>)) {
    std::tie(data_size, data_ptr) = getNdArrayCellData<double>(cell);
  } else {
    throw Elements::Exception("Unknown type ") << type.name();
  }

  std::memcpy(dst, data_ptr, data_size);
  return data_size;
}

}  // namespace

boost::python::numpy::ndarray table2numpy(const Euclid::Table::Table& table) {
  auto   colinfo = table.getColumnInfo();
  size_t ncols   = colinfo->size();
  size_t nrows   = table.size();

  py::list cols;

  // Generate the dtypes for numpy
  for (size_t i = 0; i < ncols; ++i) {
    auto coldesc = colinfo->getDescription(i);
    cols.append(numpyType(table, i));
  }

  // Convert the list of dtypes to an array description
  np::dtype dtype(cols);

  // Create the numpy array
  auto array = np::zeros(py::make_tuple(table.size()), dtype);

  // Copy into each row the content from the table
  char* nd_ptr = array.get_data();
  for (size_t i = 0; i < nrows; ++i) {
    const auto& row = table[i];
    for (size_t j = 0; j < ncols; ++j) {
      nd_ptr += copyCell(nd_ptr, colinfo->getDescription(j), row[j]);
    }
  }

  return array;
}

}  // namespace Pyston
