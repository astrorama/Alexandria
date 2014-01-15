/** 
 * @file MapPhzDataParameter.h
 * @date November 29, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef MAPPHZDATAPARAMETER_H
#define	MAPPHZDATAPARAMETER_H

#include <map>
#include <memory>
#include <utility>
#include <stdexcept>
#include "ProtoZ/parameter/PhzDataParameter.h"

namespace ProtoZ {
namespace parameter {

/**
 * @class MapPhzDataParameter
 * @brief
 *      Simple PhzDataParameter implementation which stores the parameter values
 *      and data in a map
 * 
 * @tparam T
 *      The type of the parameter values
 * @tparam D
 *      The type of the parameter data
 */
template <typename T, typename D>
class MapPhzDataParameter : public PhzDataParameter<T, D> {

public:
  
  /**
   * @brief
   *    Constructs a new MapPhzDataParameter with the values and data of the
   *    given map
   * @details
   *    The MapPhzDataParameter will take over the ownership of the given map
   *    pointer and no copying will be performed. The MapPhzDataParameter object
   *    is responsible for deleting the map and no further action is required
   *    from the caller.
   * 
   * @param name
   *    The name of the parameter
   * @param values_data
   *    A pointer to the map containing the value-data pairs of the parameter
   */
  MapPhzDataParameter(const std::string& name, std::map<T, D>* values_data) 
        : PhzDataParameter<T, D>{name}, m_values_data{values_data} { }
  
  /**
   * @brief Destructor
   */
  virtual ~MapPhzDataParameter() { }
  
  /**
   * @copydoc PhzParameter::size()
   */
  uint32_t size() const override {
    return m_values_data.get()->size();
  }
  
  /**
   * copydoc PhzParameter::indexToValue()
   */
  const T& indexToValue(uint32_t index) const override {
    if (index >= size())
      throw new std::out_of_range{"MapPhzDataParameter::indexToValue(uint32_t)"};
    auto p = m_values_data->begin();
    for (; index > 0; index--)
      p++;
    return p->first;
  }

  /**
   * @copydoc PhzDataParameter::indexToData()
   */
  const D& indexToData(uint32_t index) const override {
    if (index >= size())
      throw new std::out_of_range{"MapPhzDataParameter::indexToData(uint32_t)"};
    auto p = m_values_data->begin();
    for (; index > 0; index--)
      p++;
    return p->second;
  }

private:

  std::unique_ptr<std::map<T, D> > m_values_data;

};

} /* namespace parameter */
} /* namespace ProtoZ */

#endif	/* MAPPHZDATAPARAMETER_H */

