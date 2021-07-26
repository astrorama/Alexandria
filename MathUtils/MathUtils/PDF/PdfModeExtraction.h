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
 * @file MathUtils/PDF/PdfModeExtraction.h
 * @date 01/22/18
 * @author fdubath
 */

#ifndef _MATHUTILS_PDF_PDFMODEEXTRACTION_H
#define _MATHUTILS_PDF_PDFMODEEXTRACTION_H

#include "XYDataset/XYDataset.h"
#include <cstddef>
#include <tuple>
#include <utility>
#include <vector>

namespace Euclid {
namespace MathUtils {
/**
 * @Class ModeInfo
 *
 * @brief Class for storing the information of a PDF mode
 *
 * @details
 * The Mode info contains the mode area and the mode location. The mode location
 * is stored as the highest point in the PDF sampling, the mean
 * over the mode and a quadratic fitting around the highest point.
 */
class ModeInfo {
public:
  ModeInfo(double highest_sample, double mean, double interpolated, double area)
      : m_sample{highest_sample}, m_mean{mean}, m_interp{interpolated}, m_area{area} {}

  double getHighestSamplePosition() const {
    return m_sample;
  }

  double getMeanPosition() const {
    return m_mean;
  }

  double getInterpolatedMaxPosition() const {
    return m_interp;
  }

  double getModeArea() const {
    return m_area;
  }

private:
  double m_sample;
  double m_mean;
  double m_interp;
  double m_area;
};

/**
 * Extract the n highest modes in the provided pdf and compute for each of them
 * the location of the mode and its area.
 * A mode is discovered as the highest
 * point of the pdf, then, on both sides, samples are added until the pdf
 * starts to rise again. In order to avoid truncating the mode due to a noisy
 * pdf it is possible to specify a merge_ratio. In this case the samples are
 * added until their values is below the hight of the peak times the merge ratio,
 * then additional point are added until the pdf rise again.
 *
 * @param pdf The sampling of the pdf to be analysed.
 * @param merge_ratio The parameter for mode cutting.
 * @param n The (maximum) number of modes to be returned.
 * @return A vector of ModeInfo containing the position and the area of the modes.
 */
std::vector<ModeInfo> extractNHighestModes(const XYDataset::XYDataset& pdf, double merge_ratio, size_t n);

/**
 * Extract the n highest modes in the provided pdf and compute for each of them
 * the location of the mode and its area.
 * A mode is discovered as the highest
 * point of the pdf, then, on both sides, samples are added until the pdf
 * starts to rise again. In order to avoid truncating the mode due to a noisy
 * pdf it is possible to specify a merge_ratio. In this case the samples are
 * added until their values is below the hight of the peak times the merge ratio,
 * then additional point are added until the pdf rise again.
 *
 * @param x_sampling The horizontal sampling of the pdf to be analysed.
 * @param pdf_sampling The sampling of the pdf to be analysed.
 * @param merge_ratio The parameter for mode cutting.
 * @param n The (maximum) number of modes to be returned.
 * @return A vector of ModeInfo containing the position and the area of the modes.
 */
std::vector<ModeInfo> extractNHighestModes(std::vector<double>& x_sampling, std::vector<double>& pdf_sampling,
                                           double merge_ratio, size_t n);

/**
 * Extract the n modes with biggest area in the provided pdf and compute for
 * each of them the location of the mode and its area.
 * A mode is discovered as the highest
 * point of the pdf, then, on both sides, samples are added until the pdf
 * starts to rise again. In order to avoid truncating the mode due to a noisy
 * pdf it is possible to specify a merge_ratio. In this case the samples are
 * added until their values is below the hight of the peak times the merge ratio,
 * then additional point are added until the pdf rise again.
 *
 * @param pdf The sampling of the pdf to be analysed.
 * @param merge_ratio The parameter for mode cutting.
 * @param n The (maximum) number of modes to be returned.
 * @return A vector of ModeInfo containing the position and the area of the modes.
 */
std::vector<ModeInfo> extractNBigestModes(const XYDataset::XYDataset& pdf, double merge_ratio, size_t n);

/**
 * Extract the n modes with biggest area in the provided pdf and compute for
 * each of them the location of the mode and its area.
 * A mode is discovered as the highest
 * point of the pdf, then, on both sides, samples are added until the pdf
 * starts to rise again. In order to avoid truncating the mode due to a noisy
 * pdf it is possible to specify a merge_ratio. In this case the samples are
 * added until their values is below the hight of the peak times the merge ratio,
 * then additional point are added until the pdf rise again.
 *
 * @param x_sampling The horizontal sampling of the pdf to be analysed.
 * @param pdf_sampling The sampling of the pdf to be analysed.
 * @param merge_ratio The parameter for mode cutting.
 * @param n The (maximum) number of modes to be returned.
 * @return A vector of ModeInfo containing the position and the area of the modes.
 */
std::vector<ModeInfo> extractNBigestModes(std::vector<double>& x_sampling, std::vector<double>& pdf_sampling,
                                          double merge_ratio, size_t n);

} /* namespace MathUtils */
}  // namespace Euclid

#endif
