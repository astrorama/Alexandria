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

/**
 * @file src/lib/function/function_tools.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include "MathUtils/function/function_tools.h"
#include "ElementsKernel/Exception.h"
#include "MathUtils/function/Integrable.h"
#include "MathUtils/function/multiplication.h"

namespace Euclid {
namespace MathUtils {

double integrate(const Function& function, const double min, const double max,
                 std::unique_ptr<NumericalIntegrationScheme> numericalIntegrationScheme) {
  const Integrable* integrable = dynamic_cast<const Integrable*>(&function);
  if (integrable) {
    return integrable->integrate(min, max);
  }

  if (numericalIntegrationScheme != nullptr) {
    return (*numericalIntegrationScheme)(function, min, max);
  }

  throw Elements::Exception() << "Numerical integration of non-Integrable Functions "
                              << "requiere that you provide a NumericalIntegrationScheme";
}

class DefaultMultiplication : public Function {
public:
  DefaultMultiplication(const Function& f1, const Function& f2) : m_f1{f1.clone()}, m_f2{f2.clone()} {}
  double operator()(const double x) const override {
    return (*m_f1)(x) * (*m_f2)(x);
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function>{new DefaultMultiplication{*m_f1, *m_f2}};
  }

private:
  std::unique_ptr<Function> m_f1;
  std::unique_ptr<Function> m_f2;
};

std::unique_ptr<Function> multiply(const Function& f1, const Function& f2) {
  // First we check if we have specific function for multiplying the two types with each other
  auto iter = multiplySpecificSpecificMap.find(std::pair<std::type_index, std::type_index>(typeid(f1), typeid(f2)));
  if (iter != multiplySpecificSpecificMap.end()) {
    return iter->second(f1, f2);
  }
  iter = multiplySpecificSpecificMap.find(std::pair<std::type_index, std::type_index>(typeid(f2), typeid(f1)));
  if (iter != multiplySpecificSpecificMap.end()) {
    return iter->second(f2, f1);
  }
  // Now we check if we have a specific function for multiplying one of the
  // parameters with a generic function
  auto iter2 = multiplySpecificGenericMap.find(typeid(f1));
  if (iter2 != multiplySpecificGenericMap.end()) {
    return iter2->second(f1, f2);
  }
  iter2 = multiplySpecificGenericMap.find(typeid(f2));
  if (iter2 != multiplySpecificGenericMap.end()) {
    return iter2->second(f2, f1);
  }
  // We couldn't find any specific function for handling the multiplication of
  // the f1 and f2, so return the default
  return std::unique_ptr<Function>{new DefaultMultiplication(f1, f2)};
}

}  // namespace MathUtils
}  // end of namespace Euclid
