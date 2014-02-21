/** 
 * @file multiplication.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <memory>
#include <vector>
#include <set>
#include "ChMath/function/Polynomial.h"
#include "ChMath/function/Piecewise.h"
#include "ChMath/function/multiplication.h"
#include "ChMath/function/function_tools.h"
#include "ChMath/interpolation/Spline.h"
#include "ChMath/interpolation/interpolation.h"

namespace ChMath {

std::unique_ptr<Function> multiplyPolynomials(const Function& f1, const Function& f2) {
  const Polynomial& p1 = dynamic_cast<const Polynomial&>(f1);
  const Polynomial& p2 = dynamic_cast<const Polynomial&>(f2);
  std::vector<double> c1 = p1.getCoefficients();
  std::vector<double> c2 = p2.getCoefficients();
  std::vector<double> resultCoef(c1.size() + c2.size() - 1, 0.);
  for (uint i = 0; i < c1.size(); ++i)
    for (uint j = 0; j < c2.size(); ++j)
      resultCoef[i + j] += c1[i] * c2[j];
  return std::unique_ptr<Polynomial>(new Polynomial{resultCoef});
}

std::unique_ptr<Function> multiplyPiecewiseWithGeneric(const Function& f1, const Function& f2) {
  const Piecewise& piecewise = dynamic_cast<const Piecewise&>(f1);
  std::vector<std::shared_ptr<Function>> functions {};
  for (auto original : piecewise.getFunctions()) {
    functions.push_back(std::shared_ptr<Function>{ChMath::multiply(*original, f2).release()});
  }
  return std::unique_ptr<Function>(new Piecewise {piecewise.getKnots(), functions});
}

std::unique_ptr<Function> multiplyPiecewises(const Function& f1, const Function& f2) {
  const Piecewise& p1 = dynamic_cast<const Piecewise&>(f1);
  const Piecewise& p2 = dynamic_cast<const Piecewise&>(f2);
  
  auto p1Knots = p1.getKnots();
  auto p2Knots = p2.getKnots();
  if (p1Knots.front() >= p2Knots.back() || p1Knots.back() <= p2Knots.front()) {
    return std::unique_ptr<Function> {new Polynomial{{0.}}};
  }
  
  std::set<double> knotSet {};
  auto p1Iter = p1Knots.begin();
  auto p2Iter = p2Knots.begin();
  bool started = false;
  while (p1Iter != p1Knots.end() && p2Iter != p2Knots.end()) {
    if (!started) {
      if (*p1Iter < *p2Iter) {
        if (*(++p1Iter) > *p2Iter) {
          started = true;
        }
      } else {
        if (*p1Iter < *(++p2Iter)) {
          started = true;
        }
      }
      continue;
    }
    if (*p1Iter < *p2Iter) {
      knotSet.insert(*p1Iter);
      ++p1Iter;
    } else {
      knotSet.insert(*p2Iter);
      ++p2Iter;
    }
  }
  std::vector<double> knots {knotSet.begin(), knotSet.end()};
  
  std::vector<std::shared_ptr<Function>> functions {};
  auto p1func = p1.getFunctions();
  auto p2func = p2.getFunctions();
  int i1 {};
  int i2 {};
  for (double knot : knots) {
    if (knot == knots.back()) {
      break;
    }
    while (p1Knots[i1+1] <= knot) {
      ++i1;
    }
    while (p2Knots[i2+1] <= knot) {
      ++i2;
    }
    functions.push_back(std::shared_ptr<Function>{ChMath::multiply(*p1func[i1], *p2func[i2]).release()});
  }
  
  return std::unique_ptr<Function>{new Piecewise{knots, functions}};
}

std::unique_ptr<Function> multiplySplines(const Function& f1, const Function& f2) {
  const Piecewise& p1 = dynamic_cast<const Piecewise&>(f1);
  const Piecewise& p2 = dynamic_cast<const Piecewise&>(f2);
  
  auto p1Knots = p1.getKnots();
  auto p2Knots = p2.getKnots();
  if (p1Knots.front() >= p2Knots.back() || p1Knots.back() <= p2Knots.front()) {
    return std::unique_ptr<Function> {new Polynomial{{0.}}};
  }
  
  std::set<double> knotSet {};
  auto p1Iter = p1Knots.begin();
  auto p2Iter = p2Knots.begin();
  bool started = false;
  while (p1Iter != p1Knots.end() && p2Iter != p2Knots.end()) {
    if (!started) {
      if (*p1Iter < *p2Iter) {
        if (*(++p1Iter) > *p2Iter) {
          started = true;
        }
      } else {
        if (*p1Iter < *(++p2Iter)) {
          started = true;
        }
      }
      continue;
    }
    if (*p1Iter < *p2Iter) {
      knotSet.insert(*p1Iter);
      ++p1Iter;
    } else {
      knotSet.insert(*p2Iter);
      ++p2Iter;
    }
  }
  std::vector<double> knots {knotSet.begin(), knotSet.end()};
  std::vector<double> values {};
  for (double knot : knots) {
    values.push_back(f1(knot)*f2(knot));
  }
  return ChMath::interpolate(knots, values, InterpolationType::CUBIC_SPLINE);
}

std::map<std::pair<std::type_index,std::type_index>, MultiplyFunction> multiplySpecificSpecificMap {
  {std::pair<std::type_index,std::type_index>(typeid(Polynomial),typeid(Polynomial)), multiplyPolynomials},
  {std::pair<std::type_index,std::type_index>(typeid(Piecewise),typeid(Piecewise)), multiplyPiecewises},
  {std::pair<std::type_index,std::type_index>(typeid(Spline),typeid(Spline)), multiplySplines}
};

std::map<std::type_index, MultiplyFunction> multiplySpecificGenericMap {
  {typeid(Piecewise), multiplyPiecewiseWithGeneric}
};

} // End of ChMath