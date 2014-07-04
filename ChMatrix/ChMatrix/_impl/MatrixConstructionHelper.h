/** 
 * @file ChMatrix/_impl/MatrixConstructionHelper.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_MATRIXCONSTRUCTIONHELPER_H
#define	CHMATRIX_MATRIXCONSTRUCTIONHELPER_H

#include <vector>
#include <tuple>
#include "ChMatrix/AxisInfo.h"
#include "TemplateLoopCounter.h"

namespace ChMatrix {

/**
 * @class MatrixConstructionHelper
 * 
 * @brief Matrix construction helper class
 * 
 * @brief
 * The MatrixConstructionHelper is a helper class, which provides functions
 * which use iteration over variadic templates to construct some collections
 * required during the construction of the Matrix class. It is meant to be
 * used by the Matrix constructor. For a helper class with similar behavior
 * to be used outside the Matrix class see the MatrixIndexHelper class.
 * 
 * @tparam Axes the types of the axes
 */
template<typename... Axes>
class MatrixConstructionHelper {
public:
  
  /**
   * @brief
   * Creates a vector which contains the sizes of the given axes
   * @details
   * Note that this method is using variadic template iteration by using the
   * second parameter (TemplateLoopCounter). To initiate the iteration the
   * counter must be equal with the number of axes in the tuple.
   * 
   * @tparam I the index of the axis until which the results are calculated 
   * @param axes A tuple containing the AxisInfo objects describing the axes
   * @return A vector containing the sizes of the axes
   */
  template<int I>
  static std::vector<size_t> createAxesSizesVector(const std::tuple<AxisInfo<Axes>...>& axes,
                                                     const TemplateLoopCounter<I>&) {
    std::vector<size_t> result {createAxesSizesVector(axes, TemplateLoopCounter<I-1>{})};
    result.push_back(std::get<I-1>(axes).size());
    return result;
  }

  /// Method which terminates the iteration when creating the axes sizes vector
  static std::vector<size_t> createAxesSizesVector(const std::tuple<AxisInfo<Axes>...>&,
                                                     const TemplateLoopCounter<0>&) {
    return std::vector<size_t>{};
  }
  
  /**
   * @brief
   * Returns the index factor of an axis
   * @details
   * The index factor of an axis is the step needed to be done in the single
   * dimensional array to move to the next element of the axis. It is equal
   * to the multiplication of the sizes of all the axes which have faster
   * iteration rate. Its purpose is to facilitate the conversion of multi-
   * dimensional coordinates to the index of a long array.
   * 
   * @tparam I the index of the axis to get the factor for
   * @param axes The axes to use for the calculation
   * @return The index factor of the Ith axis
   */
  template<int I>
  static size_t getAxisIndexFactor(const std::tuple<AxisInfo<Axes>...>& axes,
                                    const TemplateLoopCounter<I>&) {
    return std::get<I>(axes).size() * getAxisIndexFactor(axes, TemplateLoopCounter<I-1>{});
  }
  
  /// Method which terminates the iteration when calculating the axis index factors
  static size_t getAxisIndexFactor(const std::tuple<AxisInfo<Axes>...>&,
                                    const TemplateLoopCounter<-1>&) {
    return 1;
  }
  
  /**
   * @brief
   * Creates a vector which contains the index factors of the given axes
   * @details
   * For an explanation of the index factor see the documentation of the
   * getAxisIndexFactor method. The returned vector has size one bigger than
   * the number of axes. The last element contains the total size of the
   * required single dimensional array to keep the data.
   * Note that this method is using variadic template iteration by using the
   * second parameter (TemplateLoopCounter). To initiate the iteration the
   * counter must be equal with the number of axes in the tuple.
   * 
   * @tparam I the index of the axis until which the results are calculated 
   * @param axes A tuple containing the AxisInfo objects describing the axes
   * @return A vector containing the index factors of the axes
   */
  template<int I>
  static std::vector<size_t> createAxisIndexFactorVector(
            const std::tuple<AxisInfo<Axes>...>& axes,const TemplateLoopCounter<I>&) {
    std::vector<size_t> result {createAxisIndexFactorVector(axes, TemplateLoopCounter<I-1>{})};
    result.push_back(getAxisIndexFactor(axes, TemplateLoopCounter<I-1>{}));
    return result;
  }
  
  /// Method which terminates the iteration when creating the axes index factors
  static std::vector<size_t> createAxisIndexFactorVector(
            const std::tuple<AxisInfo<Axes>...>&,const TemplateLoopCounter<0>&) {
    return std::vector<size_t> {1};
  }
};

} // end of namespace ChMatrix

#endif	/* CHMATRIX_MATRIXCONSTRUCTIONHELPER_H */

