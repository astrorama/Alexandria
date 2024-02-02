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

#include "MathUtils/interpolation/interpolation.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::MathUtils;
using namespace Euclid::NdArray;

static double close_tolerance{1E-10};

//-----------------------------------------------------------------------------

/**
def value_func_1d(x):
    return 2 * x
x = np.arange(0, 3)
values = value_func_1d(x)
 */
struct Fixture1D {
  std::vector<double> x{0, 1, 2};
  NdArray<double>     values{{3}, {0, 2, 4}};
};

//-----------------------------------------------------------------------------

/**
from scipy.interpolate import interpn
import numpy as np

def value_func_2d(x0, x1):
    return 2 * x0 + 3 * x1
x0 = np.arange(0, 3)
x1 = np.arange(0, 3)
values = value_func_2d(*np.meshgrid(x0, x1, indexing='ij'))
 */
struct Fixture2D {
  std::vector<double> x0{0, 1, 2};
  std::vector<double> x1{0, 1, 2};
  NdArray<double>     values{{3, 3}, {0, 3, 6, 2, 5, 8, 4, 7, 10}};
};

//-----------------------------------------------------------------------------
/**
from scipy.interpolate import interpn
import numpy as np

def value_func_3d(x0, x1, x2):
    return 5 * x0 + 8 * x1 - x2
x0 = np.arange(0, 3)
x1 = np.arange(0, 3)
x2 = np.arange(0, 3)
values = value_func_3d(*np.meshgrid(x0, x1, x2, indexing='ij'))
 */
struct Fixture3D {
  std::vector<double> x0{0, 1, 2};
  std::vector<double> x1{0, 1, 2};
  std::vector<double> x2{0, 1, 2};
  NdArray<double>     values{
          {3, 3, 3}, {0, -1, -2, 8, 7, 6, 16, 15, 14, 5, 4, 3, 13, 12, 11, 21, 20, 19, 10, 9, 8, 18, 17, 16, 26, 25, 24}};
};

//-----------------------------------------------------------------------------
/**
 * Ok, I am stopping here :D
 *
from scipy.interpolate import interpn
import numpy as np

def value_func_4d(x0, x1, x2, x3):
    return 5 * x0 + 8 * x1 - x2 * x3
x0 = np.arange(0, 3)
x1 = np.arange(0, 3)
x2 = np.arange(0, 3)
x3 = np.linspace(0, 5, 5)
values = value_func_4d(*np.meshgrid(x0, x1, x2, x3, indexing='ij'))
 */
struct Fixture4D {
  std::vector<double> x0{0, 1, 2};
  std::vector<double> x1{0, 1, 2};
  std::vector<double> x2{0, 1, 2};
  std::vector<double> x3{0., 1.25, 2.5, 3.75, 5.};
  NdArray<double>     values{{3, 3, 3, 5},
                             {//
                          0.,  0.,  0.,  0.,  0.,  0.,  -1.25, -2.5, -3.75, -5., 0.,  -2.5, -5., -7.5, -10.,
                          8.,  8.,  8.,  8.,  8.,  8.,  6.75,  5.5,  4.25,  3.,  8.,  5.5,  3.,  0.5,  -2.,
                          16., 16., 16., 16., 16., 16., 14.75, 13.5, 12.25, 11., 16., 13.5, 11., 8.5,  6.,
                          5.,  5.,  5.,  5.,  5.,  5.,  3.75,  2.5,  1.25,  0.,  5.,  2.5,  0.,  -2.5, -5.,
                          13., 13., 13., 13., 13., 13., 11.75, 10.5, 9.25,  8.,  13., 10.5, 8.,  5.5,  3.,
                          21., 21., 21., 21., 21., 21., 19.75, 18.5, 17.25, 16., 21., 18.5, 16., 13.5, 11.,
                          10., 10., 10., 10., 10., 10., 8.75,  7.5,  6.25,  5.,  10., 7.5,  5.,  2.5,  0.,
                          18., 18., 18., 18., 18., 18., 16.75, 15.5, 14.25, 13., 18., 15.5, 13., 10.5, 8.,
                          26., 26., 26., 26., 26., 26., 24.75, 23.5, 22.25, 21., 26., 23.5, 21., 18.5, 16.}};
};

