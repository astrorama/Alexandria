/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/**
 * @file MathUtils/function/multiplication.h
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_MULTIPLICATION_H
#define MATHUTILS_MULTIPLICATION_H

#include <map>
#include <memory>
#include <typeindex>
#include <utility>

#include "ElementsKernel/Export.h"
#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/// Alias of a function which multiplies Function objects
typedef std::unique_ptr<Function> (*MultiplyFunction)(const Function&, const Function&);

/**
 * A map for retrieving specific function multiplication implementations. The
 * keys of the map are the pairs of the Function types and the value of the
 * map is the function which can be used for performing this multiplication in
 * an efficient way.
 */
ELEMENTS_API extern std::map<std::pair<std::type_index, std::type_index>, MultiplyFunction> multiplySpecificSpecificMap;

/**
 * A map for retrieving specific function multiplication implementations. The
 * keys of the map are the type of a Function which can be multiplied with any
 * other function and the value of the map is the function which can be used for
 * performing this multiplication in an efficient way.
 */
ELEMENTS_API extern std::map<std::type_index, MultiplyFunction> multiplySpecificGenericMap;

}  // namespace MathUtils
}  // end of namespace Euclid

#endif /* MATHUTILS_MULTIPLICATION_H */
