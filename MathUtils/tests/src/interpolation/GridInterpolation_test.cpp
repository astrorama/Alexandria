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

#include "MathUtils/interpolation/GridInterpolation.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::MathUtils;
using namespace Euclid::NdArray;

enum class EnumType { A, B, C, D, E };

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridInterpolation_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(DiscreteAxis1) {
  std::vector<EnumType> knots{EnumType::A, EnumType::B, EnumType::C, EnumType::E};
  NdArray<double>       values({4}, {1, 10, 20, 3});

  InterpN<EnumType> interp1(std::tuple<std::vector<EnumType>>(knots), values, false);
  BOOST_CHECK_EQUAL(interp1(EnumType::A), 1);
  BOOST_CHECK_EQUAL(interp1(EnumType::B), 10);
  BOOST_CHECK_EQUAL(interp1(EnumType::C), 20);
  BOOST_CHECK_EQUAL(interp1(EnumType::D), 0);
  BOOST_CHECK_EQUAL(interp1(EnumType::E), 3);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(CombinedAxes2) {
  std::vector<EnumType> knots0{EnumType::A, EnumType::B, EnumType::C, EnumType::E};
  std::vector<double>   knots1{0., 1., 2., 3., 4.};
  NdArray<double>       values({4, 5}, {                     //
                                  1,  2,  4,  3,  5,   //
                                  6,  8,  9,  10, 11,  //
                                  90, 80, 70, 60, 65,  //
                                  1,  1,  1,  1,  1});

  InterpN<EnumType, double> interp2(std::tuple<std::vector<EnumType>, std::vector<double>>(knots0, knots1), values, true);

  BOOST_CHECK_EQUAL(interp2(EnumType::A, 1.), 2);
  BOOST_CHECK_CLOSE(interp2(EnumType::B, 2.5), 9.5, 1e-8);
  BOOST_CHECK_CLOSE(interp2(EnumType::C, 5.), 70, 1e-8);  // Extrapolated
  BOOST_CHECK_EQUAL(interp2(EnumType::D, 4.), 0.);        // d is not defined
  BOOST_CHECK_CLOSE(interp2(EnumType::E, 1.328), 1., 1e-8);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(CombinedAxesReversed2) {
  std::vector<double>   knots0{0., 1., 2., 3., 4.};
  std::vector<EnumType> knots1{EnumType::A, EnumType::B, EnumType::C, EnumType::E};

  NdArray<double> values({5, 4}, {                 //
                                  1,  4,  3,  5,   //
                                  6,  9,  10, 11,  //
                                  90, 70, 60, 65,  //
                                  1,  1,  1,  1,   //
                                  0,  3,  0,  0});

  InterpN<double, EnumType> interp2(std::tuple<std::vector<double>, std::vector<EnumType>>(knots0, knots1), values, true);

  BOOST_CHECK_EQUAL(interp2(1., EnumType::A), 6);
  BOOST_CHECK_CLOSE(interp2(2.5, EnumType::B), 35.5, 1e-8);
  BOOST_CHECK_CLOSE(interp2(5., EnumType::C), -1, 1e-8);  // Extrapolated
  BOOST_CHECK_EQUAL(interp2(4., EnumType::D), 0.);        // d is not defined
  BOOST_CHECK_CLOSE(interp2(0.5, EnumType::E), 8., 1e-8);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(CopyConstructor) {
  std::vector<double>   knots0{0., 1., 2., 3., 4.};
  std::vector<EnumType> knots1{EnumType::A, EnumType::B, EnumType::C, EnumType::E};

  NdArray<double> values({5, 4}, {                 //
                                  1,  4,  3,  5,   //
                                  6,  9,  10, 11,  //
                                  90, 70, 60, 65,  //
                                  1,  1,  1,  1,   //
                                  0,  3,  0,  0});

  InterpN<double, EnumType> interp2(std::tuple<std::vector<double>, std::vector<EnumType>>(knots0, knots1), values, true);

  BOOST_CHECK_EQUAL(interp2(1., EnumType::A), 6);
  BOOST_CHECK_CLOSE(interp2(2.5, EnumType::B), 35.5, 1e-8);

  InterpN<double, EnumType> interp_copy(interp2);

  BOOST_CHECK_EQUAL(interp_copy(1., EnumType::A), 6);
  BOOST_CHECK_CLOSE(interp_copy(2.5, EnumType::B), 35.5, 1e-8);
  BOOST_CHECK_CLOSE(interp_copy(5., EnumType::C), -1, 1e-8);  // Extrapolated
  BOOST_CHECK_EQUAL(interp_copy(4., EnumType::D), 0.);        // d is not defined
  BOOST_CHECK_CLOSE(interp_copy(0.5, EnumType::E), 8., 1e-8);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(SingleDiscreteValue) {
  std::vector<double>   knots0{0., 1., 2., 3.};
  std::vector<EnumType> knots1{EnumType::A};
  NdArray<double>       values({4, 1}, {1., 2., 3., 4.});

  InterpN<double, EnumType> interp(std::tuple<std::vector<double>, std::vector<EnumType>>(knots0, knots1), values, true);

  BOOST_CHECK_CLOSE(interp(1., EnumType::A), 2., 1e-8);
  BOOST_CHECK_CLOSE(interp(2.5, EnumType::A), 3.5, 1e-8);
  BOOST_CHECK_EQUAL(interp(1.8, EnumType::B), 0.0);

  // Swap axes
  InterpN<EnumType, double> interp2(std::tuple<std::vector<EnumType>, std::vector<double>>(knots1, knots0), values.reshape(1, 4),
                                    true);
  BOOST_CHECK_CLOSE(interp2(EnumType::A, 1.), 2., 1e-8);
  BOOST_CHECK_CLOSE(interp2(EnumType::A, 2.5), 3.5, 1e-8);
  BOOST_CHECK_EQUAL(interp2(EnumType::B, 1.8), 0.0);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(SingleContinuousValue) {
  std::vector<double>   knots0{1.};
  std::vector<EnumType> knots1{EnumType::A, EnumType::B, EnumType::C};
  NdArray<double>       values({1, 3}, {2., 3., 4.});

  InterpN<double, EnumType> interp(std::tuple<std::vector<double>, std::vector<EnumType>>(knots0, knots1), values, true);

  BOOST_CHECK_CLOSE(interp(1., EnumType::A), 2., 1e-8);
  BOOST_CHECK_CLOSE(interp(1., EnumType::B), 3., 1e-8);
  BOOST_CHECK_CLOSE(interp(1.5, EnumType::B), 3., 1e-8);  // The only sensible extrapolation is assume a constant value
  BOOST_CHECK_EQUAL(interp(1.8, EnumType::D), 0.0);

  // Swap axes
  InterpN<EnumType, double> interp2(std::tuple<std::vector<EnumType>, std::vector<double>>(knots1, knots0), values.reshape(3, 1),
                                    true);
  BOOST_CHECK_CLOSE(interp2(EnumType::A, 1.), 2., 1e-8);
  BOOST_CHECK_CLOSE(interp2(EnumType::A, 2.5), 2., 1e-8);
  BOOST_CHECK_CLOSE(interp2(EnumType::B, 1.), 3., 1e-8);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(BadConstructor) {
  std::vector<double>   knots0{0., 1., 2., 3., 4.};
  std::vector<EnumType> knots1{EnumType::A, EnumType::B, EnumType::C, EnumType::E};

  NdArray<double> values({2, 2});

  // Bad grid shape
  try {
    InterpN<double, EnumType> x(std::tuple<std::vector<double>, std::vector<EnumType>>(knots0, knots1), values, true);
    BOOST_FAIL("Constructor should have thrown");
  } catch (const InterpolationException&) {
  }

  // Knots not sorted
  try {
    InterpN<double, double> x(std::tuple<std::vector<double>, std::vector<double>>({2, 0}, {1, 2}), values, true);
    BOOST_FAIL("Constructor should have thrown");
  } catch (const InterpolationException&) {
  }

  // Grid does not have proper number of axes
  try {
    std::tuple<std::vector<double>, std::vector<double>, std::vector<double>> knots({1, 2}, {3, 4}, {1});
    InterpN<double, double, double>                                           x(knots, values, true);
    BOOST_FAIL("Constructor should have thrown");
  } catch (const InterpolationException&) {
  }

  try {
    InterpN<double> x(std::tuple<std::vector<double>>({1, 2, 3, 4}), values, true);
    BOOST_FAIL("Constructor should have thrown");
  } catch (const InterpolationException&) {
  }

  // Good dimensions, bad size
  try {
    InterpN<double, double> x(std::tuple<std::vector<double>, std::vector<double>>({1, 2, 3}, {5, 6}), values, true);
    BOOST_FAIL("Constructor should have thrown");
  } catch (const InterpolationException&) {
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