//-----------------------------------------------------------------------------

/**
 * A 2D rectangular grid
from scipy.interpolate import interpn
import numpy as np

def value_func_2d(x0, x1):
    return 2 * x0 + 3 * x1
x0 = np.arange(0, 5)
x1 = np.arange(0, 3)
values = value_func_2d(*np.meshgrid(x0, x1, indexing='ij'))
 */
struct FixtureRectangle2D {
  std::vector<double> x0{0, 1, 2, 3, 4};
  std::vector<double> x1{0, 1, 2};
  // Note that y corresponds to the axis 0!
  NdArray<double> values{{5, 3}, {0, 3, 6, 2, 5, 8, 4, 7, 10, 6, 9, 12, 8, 11, 14}};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(NDimensional_Test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Interp1D, Fixture1D) {
  auto func = interpn<1>({x}, values, InterpolationType::LINEAR, false);
  BOOST_CHECK(func);
  // interpn(x, values, [1.45],
  BOOST_CHECK_CLOSE((*func)(1.45), 2.9, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(0.40), 0.8, close_tolerance);
  BOOST_CHECK_EQUAL((*func)(-10), 0.);

  auto copy = func->clone();
  func.reset(nullptr);
  BOOST_CHECK_CLOSE((*copy)(1.45), 2.9, close_tolerance);
  BOOST_CHECK_CLOSE((*copy)(0.40), 0.8, close_tolerance);
  BOOST_CHECK_EQUAL((*copy)(-10), 0.0);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Interp1DExtrapolate, Fixture1D) {
  auto func = interpn<1>({x}, values, InterpolationType::LINEAR, true);
  // interpn(x, values, [-10.], bounds_error=False, fill_value=None)
  BOOST_CHECK_CLOSE((*func)(1.45), 2.9, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(-10), -20., close_tolerance);
  BOOST_CHECK_CLOSE((*func)(10), 20., close_tolerance);

  auto copy = func->clone();
  func.reset(nullptr);
  BOOST_CHECK_CLOSE((*copy)(1.45), 2.9, close_tolerance);
  BOOST_CHECK_CLOSE((*copy)(-10), -20., close_tolerance);
  BOOST_CHECK_CLOSE((*copy)(10), 20., close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Interp2D, Fixture2D) {
  auto func = interpn<2>({x0, x1}, values, InterpolationType::LINEAR, false);
  BOOST_CHECK(func);
  // interpn((x0,x1), values, [0.5, 0.4])
  BOOST_CHECK_CLOSE((*func)(0.5, 0.4), 2.2, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(0.4, 0.5), 2.3, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.8, 0.6), 5.4, close_tolerance);
  BOOST_CHECK_EQUAL((*func)(-10, 1.5), 0.0);
  BOOST_CHECK_EQUAL((*func)(1.9, 5.5), 0.0);

  auto copy = func->clone();
  func.reset(nullptr);
  BOOST_CHECK(copy);
  BOOST_CHECK_CLOSE((*copy)(0.4, 0.5), 2.3, close_tolerance);
  BOOST_CHECK_CLOSE((*copy)(1.8, 0.6), 5.4, close_tolerance);
  BOOST_CHECK_EQUAL((*copy)(-10, 1.5), 0.0);
  BOOST_CHECK_EQUAL((*copy)(1.9, 5.5), 0.0);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Interp2DExtrapolate, Fixture2D) {
  auto func = interpn<2>({x0, x1}, values, InterpolationType::LINEAR, true);
  BOOST_CHECK_CLOSE((*func)(0.4, 0.5), 2.3, close_tolerance);
  // interpn((x0,x1), values, [-10., 1.5], bounds_error=False, fill_value=None)
  BOOST_CHECK_CLOSE((*func)(-10, 1.5), -15.5, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.9, 5.5), 20.3, close_tolerance);

