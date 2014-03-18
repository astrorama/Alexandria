/** 
 * @file VectorParameter.h
 * @date November 29, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef VECTORPARAMETER_H
#define	VECTORPARAMETER_H

#include <vector>
#include <string>
#include "ProtoZ/parameter/PhzParameter.h"

namespace ProtoZ {
namespace parameter {

/**
 * @class VectorPhzParameter
 * @brief
 *      Simple PhzParameter implementation which stores the parameter values in
 *      a vector
 * 
 * @tparam T
 *      The type of the parameter values
 */
template <typename T>
class VectorPhzParameter : public PhzParameter<T> {

public:

  /**
   * @brief
   *    Constructs a new VectorParameter with the values of the given vector
   * @details
   *    The values of the given vector are copied internally in the PhzParameter
   *    object. Copying is used here as the values of the parameter should be
   *    small in size.
   * @param name
   *    The name of the parameter
   * @param values
   *    The values of the parameter
   */
  VectorPhzParameter(const std::string& name, const std::vector<T>& values)
        : PhzParameter<T>{name}, m_values{values} { }

  /**
   * @brief Destructor
   */
  virtual ~VectorPhzParameter() { }

  // Methods of PhzParameter are delegated to the vector

  /**
   * @copydoc PhzParameter::size()
   */
  uint32_t size() const override {
    return m_values.size();
  }

  /**
   * @copydoc PhzParameter::indexToValue()
   */
  const T& indexToValue(uint32_t index) const override {
    return m_values[index];
  }

private:

  const std::vector<T> m_values;
  
};

} /* namespace parameter */
} /* namespace ProtoZ */

#endif	/* VECTORPARAMETER_H */

