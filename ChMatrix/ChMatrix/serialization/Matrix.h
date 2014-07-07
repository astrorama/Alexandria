/** 
 * @file ChMatrix/serialization/Matrix.h
 * @date May 17, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_SERIALIZATION_MATRIX_H
#define	CHMATRIX_SERIALIZATION_MATRIX_H

#include <type_traits>
#include <memory>
#include <boost/serialization/vector.hpp>
#include "ChMatrix/AxisInfo.h"
#include "ChMatrix/Matrix.h"
#include "ChMatrix/serialization/tuple.h"
#include "ChMatrix/serialization/AxisInfo.h"

namespace boost {
namespace serialization {

/// Method which saves/loads a Matrix instance to/from an archive. It does a
/// check that the DataManager of the Matrix allows for boost serialization.
/// This check is done in compilation time.
template<class Archive, typename DataManager, typename... AxesTypes>
void serialize(Archive&, ChMatrix::Matrix<DataManager,AxesTypes...>&, const unsigned int) {
  static_assert(ChMatrix::DataManagerTraits<DataManager>::enable_boost_serialize,
                "Boost serialization of Matrix with unsupported DataManager");
}

/// Saves in the given archive all the data necessary for recunstructing the
/// given Matrix by using its constructor. The data saved are the axes tuple
/// and a pointer to the DataManager.
/// NOTE: Any changes in this method should be reflected in the
/// load_construct_data method.
template<class Archive, typename DataManager, typename... AxesTypes>
void save_construct_data(Archive& ar, const ChMatrix::Matrix<DataManager,AxesTypes...>* t,
                                const unsigned int) {
  std::tuple<ChMatrix::AxisInfo<AxesTypes>...> axes_tuple = t->axisInfoTuple();
  ar << axes_tuple;
  // Do NOT delete this pointer!!! It points to the DataManager of the matrix
  const DataManager* data_manager_ptr = &(t->dataManager());
  ar << data_manager_ptr;
}

/// Helper method which constructs an AxisInfo object with empty name and
/// zero knots.
template <typename T>
ChMatrix::AxisInfo<T> emptyAxisInfo() {
  return {"", {}};
}

/// Loads from the given archive all the data necessary for reconstructing a
/// Matrix object and constructs a new one where the t pointer points. The
/// data red are the axes tuple and the DataManager.
/// NOTE: Any changes in this method should be reflected in the
/// save_construct_data method.
template<class Archive, typename DataManager, typename... AxesTypes>
void load_construct_data(Archive& ar, ChMatrix::Matrix<DataManager,AxesTypes...>* t,
                                const unsigned int) {
  // We create a tuple containing empty AxisInfo objects. These will be replaced
  // when we read from the stream with the real AxisInfo objects. We have to do
  // that because the AxisInfo does not have a default constructor.
  std::tuple<ChMatrix::AxisInfo<AxesTypes>...> axes_tuple {(emptyAxisInfo<AxesTypes>())...};
  ar >> axes_tuple;
  DataManager* data_manager;
  ar >> data_manager;
  std::unique_ptr<DataManager> ptr {data_manager};
  ::new(t) ChMatrix::Matrix<DataManager,AxesTypes...>(std::move(ptr), axes_tuple);
}

} /* end of namespace serialization */
} /* end of namespace boost */

#endif	/* CHMATRIX_SERIALIZATION_MATRIX_H */