  auto copy = func->clone();
  func.reset(nullptr);
  BOOST_CHECK_CLOSE((*copy)(-10, 1.5), -15.5, close_tolerance);
  BOOST_CHECK_CLOSE((*copy)(1.9, 5.5), 20.3, close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Interp3D, Fixture3D) {
  auto func = interpn<3>({x0, x1, x2}, values, InterpolationType::LINEAR, false);
  BOOST_CHECK(func);
  // interpn((x0,x1,x2), values, [0.4, 0.5, 1.1])
  BOOST_CHECK_CLOSE((*func)(0.4, 0.5, 1.1), 4.9, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.3, 0.8, 0.0), 12.9, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(0.0, 0.0, 0.1), -0.1, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(0.0, 0.1, 0.1), 0.7, close_tolerance);
  // No extrapolation
  BOOST_CHECK_CLOSE((*func)(-1.0, 0.1, 0.1), 0.0, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(10.0, 0.1, 0.1), 0.0, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, -0.1, 0.1), 0.0, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, 10.1, 0.1), 0.0, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, 0.1, 10.1), 0.0, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, 0.1, -0.8), 0.0, close_tolerance);

  auto copy = func->clone();
  func.reset(nullptr);
  BOOST_CHECK(copy);
  BOOST_CHECK_CLOSE((*copy)(0.4, 0.5, 1.1), 4.9, close_tolerance);
  BOOST_CHECK_CLOSE((*copy)(1.1, 10.1, 0.1), 0.0, close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Interp3DExtrapolate, Fixture3D) {
  auto func = interpn<3>({x0, x1, x2}, values, InterpolationType::LINEAR, true);

  BOOST_CHECK_CLOSE((*func)(0.4, 0.5, 1.1), 4.9, close_tolerance);
  // interpn((x0,x1,x2), values, [-1.0, 0.1, 0.1], bounds_error=False, fill_value=None)
  BOOST_CHECK_CLOSE((*func)(-1.0, 0.1, 0.1), -4.3, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(10.0, 0.1, 0.1), 50.7, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, -0.1, 0.1), 4.6, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, 10.1, 0.1), 86.2, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, 0.1, 10.1), -3.8, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(1.1, 0.1, -0.8), 7.1, close_tolerance);

  auto copy = func->clone();
  func.reset(nullptr);
  BOOST_CHECK_CLOSE((*copy)(1.1, 0.1, -0.8), 7.1, close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Interp4D, Fixture4D) {
  auto func = interpn<4>({x0, x1, x2, x3}, values, InterpolationType::LINEAR, true);
  // interpn((x0,x1,x2,x3), values, [0.5, 0.5, 0.5, 0.5], bounds_error=False, fill_value=None)
  BOOST_CHECK_CLOSE((*func)(0.5, 0.5, 0.5, 0.5), 6.25, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(0.0, 0.1, 1.6, 4.5), -6.4, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(0.0, -0.1, 2.6, 5.5), -15.1, close_tolerance);

  auto copy = func->clone();
  func.reset(nullptr);
  BOOST_CHECK_CLOSE((*copy)(0.5, 0.5, 0.5, 0.5), 6.25, close_tolerance);
  BOOST_CHECK_CLOSE((*copy)(0.0, -0.1, 2.6, 5.5), -15.1, close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(InterpRectable2D, FixtureRectangle2D) {
  auto func = interpn<2>({x0, x1}, values, InterpolationType::LINEAR, false);
  // interpn((x0,x1), values, [0.4, 0.5])
  BOOST_CHECK_CLOSE((*func)(0.4, 0.5), 2.3, close_tolerance);
  BOOST_CHECK_CLOSE((*func)(4., 2.), 14., close_tolerance);
  // This extrapolates!
  BOOST_CHECK_CLOSE((*func)(2., 4.), 0., close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
