/**
 * @file Catalog.h
 *
 * @author Nicolas Morisset
 *
 * Created on: Feb 4, 2014
 */

#ifndef CATALOG_H_
#define CATALOG_H_

#include <map>
#include <memory>
#include "ChCatalog/Source.h"

namespace ChCatalog {

/**
 * @class Catalog
 *
 * @brief
 *  Catalog contains a container of sources
 *
 */
class Catalog
{

public:

  /**
   * @brief
   *  Build a catalog of Source objects
   *
   * @details
   *  Constructs a vector container of Source objects and a map
   *  of source identification and an index which is the location of the Source
   *  object in the vector container
   * @param
   *  Vector container of Source objects
   * @throw ElementsException
   *  A Source object can not be inserted twice in the map
   */
  Catalog(std::vector<Source> source_vector);

  /**
   * @brief Destructor
   */
  virtual ~Catalog() { }

  /**
   * @brief
   *  Get a const_iterator pointing to the first element in the m_source_vector
   *  vector
   * @return
   *  Returns a const_iterator pointing to the first element in the m_source_vector
   *  container
   */
  std::vector<Source>::const_iterator cbegin()  { return m_source_vector.cbegin() ; }

  /**
   * @brief
   *  Get an const_iterator pointing to the last element in the m_source_vector
   *  vector
   * @return
   *  Returns a const_iterator pointing to the past-the-end element in the
   *  m_source_vector container
   */
  std::vector<Source>::const_iterator cend()  { return m_source_vector.cend() ; }

  /**
   * @brief
   *  Find the Source object from its identification number
   * @param
   * The source identification number
   * @return
   * A shared pointer to the Source object or a null pointer in case of
   * no object was found for this source_id
   */
  std::shared_ptr<Source> find(const int64_t source_id) const;

  /**
   * @brief
   *  Get the size of the vector container
   * @return
   *  The size of the container which is the number of Source objects
   */
  size_t size() const { return m_source_vector.size();}

private:
  /// Vector of Source objects
  std::vector<Source>        m_source_vector { };
  /// Map of the Source identification and their location
  /// in the Source vector
  std::map<int64_t, size_t> m_indices_map { };

};

} /* namespace ChCatalog */

#endif /* CATALOG_H_ */
