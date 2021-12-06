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

#include "AlexandriaKernel/memory_tools.h"
#include "MathUtils/function/Function.h"
#include "mocks.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::MathUtils;

class ABinaryFunction final : public BinaryFunction {
public:
  ABinaryFunction(double a, double b, double c) : m_a(a), m_b(b), m_c(c) {}

  double operator()(double x, double y) const override {
    return m_a * x + m_b * y + m_c;
  }

  void operator()(const std::vector<double>& xs, const std::vector<double>& ys,
                  std::vector<double>& out) const override {
    out.resize(xs.size());
    for (size_t i = 0; i < xs.size(); ++i) {
      out[i] = (*this)(xs[i], ys[i]);
    }
  }

  std::unique_ptr<BinaryFunction> clone() const override {
    return Euclid::make_unique<ABinaryFunction>(m_a, m_b, m_c);
  }

private:
  double m_a, m_b, m_c;
};

//-----------------------------------------------------------------------------

class ATernaryFunction final : public TernaryFunction {
public:
  ATernaryFunction(double a, double b, double c) : m_a(a), m_b(b), m_c(c) {}

  double operator()(double x, double y, double z) const override {
    return m_a * x + m_b * y + m_c * z;
  }

  void operator()(const std::vector<double>& xs, const std::vector<double>& ys, const std::vector<double>& zs,
                  std::vector<double>& out) const override {
    out.resize(xs.size());
    for (size_t i = 0; i < xs.size(); ++i) {
      out[i] = m_a * xs[i] + m_b * ys[i] + m_c * zs[i];
    }
  }

  std::unique_ptr<TernaryFunction> clone() const override {
    return Euclid::make_unique<ATernaryFunction>(m_a, m_b, m_c);
  }

private:
  double m_a, m_b, m_c;
};

//-----------------------------------------------------------------------------

template <std::size_t N>
void ThisShouldCompileJustFine(NAryFunction<N>& func, std::size_t n) {
  auto clone = func.clone();
  BOOST_CHECK(clone);
  BOOST_CHECK_EQUAL(N, n);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(NAryFunction_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(BinaryTest) {
  auto function = Euclid::make_unique<ABinaryFunction>(2, 3, 42);
  BOOST_CHECK_EQUAL((*function)(10, 20), 10 * 2 + 20 * 3 + 42);

  auto cloned = function->clone();
  BOOST_CHECK_EQUAL((*cloned)(2, 1), 2 * 2 + 1 * 3 + 42);

  ThisShouldCompileJustFine(*function, 2);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(TernaryTest) {
  auto function = Euclid::make_unique<ATernaryFunction>(4, 8, 2);

  BOOST_CHECK_EQUAL((*function)(10, 5, 1), 10 * 4 + 5 * 8 + 1 * 2);

  auto cloned = function->clone();
  BOOST_CHECK_EQUAL((*cloned)(4, 9, 3), 4 * 4 + 9 * 8 + 3 * 2);

  ThisShouldCompileJustFine(*function, 3);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(FunctionAsNary1Test) {
  std::unique_ptr<Function> function = Euclid::make_unique<FunctionMock>(88);
  ThisShouldCompileJustFine(*function, 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
