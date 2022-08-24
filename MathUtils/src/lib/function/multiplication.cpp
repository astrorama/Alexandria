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
 * @file src/lib/function/multiplication.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include "MathUtils/function/multiplication.h"
#include "AlexandriaKernel/memory_tools.h"
#include "MathUtils/function/Piecewise.h"
#include "MathUtils/function/Polynomial.h"
#include "MathUtils/function/function_tools.h"
#include "MathUtils/interpolation/interpolation.h"
#include <memory>
#include <set>
#include <vector>

namespace Euclid {
namespace MathUtils {

/// Function for multiplying two Polynomial%s. It multiplies their coefficients.
std::unique_ptr<Function> multiplyPolynomials(const Function& f1, const Function& f2) {
  const auto&         p1 = dynamic_cast<const Polynomial&>(f1);
  const auto&         p2 = dynamic_cast<const Polynomial&>(f2);
  std::vector<double> c1 = p1.getCoefficients();
  std::vector<double> c2 = p2.getCoefficients();
  std::vector<double> resultCoef(c1.size() + c2.size() - 1, 0.);
  for (size_t i = 0; i < c1.size(); ++i)
    for (size_t j = 0; j < c2.size(); ++j)
      resultCoef[i + j] += c1[i] * c2[j];
  return make_unique<Polynomial>(std::move(resultCoef));
}

/// Function for multiplying a Piecewise with any other type. It multiplies each
/// sub-function of the Piecewise with the other function.
std::unique_ptr<Function> multiplyPiecewiseWithGeneric(const Function& f1, const Function& f2) {
  const auto& piecewise          = dynamic_cast<const Piecewise&>(f1);
  const auto& interval_functions = piecewise.getFunctions();

  std::vector<std::shared_ptr<Function>> functions(interval_functions.size());
  std::transform(interval_functions.begin(), interval_functions.end(), functions.begin(),
                 [&f2](const std::unique_ptr<Function>& original) { return multiply(*original, f2); });
  return make_unique<Piecewise>(piecewise.getKnots(), functions);
}

template <typename Iter>
static std::pair<Iter, Iter> overlappingStart(Iter start1, Iter end1, Iter start2, Iter end2) {
  for (auto i1 = start1, i2 = start2; i1 != end1 && i2 != end2;) {
    if (*i1 < *i2) {
      ++i1;
      if (i1 != end1 && *i1 > *i2) {
        return {i1, i2};
      }
    } else {
      ++i2;
      if (i2 != end2 && *i1 < *i2) {
        return {i1, i2};
      }
    }
  }
  return {end1, end2};
}

/// Returns a vector of the overlapping knots from the given vectors
std::vector<double> overlappingKnots(const std::vector<double>& knots1, const std::vector<double>& knots2) {
  std::set<double>                    knotSet{};
  std::vector<double>::const_iterator p1Iter;
  std::vector<double>::const_iterator p2Iter;
  std::tie(p1Iter, p2Iter) = overlappingStart(knots1.begin(), knots1.end(), knots2.begin(), knots2.end());

  while (p1Iter != knots1.end() && p2Iter != knots2.end()) {
    if (*p1Iter < *p2Iter) {
      knotSet.insert(*p1Iter);
      ++p1Iter;
    } else {
      knotSet.insert(*p2Iter);
      ++p2Iter;
    }
  }
  return std::vector<double>{knotSet.begin(), knotSet.end()};
}

// Multiply two Piecewise Function%s by multiplying all their sub-functions
std::unique_ptr<Function> multiplyPiecewises(const Function& f1, const Function& f2) {
  const auto& p1 = dynamic_cast<const Piecewise&>(f1);
  const auto& p2 = dynamic_cast<const Piecewise&>(f2);

  auto knots = overlappingKnots(p1.getKnots(), p2.getKnots());

  if (knots.empty()) {
    return make_unique<Polynomial>(std::vector<double>{0.});
  }

  std::vector<std::shared_ptr<Function>> functions{};
  auto&                                  p1func = p1.getFunctions();
  auto&                                  p2func = p2.getFunctions();
  int                                    i1{};
  int                                    i2{};
  for (double knot : knots) {
    if (knot == knots.back()) {
      break;
    }
    while (p1.getKnots()[i1 + 1] <= knot) {
      ++i1;
    }
    while (p2.getKnots()[i2 + 1] <= knot) {
      ++i2;
    }
    functions.push_back(std::shared_ptr<Function>{Euclid::MathUtils::multiply(*p1func[i1], *p2func[i2]).release()});
  }

  return make_unique<Piecewise>(knots, std::move(functions));
}

std::map<std::pair<std::type_index, std::type_index>, MultiplyFunction> multiplySpecificSpecificMap{
    {std::pair<std::type_index, std::type_index>(typeid(Polynomial), typeid(Polynomial)), &multiplyPolynomials},
    {std::pair<std::type_index, std::type_index>(typeid(Piecewise), typeid(Piecewise)), &multiplyPiecewises}};

std::map<std::type_index, MultiplyFunction> multiplySpecificGenericMap{
    {typeid(Piecewise), &multiplyPiecewiseWithGeneric}};

}  // namespace MathUtils
}  // end of namespace Euclid
