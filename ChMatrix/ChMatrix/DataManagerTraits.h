/** 
 * @file ChMatrix/DataManagerTraits.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_DATAMANAGERTRAITS_H
#define	CHMATRIX_DATAMANAGERTRAITS_H

#include <vector>
#include <memory>

namespace ChMatrix {

/**
 * @class DataManagerTraits
 * 
 * @brief Class used by the Matrix to access the different DataManagers
 * 
 * @details
 * To reduce the requirements of the different DataManager which are used by
 * the Matrix to store the data, the Matrix class does not directly access the
 * DataManager instances, but it uses this trait to redirect all the operations.
 * The default implementation of the trait simply redirects the operations,
 * but, if the API of a manager does not fit the trait, this default behavior
 * can be overridden by declaring a specialization of the trait.
 * 
 * @tparam DataManager the manager which keeps the Matrix data
 */
template<typename DataManager>
class DataManagerTraits {
  
public:
  
  /// The type of the data kept by the DataManager
  typedef typename DataManager::data_type data_type;
  
  /// The iterator type which is used to iterate through the data kept in the
  /// data manager
  typedef typename DataManager::iterator iterator;
  
  /**
   * Factory which creates a DataManager instance with the given number of
   * managed data, which all are set to a default value. The default
   * implementation will try to use a constructor with the size as parameter.
   * 
   * @param size The number of data the manager will contain
   * @return A unique_ptr to the newly constructed DataManager
   */
  static std::unique_ptr<DataManager> factory(size_t size);
  
  /**
   * Returns the number of data managed by the given DataManager. Defaults on
   * calling the constant version of method size() on the DataManager instance.
   * 
   * @param data_manager The DataManager to get the size of
   * @return The number of data managed by the DataManager
   */
  static size_t size(const DataManager& data_manager);
  
  /**
   * Returns an iterator pointing to the first element managed by the
   * DataManager. Defaults on calling the begin() method of the DataManager
   * instance.
   * 
   * @param data_manager the data manager
   * @return An iterator at the first element
   */
  static iterator begin(DataManager& data_manager);
  
  /**
   * Returns an iterator pointing right after the last element managed by the
   * DataManager. Defaults on calling the end() method of the DataManager
   * instance.
   * 
   * @param data_manager the DataManager
   * @return An iterator right after the last element
   */
  static iterator end(DataManager& data_manager);
  
  /// Flag which indicates if the DataManager is boost serializable. By default
  /// it is set to false. Note that Matrices which use DataManagers which have
  /// this flag set to false cannot be serialized.
  static const bool enable_boost_serialize = false;
  
}; // end of DataManagerTraits


/**
 * Specialization of the DataManagerTraits for vector DataManagers. It uses
 * all the default operations but it changes the serialization flag to true
 * to declare that vector DataManager%s can be serialized. Note that the type
 * T of the data managed has to also be serializable.
 * 
 * @tparam T the type of the data kept by the vector
 */
template<typename T>
class DataManagerTraits<std::vector<T>> {
  
public:
  
  /// The type of the data kept by the DataManager
  typedef T data_type;
  
  /// The iterator type which is used to iterate through the data kept in the
  /// data manager
  typedef typename std::vector<T>::iterator iterator;
  
  /// Returns a vector containing "size" default constructed elements
  static std::unique_ptr<std::vector<T>> factory(size_t size);
  
  /// Returns the size of the vector
  static size_t size(const std::vector<T>& vector);
  
  /// Returns an iterator at the first element of the vector
  static iterator begin(std::vector<T>& vector);
  
  /// Returns an iterator right after the last element of the vector
  static iterator end(std::vector<T>& vector);
  
  /// Enables boost serialization of Matrices using vector%s as DataManager%s
  static const bool enable_boost_serialize = true;
  
}; // end of DataManagerTraits vector specialization

} // end of namespace ChMatrix

#include "ChMatrix/_impl/DataManagerTraits.icpp"

#endif	/* CHMATRIX_DATAMANAGERTRAITS_H */

