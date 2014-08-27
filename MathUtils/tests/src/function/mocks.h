/** 
 * @file tests/src/function/mocks.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MOCKS_H
#define	MOCKS_H

#include "MathUtils/function/Function.h"
#include "MathUtils/function/Integrable.h"
#include "MathUtils/function/Differentiable.h"

class FunctionMock : public Euclid::ChMath::Function {
public:
  FunctionMock(const double value) : m_value{value} { }
  double operator()(const double) const {
    return m_value;
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> {new FunctionMock{m_value}};
  }
private:
  double m_value;
};

class IntegrableMock : public Euclid::ChMath::Integrable {
public:
  IntegrableMock(const double value) : m_value{value} { }
  double operator()(const double) const {
    return m_value;
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> {new IntegrableMock{m_value}};
  }
  double integrate(const double min, const double max) const {
    m_min = min;
    m_max = max;
    return m_value * (max - min);
  }
  mutable double m_min {0};
  mutable double m_max {0};
private:
  double m_value;
};

class DifferentiableMock : public Euclid::ChMath::Differentiable {
public:
  double operator()(const double x) const {
    if (x < 0) {
      return 0;
    } else {
      return 1;
    }
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> {new DifferentiableMock{}};
  }
  std::shared_ptr<Euclid::ChMath::Function> derivative() const {
    return nullptr;
  }
  std::shared_ptr<Euclid::ChMath::Function> indefiniteIntegral() const {
    if (!m_func) {
      m_func.reset(new DifferentiableMock{});
    }
    return m_func;
  }
private:
  mutable std::shared_ptr<Euclid::ChMath::Function> m_func {};
};


#endif	/* MOCKS_H */

