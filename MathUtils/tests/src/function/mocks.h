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
 * @file tests/src/std::unique_ptr<Euclid::MathUtils::Function>/mocks.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MOCKS_H
#define MOCKS_H

#include "MathUtils/function/Differentiable.h"
#include "MathUtils/function/Function.h"
#include "MathUtils/function/Integrable.h"

class FunctionMock : public Euclid::MathUtils::Function {
public:
  explicit FunctionMock(const double value) : m_value{value} {}
  double operator()(const double) const override {
    return m_value;
  }
  std::unique_ptr<Euclid::MathUtils::Function> clone() const override {
    return std::unique_ptr<Euclid::MathUtils::Function>{new FunctionMock{m_value}};
  }

private:
  double m_value;
};

class IntegrableMock : public Euclid::MathUtils::Integrable {
public:
  explicit IntegrableMock(const double value) : m_value{value} {}
  double operator()(const double) const override {
    return m_value;
  }
  std::unique_ptr<Euclid::MathUtils::Function> clone() const override {
    return std::unique_ptr<Euclid::MathUtils::Function>{new IntegrableMock{m_value}};
  }
  double integrate(const double min, const double max) const override {
    m_min = min;
    m_max = max;
    return m_value * (max - min);
  }
  mutable double m_min{0};
  mutable double m_max{0};

private:
  double m_value;
};

class DifferentiableMock : public Euclid::MathUtils::Differentiable {
public:
  double operator()(const double x) const override {
    if (x < 0) {
      return 0;
    } else {
      return 1;
    }
  }
  std::unique_ptr<Euclid::MathUtils::Function> clone() const override {
    return std::unique_ptr<Euclid::MathUtils::Function>{new DifferentiableMock{}};
  }
  std::shared_ptr<Euclid::MathUtils::Function> derivative() const override {
    return nullptr;
  }
  std::shared_ptr<Euclid::MathUtils::Function> indefiniteIntegral() const override {
    if (!m_func) {
      m_func.reset(new DifferentiableMock{});
    }
    return m_func;
  }

private:
  mutable std::shared_ptr<Euclid::MathUtils::Function> m_func{};
};

#endif /* MOCKS_H */
