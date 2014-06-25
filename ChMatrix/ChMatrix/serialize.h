/** 
 * @file ChMatrix/serialize.h
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_SERIALIZE_H
#define	CHMATRIX_SERIALIZE_H

#include <iostream>
#include <memory>
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include "ChMatrix/Matrix.h"
#include "ChMatrix/serialization/Matrix.h"

namespace ChMatrix {

template<typename DataManager, typename... AxesTypes>
void binaryExport(std::ostream& out, const Matrix<DataManager, AxesTypes...>& matrix) {
  // Do NOT delete this pointer!!! It  points to the actual matrix
  const Matrix<DataManager, AxesTypes...>* ptr = &matrix;
  boost::archive::binary_oarchive boa {out};
  boa << ptr;
}

template<typename DataManager, typename... AxesTypes>
std::unique_ptr<Matrix<DataManager, AxesTypes...>> binaryImport(std::istream& in) {
  boost::archive::binary_iarchive bia {in};
  // Do NOT delete manually this pointer. It is wrapped with a unique_ptr later.
  Matrix<DataManager, AxesTypes...>* ptr;
  bia >> ptr;
  return std::unique_ptr<Matrix<DataManager, AxesTypes...>> {ptr};
}

} // end of namespace ChMatrix

#endif	/* CHMATRIX_SERIALIZE_H */

