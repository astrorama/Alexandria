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
#include "MathUtils/helpers/InverseCumulative.h"
#include <boost/test/unit_test.hpp>

using Euclid::MathUtils::InverseCumulative;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(InverseCumulative_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InverseCumulativeContinuous_test) {
  std::vector<float>  knots{-1.0, -0.5, -0.3, 0.0, 0.3, 0.5, 1.0};
  std::vector<double> pdf{0.0, 0.05, 0.2, 0.5, 0.2, 0.05, 0.0};

  InverseCumulative<float> cumulative(knots, pdf);

  BOOST_CHECK_CLOSE(cumulative(1.0), 1.00, 1e-4);
  // Median
  BOOST_CHECK_SMALL(cumulative(0.5), 1e-4);
  // Half-way between -0.5 and -0.3, it should lean towards -0.3 since the CDF is quadratic
  BOOST_CHECK_CLOSE_FRACTION(cumulative(0.15), -0.27, 1e-1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InverseCumulativeUniform_test) {
  std::vector<float>  knots{-2.0, -1.0, 0.0, 1.0, 2.0};
  std::vector<double> pdf{1.0, 1.0, 1.0, 1.0, 1.0};

  InverseCumulative<float> cumulative(knots, pdf);

  BOOST_CHECK_SMALL(cumulative(0.5), 1e-4);
  BOOST_CHECK_CLOSE(cumulative(0.6), 0.4, 1e-4);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InverseCumulativeContinuousStep_test) {
  std::vector<float>  knots{-1.0, -0.5, -0.5, -0.3, 0.0, 0.0, 1.0};
  std::vector<double> pdf{0.0, 0.0, 0.2, 0.5, 0.2, 0.0, 0.0};

  InverseCumulative<float> cumulative(knots, pdf);

  BOOST_CHECK_SMALL(cumulative(1.0), 1e-4);
  BOOST_CHECK_LT(cumulative(0.2), -0.3);
  BOOST_CHECK_GE(cumulative(0.2), -0.5);
  BOOST_CHECK_LT(cumulative(0.2), cumulative(0.3));
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InverseBadKnots_test) {
  std::vector<float>  knots{-1.0, -0.5, 0.5, -0.3, 0.0};
  std::vector<double> pdf{0.0, 0.0, 0.2, 0.5, 0.2, 0.0};

  try {
    InverseCumulative<float> cumulative(knots, pdf);
    BOOST_FAIL("Must throw with unsorted knots");
  } catch (const Elements::Exception&) {
    // pass
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InverseCumulativeContinuousSingle_test) {
  std::vector<float>  knots{150};
  std::vector<double> pdf{1.};

  InverseCumulative<float> cumulative(knots, pdf);

  BOOST_CHECK_CLOSE(cumulative(1.0), 150, 1e-6);
  BOOST_CHECK_CLOSE(cumulative(0.1), 150, 1e-6);
  BOOST_CHECK_CLOSE(cumulative(0.5), 150, 1e-6);
}

//-----------------------------------------------------------------------------
BOOST_AUTO_TEST_CASE(InverseCumulativeDiscrete_test) {
  std::vector<std::string> knots{"A", "B", "C", "E", "F"};  // F is missing, and not in order, which should be ok
  std::vector<double>      pdf{0.15, 0.1, 0.5, 0.2, 0.05};

  InverseCumulative<std::string> cumulative(knots, pdf);
  BOOST_CHECK_EQUAL(cumulative(0.15), "A");
  BOOST_CHECK_EQUAL(cumulative(0.5), "C");
  BOOST_CHECK_EQUAL(cumulative(1.0), "F");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InverseCumulativeRepeatedDiscrete_test) {
  std::vector<std::string> knots{"A", "B", "F", "F", "C"};
  std::vector<double>      pdf{0.15, 0.1, 0.5, 0.2, 0.05};

  InverseCumulative<std::string> cumulative(knots, pdf);
  BOOST_CHECK_EQUAL(cumulative(0.15), "A");
  BOOST_CHECK_EQUAL(cumulative(0.5), "F");
  BOOST_CHECK_EQUAL(cumulative(0.8), "F");
  BOOST_CHECK_EQUAL(cumulative(1.0), "C");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InverseCumulativeSingleDiscrete_test) {
  std::vector<std::string> knots{"A"};
  std::vector<double>      pdf{0.15};

  InverseCumulative<std::string> cumulative(knots, pdf);
  BOOST_CHECK_EQUAL(cumulative(0.15), "A");
  BOOST_CHECK_EQUAL(cumulative(0.5), "A");
  BOOST_CHECK_EQUAL(cumulative(0.8), "A");
  BOOST_CHECK_EQUAL(cumulative(1.0), "A");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
