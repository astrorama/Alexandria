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
#include "ChDataModel/Source.h"

namespace ChDataModel {

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
   *
   * @param
   *  Vector container of Source objects
   *
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
   *  Get a const_iterator pointing to the first element in the m_sourceVector
   *  vector
   *
   * @return
   *  Returns a const_iterator pointing to the first element in the m_sourceVector
   *  container
   */
  std::vector<Source>::const_iterator cbegin() { return m_sourceVector.cbegin() ; }

  /**
   * @brief
   *  Get an const_iterator pointing to the last element in the m_sourceVector
   *  vector
   *
   * @return
   *  Returns a const_iterator pointing to the past-the-end element in the
   *  m_sourceVector container
   */
  std::vector<Source>::const_iterator cend()   { return m_sourceVector.cend() ; }

  /**
   * @brief
   *  Find the Source object from its identification number
   *
   * @param
   * The source identification number
   *
   * @return
   * A shared pointer to the Source object or a null pointer in case of
   * no object was found for this source_id
   */
  std::shared_ptr<Source> find(const uint64_t source_id);

  /**
   * @brief
   *  Get the size of the vector container
   *
   * @return
   *  The size of the container which is the number of Source objects
   */
  size_t size() { return m_sourceVector.size();}

private:

  std::vector<Source>       m_sourceVector { };
  std::map<uint64_t, size_t> m_indeces_map { };

};

} /* namespace ChDataModel */

#endif /* CATALOG_H_ */
