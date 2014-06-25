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

typedef std::unique_ptr<Function> (*MultiplyFunction)(const Function&, const Function&);
extern std::map<std::pair<std::type_index,std::type_index>, MultiplyFunction> multiplySpecificSpecificMap;
extern std::map<std::type_index, MultiplyFunction> multiplySpecificGenericMap;

} // End of ChMath

#endif	/* CHMATH_MULTIPLICATION_H */

