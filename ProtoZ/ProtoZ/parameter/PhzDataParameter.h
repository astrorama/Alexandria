/** 
 * @file PhzDataParameter.h
 * @date November 29, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAPARAMETER_H
#define	PHZDATAPARAMETER_H

#include "ProtoZ/parameter/PhzParameter.h"

namespace ProtoZ {
namespace parameter {

/**
 * @class PhzDataParameter
 * @brief
 *      Extends the PhzParameter interface to represent a parameter bonded with
 *      some data
 * @details
 *      The value of a PhzParameter must always have a small string representation.
 *      This class extends the PhzParameter to bond each value with a data object
 *      of arbitrary size. The access of the data is done the same way like the
 *      parameter values, by using indeces (function PhzDataParameter::indexToData(int)).
 * 
 *      Implementation instructions:
 *      Implementations should follow the instructions of the PhzParameter class
 * 
 * @tparam T
 *      The type of the parameter values
 * @tparam D
 *      The type of the parameter data
 */
template <typename T, typename D>
class PhzDataParameter : public PhzParameter<T> {

public:
  
  /**
   * Constructs a new PhzDataParameter with the given name.
   * 
   * @param name
   *    The name of the parameter
   */
  PhzDataParameter(const std::string& name) : PhzParameter<T>{name} { }

  /**
   * @brief Destructor
   */
  virtual ~PhzDataParameter() {}
  
  /**
   * @brief
   *    Returns the data of the parameter for the given (zero based) index
   * 
   * @param index
   *    The index to retrieve the data for
   * @return
   *    The data of the parameter
   * @throws
   *    std::out_of_range, if the index is out of range
   */
  virtual const D& indexToData(uint32_t index) const = 0;

};

} /* namespace parameter */
} /* namespace ProtoZ */

#endif	/* PHZDATAPARAMETER_H */

