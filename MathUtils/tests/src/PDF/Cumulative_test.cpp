/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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
 * @file tests/src/Cumulative_test.cpp
 * @date 01/11/18
 * @author fdubath
 */

#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Exception.h"
#include "MathUtils/PDF/Cumulative.h"
#include "XYDataset/XYDataset.h"
#include <utility>
#include <vector>

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Cumulative_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(constructor_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.};
  std::vector<double> y = {0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};

  BOOST_CHECK_NO_THROW(Euclid::MathUtils::Cumulative(x, y));
  auto cumul = Euclid::MathUtils::Cumulative(x, y);
  for (size_t i = 0; i < x.size(); ++i) {
    BOOST_CHECK_CLOSE(cumul.findValue(y[i]), x[i], 0.0001);
  }

  std::vector<double> yy = {0., 0.1, 0.2, 0.3, 0.4, 0.5};
  BOOST_CHECK_THROW(Euclid::MathUtils::Cumulative(x, yy), Elements::Exception);
}

BOOST_AUTO_TEST_CASE(normalize_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6};

  std::vector<double> ynorm = {0., 1. / 6., 1. / 3., 1. / 2., 2. / 3., 5. / 6., 1.};

  Euclid::MathUtils::Cumulative cumul{x, y};
  BOOST_CHECK_NO_THROW(cumul.normalize());

  for (size_t i = 0; i < x.size(); ++i) {
    BOOST_CHECK_CLOSE(cumul.findValue(ynorm[i]), x[i], 0.0001);
  }
}

BOOST_AUTO_TEST_CASE(normalize_XY_test) {
  std::vector<double>          x  = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double>          y  = {0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6};
  Euclid::XYDataset::XYDataset xy = Euclid::XYDataset::XYDataset::factory(x, y);

  std::vector<double> ynorm = {0., 1. / 6., 1. / 3., 1. / 2., 2. / 3., 5. / 6., 1.};

  Euclid::MathUtils::Cumulative cumul{xy};
  BOOST_CHECK_NO_THROW(cumul.normalize());

  for (size_t i = 0; i < x.size(); ++i) {
    BOOST_CHECK_CLOSE(cumul.findValue(ynorm[i]), x[i], 0.0001);
  }
}

BOOST_AUTO_TEST_CASE(findValue_test) {
  std::vector<double> x          = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y          = {0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6};
  double              expected_x = 0.;

  Euclid::MathUtils::Cumulative cumul{x, y};
  double                        res_x = cumul.findValue(0.);
  BOOST_CHECK_CLOSE(res_x, expected_x, 0.0001);

  expected_x = 3.;
  res_x      = cumul.findValue(0.5);
  BOOST_CHECK_CLOSE(res_x, expected_x, 0.0001);

  BOOST_CHECK_THROW(cumul.findValue(-1.), Elements::Exception);
  BOOST_CHECK_THROW(cumul.findValue(1.1), Elements::Exception);
}

BOOST_AUTO_TEST_CASE(findValue_tray_test) {
  std::vector<double>           x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double>           y = {0., 0.1, 0.3, 0.3, 0.3, 0.5, 0.6};
  Euclid::MathUtils::Cumulative cumul{x, y};

  double expected_x = 2.;
  double res_x      = cumul.findValue(0.5, Euclid::MathUtils::Cumulative::TrayPosition::begin);
  BOOST_CHECK_CLOSE(res_x, expected_x, 0.0001);

  expected_x = 3.;
  res_x      = cumul.findValue(0.5, Euclid::MathUtils::Cumulative::TrayPosition::middle);
  BOOST_CHECK_CLOSE(res_x, expected_x, 0.0001);

  expected_x = 4.;
  res_x      = cumul.findValue(0.5, Euclid::MathUtils::Cumulative::TrayPosition::end);
  BOOST_CHECK_CLOSE(res_x, expected_x, 0.0001);
}

BOOST_AUTO_TEST_CASE(findMinInterval_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {0., 0.1, 0.2, 0.7, 0.9, 0.95, 1.};

  Euclid::MathUtils::Cumulative cumul{x, y};

  std::pair<double, double> interval = cumul.findMinInterval(0.45);

  BOOST_CHECK_CLOSE(interval.first, 2., 0.0001);
  BOOST_CHECK_CLOSE(interval.second, 3., 0.0001);

  interval = cumul.findMinInterval(1.0);

  BOOST_CHECK_CLOSE(interval.first, 0., 0.0001);
  BOOST_CHECK_CLOSE(interval.second, 6., 0.0001);
}

