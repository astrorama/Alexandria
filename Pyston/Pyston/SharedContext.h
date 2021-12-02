/**
 * @copyright (C) 2012-2020 Euclid Science Ground Segment
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

#ifndef PYSTON_SHAREDCONTEXT_H
#define PYSTON_SHAREDCONTEXT_H

#include "Graph/Node.h"

namespace Pyston {

/**
 * This context is used globally (per thread) to pass a context whenever
 * the original python snippet could not be compiled.
 * Basically, it is stored on this global just before jumping into python,
 * and passed to the registered function that has need for it.
 *
 * @see PythonCall
 * @see ExpressionTreeBuilder::registerFunction
 */
extern thread_local Context sharedContext;

}  // namespace Pyston

#endif  // PYSTON_SHAREDCONTEXT_H
