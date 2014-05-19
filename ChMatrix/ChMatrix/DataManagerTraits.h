/** 
 * @file DataManagerTraits.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_DATAMANAGERTRAITS_H
#define	CHMATRIX_DATAMANAGERTRAITS_H

#include <vector>
#include <memory>

namespace ChMatrix {

template<typename DataManager>
class DataManagerTraits {
public:
  typedef typename DataManager::data_type data_type;
  typedef typename DataManager::iterator iterator;
  static std::unique_ptr<DataManager> factory(size_t size);
  static size_t size(const DataManager& data_manager);
  static iterator begin(DataManager& data_manager);
  static iterator end(DataManager& data_manager);
  static const bool enable_boost_serialize = false;
};

template<typename T>
class DataManagerTraits<std::vector<T>> {
public:
  typedef T data_type;
  typedef typename std::vector<T>::iterator iterator;
  static std::unique_ptr<std::vector<T>> factory(size_t size);
  static size_t size(const std::vector<T>& vector);
  static iterator begin(std::vector<T>& vector);
  static iterator end(std::vector<T>& vector);
  static const bool enable_boost_serialize = true;
};

} // end of namespace ChMatrix

#include "ChMatrix/_impl/DataManagerTraits.icpp"

#endif	/* CHMATRIX_DATAMANAGERTRAITS_H */

