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

/**
 * @brief Exports to the given output stream the given matrix
 * @details
 * The current implementation uses boost serialization and it requires that
 * the DataManager and all the axes values are serializable. Also the
 * DataManagerTraits specialization for the specific DataManager must have the
 * enable_boost_serialize flag set to true.
 * 
 * Note that if any of the required types is not boost serializable, compilation
 * of this method will fail. Non serializable matrices of this type can still 
 * be used if there is no call to this method.
 * 
 * @tparam DataManager the type of the data manager of the Matrix
 * @tparam AxesTypes the types of the Matrix axes knot values
 * @param out The stream to write the matrix in
 * @param matrix The matrix to export
 */
template<typename DataManager, typename... AxesTypes>
void binaryExport(std::ostream& out, const Matrix<DataManager, AxesTypes...>& matrix) {
  // Do NOT delete this pointer!!! It  points to the actual matrix
  const Matrix<DataManager, AxesTypes...>* ptr = &matrix;
  boost::archive::binary_oarchive boa {out};
  boa << ptr;
}

/**
 * @brief Imports from the given stream a matrix
 * @details
 * The current implementation uses boost serialization and it requires that
 * the DataManager and all the axes values are serializable. Also the
 * DataManagerTraits specialization for the specific DataManager must have the
 * enable_boost_serialize flag set to true.
 * 
 * Note that if any of the required types is not boost serializable, compilation
 * of this method will fail. Non serializable matrices of this type can still 
 * be used if there is no call to this method.
 * 
 * @tparam DataManager the type of the data manager of the Matrix
 * @tparam AxesTypes the types of the Matrix axes knot values
 * @param in The stream to read the matrix from
 * @return The matrix red from the stream
 */
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

