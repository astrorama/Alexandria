/** 
 * @file Parameter.h
 * @date November 28, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef PHZPARAMETER_H
#define	PHZPARAMETER_H

#include <string>
#include <cstdint>

namespace ProtoZ {
namespace parameter {

/**
 * @class PhzParameter
 * @brief
 *      Interface representing a PHZ algorithm parameter
 * @details
 *      This interface represents a parameter for which the PHZ algorithm makes
 *      flux calculations. Each parameter has a name (string) and a set of possible
 *      values. The PHZ algorithm calculates a flux value for each possible 
 *      combination of parameter values.
 * 
 *      Currently the use of this class is done by using the index of the values
 *      of the parameter. The method PhzParameter::size() can be used to retrieve
 *      the total number of the parameter possible values. Then the method
 *      PhzParameter::indexToValue(int) can be used to convert the indeces to
 *      the real parameter values.
 * 
 *      Implementation instructions:
 *      All implementations should be immutable because the parameters of the
 *      PHZ algorithm cannot change during the algorithm execution. There is no
 *      ordering (increasing/decreasing) restriction for the values of the
 *      parameters, but implementations need to be consistent on the mapping
 *      between indeces and values.
 * 
 * @tparam T
 *      The type of the parameter values
 */
template <typename T>
class PhzParameter {

public:
  
  /**
   * Constructs a new PhzParameter with the given name.
   * 
   * @param name
   *    The name of the parameter
   */
  PhzParameter(const std::string& name) : m_name{name} { }

  /**
   * @brief Destructor
   */
  virtual ~PhzParameter() { }
  
  const std::string& getName() const {
    return m_name;
  }
  
  /**
   * @brief
   *    Returns the number of possible values
   * 
   * @return 
   *    The number of possible values
   */
  virtual uint32_t size() const = 0;
  
  /**
   * @brief
   *    Returns the value of the parameter for the given (zero based) index
   * 
   * @param index
   *    The index to retrieve the value for
   * @return
   *    The value of the parameter
   * @throws
   *    std::out_of_range, if the index is out of range
   */
  virtual const T& indexToValue(uint32_t index) const = 0;
  
private:
  
  std::string m_name;

};

} /* namespace parameter */
} /* namespace ProtoZ */

#endif	/* PARAMETER_H */

