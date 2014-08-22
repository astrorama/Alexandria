/**
 * @file src/lib/function/Polynomial.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <utility>
#include <cmath>
#include <memory>
#include "ChMath/function/Polynomial.h"

namespace Euclid {
namespace ChMath {

Polynomial::Polynomial(std::vector<double> coefficients) : m_coef{std::move(coefficients)} {
}

const std::vector<double>& Polynomial::getCoefficients() const {
  return m_coef;
}

double Polynomial::operator()(const double x) const {
  double result {};
  double xPow {1};
  for (double coef : m_coef) {
    result += coef * xPow;
    xPow *= x;
  }
  return result;
}

std::unique_ptr<Function> Polynomial::clone() const {
  return std::unique_ptr<Function> {new Polynomial(m_coef)};
}

std::shared_ptr<Function> Polynomial::derivative() const {
  if (!m_derivative) {
    std::vector<double> derivCoef {};
    for (size_t i = 1; i < m_coef.size(); i++) {
        derivCoef.push_back(i * this->m_coef[i]);
    }
    m_derivative.reset(new Polynomial{std::move(derivCoef)});
  }
  return m_derivative;
}

std::shared_ptr<Function> Polynomial::indefiniteIntegral() const {
  if (!m_indefIntegral) {
    std::vector<double> indefIntegCoef {};
    indefIntegCoef.push_back(0.);
    for (size_t i = 0; i < m_coef.size(); i++) {
        indefIntegCoef.push_back(m_coef[i] / (i+1));
    }
    m_indefIntegral.reset(new Polynomial{std::move(indefIntegCoef)});
  }
  return m_indefIntegral;
}

} // End of ChMath
} // end of namespace Euclid
