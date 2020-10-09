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
 * @file src/lib/PDF/PdfModeExtraction.cpp
 * @date 01/22/18
 * @author fdubath
 */

#include "MathUtils/PDF/PdfModeExtraction.h"
#include "ElementsKernel/Exception.h"
#include <cstddef>
#include <iterator>
#include <tuple>
#include <utility>
#include <vector>

namespace Euclid {
namespace MathUtils {

std::pair<std::vector<double>, std::vector<double>> getXYs(const XYDataset::XYDataset& pdf) {
  std::vector<double> xs{};
  std::vector<double> ys{};

  auto iter = pdf.begin();
  while (iter != pdf.end()) {
    xs.push_back((*iter).first);
    ys.push_back((*iter).second);
    ++iter;
  }

  return std::make_pair(xs, ys);
}

size_t findMaximumIndex(const std::vector<double>& pdf) {
  double max       = -1;
  size_t index     = 0;
  size_t max_index = 0;
  for (auto iter = pdf.begin(); iter != pdf.end(); ++iter) {
    if (*iter > max) {
      max       = *iter;
      max_index = index;
    }
    ++index;
  }

  return max_index;
}

std::pair<size_t, size_t> catchPeak(const std::vector<double>& pdf, size_t center_index, double merge_ratio) {

  double peak_value = pdf[center_index];
  double threshold  = (1.0 - merge_ratio) * peak_value;
  size_t min_x      = 0;
  size_t max_x      = pdf.size() - 1;

  for (size_t index = 0; index <= center_index; ++index) {
    size_t position = center_index - index;
    if (position == 0 || pdf[position] == 0) {
      break;
    }
    if ((pdf[position] < threshold && pdf[position - 1] >= pdf[position])) {
      min_x = position;
      break;
    }
    min_x = position;
  }

  for (size_t position = center_index; position <= pdf.size(); ++position) {
    if (position == pdf.size() - 1 || pdf[position] == 0) {
      break;
    }
    if ((pdf[position] < threshold && pdf[position + 1] >= pdf[position])) {
      max_x = position;
      break;
    }
    max_x = position;
  }

  return std::make_pair(min_x, max_x);
}

// basic integration may be refined
std::pair<double, double> avgArea(std::pair<std::vector<double>, std::vector<double>>& pdf, size_t min_x, size_t max_x) {

  double num  = 0.;
  double area = 0.;
  for (size_t index = min_x; index <= max_x; ++index) {
    double dx = 0.;
    if (index == 0) {
      dx = pdf.first[index + 1] - pdf.first[index];
    } else if (index == pdf.first.size() - 1) {
      dx = pdf.first[index] - pdf.first[index - 1];
    } else {
      dx = (pdf.first[index + 1] - pdf.first[index - 1]) / 2.0;
    }

    num += pdf.first[index] * pdf.second[index] * dx;
    area += pdf.second[index] * dx;
  }

  return std::make_pair(num / area, area);
}

double getInterpolationAround(const std::pair<std::vector<double>, std::vector<double>>& pdf, size_t x_index) {
  /*
  without assuming equi-distant sampling

  x_max= ((x1^2-x0^2)*y2 - (x2^2-x0^2)*y1+(x2^2-x1^2)*y0)/(2*((x1-x0)*y2-(x2-x0)*y1+(x2-x1)*y0))

  */
  if (x_index >= pdf.first.size()) {
    throw Elements::Exception("getInterpolationAround: x_index out of range.");
  }

  // ensure we are not on the border
  if (x_index == 0) {
    x_index += 1;
  } else if (x_index + 1 == pdf.first.size()) {
    x_index -= 1;
  }

  double x0 = pdf.first[x_index - 1];
  double y0 = pdf.second[x_index - 1];

  double x1 = pdf.first[x_index];
  double y1 = pdf.second[x_index];

  double x2 = pdf.first[x_index + 1];
  double y2 = pdf.second[x_index + 1];

  double denom = 2 * ((x1 - x0) * y2 - (x2 - x0) * y1 + (x2 - x1) * y0);
  double num   = (x1 * x1 - x0 * x0) * y2 - (x2 * x2 - x0 * x0) * y1 + (x2 * x2 - x1 * x1) * y0;

  double x_max = x1;
  // protect against division by 0 (flat interval)
  if (denom != 0) {
    x_max = num / denom;
  }

  // check in interval
  if (x_max < pdf.first.front()) {
    x_max = pdf.first.front();
  } else if (x_max > pdf.first.back()) {
    x_max = pdf.first.back();
  }

  return x_max;
}

std::pair<std::vector<double>, std::vector<double>> flatternPeak(const std::pair<std::vector<double>, std::vector<double>>& pdf,
                                                                 size_t min_x, size_t max_x, double value) {
  std::vector<double> flatterned{pdf.second};
  for (size_t index = min_x; index <= max_x; ++index) {
    flatterned[index] = value;
  }
  return std::make_pair(pdf.first, flatterned);
}

std::vector<ModeInfo> extractNHighestModes(std::vector<double>& x_sampling, std::vector<double>& pdf_sampling, double merge_ratio,
                                           size_t n) {
  std::vector<ModeInfo> result{};
  auto                  pdf_xy = std::make_pair(x_sampling, pdf_sampling);

  for (size_t idx = 0; idx < n; ++idx) {
    auto peak_index = findMaximumIndex(pdf_xy.second);
    auto min_max    = catchPeak(pdf_xy.second, peak_index, merge_ratio);
    auto mean_area  = avgArea(pdf_xy, min_max.first, min_max.second);
    auto max_inter  = getInterpolationAround(pdf_xy, peak_index);

    result.push_back(ModeInfo(pdf_xy.first[peak_index], mean_area.first, max_inter, mean_area.second));
    pdf_xy = flatternPeak(pdf_xy, min_max.first, min_max.second, 0.0);
  }
  return result;
}

std::vector<ModeInfo> extractNHighestModes(const XYDataset::XYDataset& pdf, double merge_ratio, size_t n) {
  auto pdf_xy = getXYs(pdf);
  return extractNHighestModes(pdf_xy.first, pdf_xy.second, merge_ratio, n);
}

std::vector<ModeInfo> extractNBigestModes(std::vector<double>& x_sampling, std::vector<double>& pdf_sampling, double merge_ratio,
                                          size_t n) {
  auto   pdf_xy     = std::make_pair(x_sampling, pdf_sampling);
  double total_area = avgArea(pdf_xy, 0, x_sampling.size() - 1).second;

  std::vector<ModeInfo> result{};

  bool   out  = false;
  size_t loop = 0;
  while (!out) {

    auto   peak_index       = findMaximumIndex(pdf_xy.second);
    auto   min_max          = catchPeak(pdf_xy.second, peak_index, merge_ratio);
    auto   mean_area        = avgArea(pdf_xy, min_max.first, min_max.second);
    auto   max_sample       = pdf_xy.first[peak_index];
    double interp_max_value = getInterpolationAround(pdf_xy, peak_index);
    auto   new_mode         = ModeInfo(max_sample, mean_area.first, interp_max_value, mean_area.second);

    auto iter_mode = result.begin();
    while (iter_mode != result.end()) {
      if ((*iter_mode).getModeArea() < mean_area.second) {
        break;
      }
      ++iter_mode;
    }

    if (iter_mode != result.end()) {
      result.insert(iter_mode, new_mode);
    } else if (result.size() < n) {
      result.push_back(new_mode);
    }
    total_area -= mean_area.second;
    out = result.size() >= n && (result.back().getModeArea() > total_area || loop > 3 * n);

    pdf_xy = flatternPeak(pdf_xy, min_max.first, min_max.second, 0.0);
    ++loop;
  }

  return result;
}

std::vector<ModeInfo> extractNBigestModes(const XYDataset::XYDataset& pdf, double merge_ratio, size_t n) {
  auto pdf_xy = getXYs(pdf);
  return extractNBigestModes(pdf_xy.first, pdf_xy.second, merge_ratio, n);
}

}  // namespace MathUtils
}  // namespace Euclid
