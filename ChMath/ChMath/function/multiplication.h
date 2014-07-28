/** 
 * @file ChMath/function/multiplication.h
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_MULTIPLICATION_H
#define	CHMATH_MULTIPLICATION_H

#include <map>
#include <utility>
#include <typeindex>

namespace ChMath {

/// Alias of a function which multiplies Function objects
typedef std::unique_ptr<Function> (*MultiplyFunction)(const Function&, const Function&);

/**
 * A map for retrieving specific function multiplication implementations. The
 * keys of the map are the pairs of the Function types and the value of the
 * map is the function which can be used for performing this multiplication in
 * an efficient way.
 */
extern std::map<std::pair<std::type_index,std::type_index>, MultiplyFunction> multiplySpecificSpecificMap;

/**
 * A map for retrieving specific function multiplication implementations. The
 * keys of the map are the type of a Function which can be multiplied with any
 * other function and the value of the map is the function which can be used for
 * performing this multiplication in an efficient way.
 */
extern std::map<std::type_index, MultiplyFunction> multiplySpecificGenericMap;

} // End of ChMath

#endif	/* CHMATH_MULTIPLICATION_H */

