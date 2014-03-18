/** 
 * @file serialize.h
 * @date December 9, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef SERIALIZE_H
#define	SERIALIZE_H

#include <cstdint>
#include <tuple>
#include <string>
#include <fstream>
#include <memory>
#include <boost/serialization/vector.hpp>
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include "ProtoZ/matrix/AxisInfo.h"
#include "ProtoZ/matrix/Matrix.h"

namespace ProtoZ {
namespace matrix {

template<typename T, typename... Axes>
void writeMatrixInFile(const std::string& filename, const Matrix<T,Axes...>& matrix) {
  std::ofstream ofs(filename);
  boost::archive::binary_oarchive boa(ofs);
  boa << matrix;
}

template<typename T, typename... Axes>
Matrix<T,Axes...> readMatrixFromFile(const std::string& filename) {
  std::ifstream ifs(filename);
  boost::archive::binary_iarchive bia(ifs);
  Matrix<T,Axes...> matrix {};
  bia >> matrix;
  return matrix;
}

} /* namespace matrix */
} /* namespace ProtoZ */

namespace boost {
namespace serialization {

// Handling of tuple serialization

template<uint32_t N>
struct Serialize {
  template<class Archive, typename... Args>
  static void serialize(Archive & ar, std::tuple<Args...> & t, const unsigned int version) {
    ar & std::get<N-1>(t);
    Serialize<N-1>::serialize(ar, t, version);
  }
};

template<>
struct Serialize<0> {
  template<class Archive, typename... Args>
  static void serialize(Archive &, std::tuple<Args...> &, const unsigned int) { }
};

template<class Archive, typename... Args>
void serialize(Archive & ar, std::tuple<Args...> & t, const unsigned int version) {
  Serialize<sizeof...(Args)>::serialize(ar, t, version);
}

// end of tuple serialization handling

template<typename Archive, typename T>
void serialize(Archive& ar, ProtoZ::matrix::AxisInfo<T>& axisInfo,const unsigned int) {
  ar & axisInfo.m_name;
  ar & axisInfo.m_values;
}

template<typename Archive, typename T, typename... Axes>
void serialize(Archive& ar, ProtoZ::matrix::Matrix<T, Axes...>& matrix, const unsigned int) {
  ar & matrix.m_axes;
  ar & matrix.m_data;
  ar & matrix.m_axis_index_factors;
  ar & matrix.m_axis_sizes;
}

} /* namespace serialization */
} /* namespace boost */

#endif	/* SERIALIZE_H */

