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
 * @file FunctionUtils/Cumulative.h
 * @date 01/11/18
 * @author fdubath
 */

#ifndef _FUNCTIONUTILS_CUMULATIVE_H
#define _FUNCTIONUTILS_CUMULATIVE_H

#include <vector>
#include <utility>
#include "XYDataset/XYDataset.h"

namespace Euclid {
namespace MathUtils {

/**
 * @class Cumulative
 *
 * @brief Class for build cumulative from PDF and extract feature out of it.
 *
 */
class Cumulative {

public:
/**
 * @enum TrayPosition
 *
 * @brief when looking for the position having a given value, one may encounter
 * tray where the value is constant on an interval. This enum allow to specify
 * if one want an extremity or the middle of the tray.
 */
  enum TrayPosition { begin, middle, end };

  /**
  * @brief move constructor
  */
  Cumulative ( Cumulative && other);

  /**
  * @brief move assignation operator
  */
  Cumulative & operator = ( Cumulative && other);

  /**
  * @brief copy constructor
  */
  Cumulative(const Cumulative & other);

  /**
  * @brief copy assignation operator
  */
  Cumulative & operator = ( const Cumulative & other);

  /**
  * @brief Constructor from the sampling of a cumulative
  *
  * @param x_sampling horizontal sampling.
  * @param y_sampling vertical sampling.
  * @throw Exception if the 2 axis have not the same length
  */
  Cumulative(std::vector<double>& x_sampling, std::vector<double>& y_sampling);

  /**
  * @brief Constructor from the sampling of a cumulative
  *
  * @param sampling cumulative sampling.
  */
  explicit Cumulative(const XYDataset::XYDataset & sampling);

  /**
  * @brief Factory from the sampling of a PDF. The Cumulative vertical samples
  * are build as the sum of the the pdf vertical sample with horizontal value
  * smaller or equal to the cumulative horizontal value
  *
  * @param x_sampling pdf horizontal sampling.
  * @param y_sampling pdf vertical sampling.
  * @throw Exception if the 2 axis have not the same length
  */
  static Cumulative fromPdf(std::vector<double>& x_sampling, std::vector<double>& pdf_sampling);

  /**
  * @brief Factory from the sampling of a PDF. The Cumulative vertical samples
  * are build as the sum of the the pdf vertical sample with horizontal value
  * smaller or equal to the cumulative horizontal value
  *
  * @param sampling pdf sampling.
  */
  static Cumulative fromPdf(const XYDataset::XYDataset &  sampling);

  /**
  * @brief Normalize the Cumulative. After calling this function the last vertical value is 1.0.
  */
  void normalize();

  /**
  * @brief Find the first horizontal sample which vertical value is bigger or equal to the ratio value.
  * If the Cumulative is not normalize the searched value is the last vertical value of the Cumulative time the ratio.
  * If the selected sample is part of a tray (next sample(s) have the same vertical value),
  * the position param allow to specify if the first, the last or the average of the point with the same value
  * has to be returned
  *
  *
  * @param ratio The value to be searched,
  * @param position Selection of the returned value in case of tray,
  * @return the horizontal value for which the Cumulative has the vertical value ratio.
  */
  double findValue(double ratio, TrayPosition position=TrayPosition::middle) const;

  /**
  * @brief Scan the horizontal axis looking for the smallest x-interval for which
  * the vertical interval is at least rate*Last Value of the Cumulative.
  *
  * @param rate Vertical interval,
  * @return a pair of number the first is the horizontal value of the begining of the interval, the second the end.
  */
  std::pair<double,double> findMinInterval(double rate) const;

  /**
  * @brief return the horizontal interval starting where the Cumulative has value
  * (1-ratio)/2 and ending where the Cumulative has value (1+ratio)/2.
  * If the Cumulative is not normalized the searched value are multiplied by the
  * last cumulative vertical value.
  *
  * @param rate Vertical interval,
  * @return a pair of number the first is the horizontal value of the begining of the interval, the second the end.
  */
  std::pair<double,double> findCenteredInterval(double rate) const;

  /**
   * @brief Destructor
   */
  virtual ~Cumulative() = default;


private:
  std::vector<double> m_x_sampling;
  std::vector<double> m_y_sampling;


}; /* End of Cumulative class */

} /* namespace MathUtils */
}

#endif
