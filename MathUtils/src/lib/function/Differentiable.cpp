/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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
 * @file src/lib/function/Differentiable.cpp
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#include "MathUtils/function/Differentiable.h"

namespace Euclid {
namespace MathUtils {

double Differentiable::integrate(const double x1, const double x2) const {
  std::shared_ptr<Function> antiderivative{this->indefiniteIntegral()};
  return (*antiderivative)(x2) - (*antiderivative)(x1);
}

}  // namespace MathUtils
}  // end of namespace Euclid
