/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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

/*
 * FunctionAdapter.cpp
 *
 *  Created on: Nov 2, 2015
 *      Author: fdubath
 */

#include "MathUtils/function/FunctionAdapter.h"

namespace Euclid {
namespace MathUtils {

FunctionAdapter::FunctionAdapter(std::function<double(double)> function) : m_function{function} {}

double FunctionAdapter::operator()(const double x) const {
  return m_function(x);
}

std::unique_ptr<Function> FunctionAdapter::clone() const {
  return std::unique_ptr<Function>{new FunctionAdapter(m_function)};
}

}  // namespace MathUtils
}  // namespace Euclid