BOOST_AUTO_TEST_CASE(fromPDF_test) {
  std::vector<double> x        = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y        = {0., 0.5, 0.2, 0.07, 0.08, 0.1, 0.05};
  std::vector<double> expected = {0., 0.5, 0.7, 0.77, 0.85, 0.95, 1.0};

  auto cumul = Euclid::MathUtils::Cumulative::fromPdf(x, y);

  for (size_t i = 0; i < x.size(); ++i) {
    BOOST_CHECK_CLOSE(cumul.findValue(expected[i]), x[i], 0.0001);
  }
}

BOOST_AUTO_TEST_CASE(fromPDF_XY_test) {
  std::vector<double>          x        = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double>          y        = {0., 0.5, 0.2, 0.07, 0.08, 0.1, 0.05};
  Euclid::XYDataset::XYDataset xy       = Euclid::XYDataset::XYDataset::factory(x, y);
  std::vector<double>          expected = {0., 0.5, 0.7, 0.77, 0.85, 0.95, 1.0};

  auto cumul = Euclid::MathUtils::Cumulative::fromPdf(xy);

  for (size_t i = 0; i < x.size(); ++i) {
    BOOST_CHECK_CLOSE(cumul.findValue(expected[i]), x[i], 0.0001);
  }
}

BOOST_AUTO_TEST_CASE(findMinInterval_throw_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {0., 0, 100, 100, 100, 100, 100};

  Euclid::MathUtils::Cumulative cumul{x, y};
  BOOST_CHECK_THROW(cumul.findMinInterval(-0.1), Elements::Exception);
  BOOST_CHECK_THROW(cumul.findMinInterval(0), Elements::Exception);
  BOOST_CHECK_NO_THROW(cumul.findMinInterval(0.5));
  BOOST_CHECK_NO_THROW(cumul.findMinInterval(1.0));
  BOOST_CHECK_THROW(cumul.findMinInterval(1.1), Elements::Exception);
}

BOOST_AUTO_TEST_CASE(findMinInterval_prob_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {0., 0, 100, 100, 100, 100, 100};

  Euclid::MathUtils::Cumulative cumul{x, y};

  std::pair<double, double> interval = cumul.findMinInterval(0.7);

  BOOST_CHECK_CLOSE(interval.first, 1., 0.0001);
  BOOST_CHECK_CLOSE(interval.second, 2., 0.0001);
}

BOOST_AUTO_TEST_CASE(findMinInterval_prob2_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {99., 100, 100, 100, 100, 100, 100};

  Euclid::MathUtils::Cumulative cumul{x, y};

  std::pair<double, double> interval = cumul.findMinInterval(0.7);

  BOOST_CHECK_CLOSE(interval.first, 0., 0.0001);
  BOOST_CHECK_CLOSE(interval.second, 1., 0.0001);
}

BOOST_AUTO_TEST_CASE(findCenteredInterval_throw_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {0., 0, 100, 100, 100, 100, 100};

  Euclid::MathUtils::Cumulative cumul{x, y};
  BOOST_CHECK_THROW(cumul.findCenteredInterval(-0.1), Elements::Exception);
  BOOST_CHECK_THROW(cumul.findCenteredInterval(0), Elements::Exception);
  BOOST_CHECK_NO_THROW(cumul.findCenteredInterval(0.5));
  BOOST_CHECK_NO_THROW(cumul.findCenteredInterval(1.0));
  BOOST_CHECK_THROW(cumul.findCenteredInterval(1.1), Elements::Exception);
}

BOOST_AUTO_TEST_CASE(findCenteredInterval_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {0., 10, 30, 50, 80, 90, 100};

  Euclid::MathUtils::Cumulative cumul{x, y};

  std::pair<double, double> interval = cumul.findCenteredInterval(0.8);
  BOOST_CHECK_CLOSE(interval.first, 1., 0.0001);
  BOOST_CHECK_CLOSE(interval.second, 5., 0.0001);
}

BOOST_AUTO_TEST_CASE(findCenteredInterval_tray_test) {
  std::vector<double> x = {0., 1., 2., 3., 4., 5., 6.};
  std::vector<double> y = {0., 10, 10, 50, 90, 90, 100};

  Euclid::MathUtils::Cumulative cumul{x, y};

  std::pair<double, double> interval = cumul.findCenteredInterval(0.8);
  BOOST_CHECK_CLOSE(interval.first, 2., 0.0001);
  BOOST_CHECK_CLOSE(interval.second, 4., 0.0001);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
