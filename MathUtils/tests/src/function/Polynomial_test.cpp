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
 * @file tests/src/function/Polynomial_test.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Real.h"
#include "MathUtils/function/Polynomial.h"
#include <boost/test/test_tools.hpp>
#if BOOST_VERSION >= 105900
#include <boost/test/tools/floating_point_comparison.hpp>
#else
#include <boost/test/floating_point_comparison.hpp>
#endif
#include <boost/test/unit_test.hpp>
#include <memory>
#include <sstream>

struct Polynomial_Fixture {
  double relative_error_tolerance{1E-10};
  template <typename T>
  void AlmostEqualRelative(T expected, T actual) {
    T relative_error = (expected - actual) / actual;
    if (relative_error < 0) {
      relative_error = -relative_error;
    }
    if (relative_error > relative_error_tolerance) {
      std::stringstream error_message;
      error_message << "Expected " << expected << " but got " << actual;
      BOOST_ERROR(error_message.str());
    }
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Polynomial_test)

//-----------------------------------------------------------------------------
// Test that the constructor sets the coefficients correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor, Polynomial_Fixture) {

  // Given
  std::vector<double>           coef{2.5, 0.8, -1.3, 0.02};
  Euclid::MathUtils::Polynomial polynomial{coef};

  // When
  std::vector<double> resCoef = polynomial.getCoefficients();

  // Then
  BOOST_CHECK_EQUAL_COLLECTIONS(resCoef.begin(), resCoef.end(), coef.begin(), coef.end());
}

//-----------------------------------------------------------------------------
// Test that the clone works correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Clone, Polynomial_Fixture) {

  // Given
  std::vector<double>           coef{2.5, 0.8, -1.3, 0.02};
  Euclid::MathUtils::Polynomial polynomial{coef};

  // When
  auto clonePtr = polynomial.clone();

  // Then
  BOOST_CHECK(clonePtr);
  Euclid::MathUtils::Polynomial* resPol = dynamic_cast<Euclid::MathUtils::Polynomial*>(clonePtr.get());
  BOOST_CHECK(resPol);
  std::vector<double> resCoef = resPol->getCoefficients();
  BOOST_CHECK_EQUAL_COLLECTIONS(resCoef.begin(), resCoef.end(), coef.begin(), coef.end());
}

//-----------------------------------------------------------------------------
// Test that the polynomial works correctly as a function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(FunctionOperator, Polynomial_Fixture) {

  // Given
  std::vector<double>           coef{2.5, 0.8, -1.3, 0.02};
  Euclid::MathUtils::Polynomial polynomial{coef};

  for (size_t i = 0; i < 200; ++i) {
    double x = -10. + (static_cast<double>(i) * 0.1);
    // When
    double expected = 2.5 + 0.8 * x - 1.3 * x * x + 0.02 * x * x * x;
    double polValue = polynomial(x);

    // Then
    AlmostEqualRelative(expected, polValue);
  }
}

//-----------------------------------------------------------------------------
// Test the derivative
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Derivative, Polynomial_Fixture) {

  // Given
  std::vector<double>           polCoef{2.5, 0.8, -1.3, 0.02};
  std::vector<double>           expectedCoef{0.8, -2.6, 0.06};
  Euclid::MathUtils::Polynomial polynomial{polCoef};

  // When
  auto derivative = std::dynamic_pointer_cast<Euclid::MathUtils::Polynomial>(polynomial.derivative());

  // Then
  BOOST_CHECK(derivative);
  std::vector<double> derCoef = derivative->getCoefficients();
  BOOST_CHECK_EQUAL_COLLECTIONS(derCoef.begin(), derCoef.end(), expectedCoef.begin(), expectedCoef.end());
}

//-----------------------------------------------------------------------------
// Test the indefinite integral
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(IndefiniteIntegral, Polynomial_Fixture) {

  // Given
  std::vector<double>           polCoef{2.5, 0.8, -1.5, 0.02};
  std::vector<double>           expectedCoef{0., 2.5, 0.4, -0.5, 0.005};
  Euclid::MathUtils::Polynomial polynomial{polCoef};

  // When
  auto indefiniteIntegral = std::dynamic_pointer_cast<Euclid::MathUtils::Polynomial>(polynomial.indefiniteIntegral());

  // Then
  BOOST_CHECK(indefiniteIntegral);
  std::vector<double> indefIntCoef = indefiniteIntegral->getCoefficients();
  BOOST_CHECK_EQUAL_COLLECTIONS(indefIntCoef.begin(), indefIntCoef.end(), expectedCoef.begin(), expectedCoef.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
