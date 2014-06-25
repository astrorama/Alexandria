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

template<typename... Axes>
class MatrixConstructionHelper {
public:
  
  // The createAxesSizesVector functions implement a variadic template loop which
  // produces a vector containing all the axes sizes.
  template<int I>
  static std::vector<size_t> createAxesSizesVector(const std::tuple<AxisInfo<Axes>...>& axes,
                                                     const TemplateLoopCounter<I>&) {
    std::vector<size_t> result {createAxesSizesVector(axes, TemplateLoopCounter<I-1>{})};
    result.push_back(std::get<I-1>(axes).size());
    return result;
  }

  static std::vector<size_t> createAxesSizesVector(const std::tuple<AxisInfo<Axes>...>&,
                                                     const TemplateLoopCounter<0>&) {
    return std::vector<size_t>{};
  }
  
  // The getAxisIndexFactor methods implement a variadic template loop which
  // calculates the factor which which the index of an
  // axis must be multiplied when calculating the index of the data vector
  template<int I>
  static size_t getAxisIndexFactor(const std::tuple<AxisInfo<Axes>...>& axes,
                                    const TemplateLoopCounter<I>&) {
    return std::get<I>(axes).size() * getAxisIndexFactor(axes, TemplateLoopCounter<I-1>{});
  }
  
  static size_t getAxisIndexFactor(const std::tuple<AxisInfo<Axes>...>&,
                                    const TemplateLoopCounter<-1>&) {
    return 1;
  }
  
  // The createAxisIndexFactorVector methods implement a variadic template loop
  // which produces a vector containing the axis index factors (see getAxisIndexFactor)
  template<int I>
  static std::vector<size_t> createAxisIndexFactorVector(
            const std::tuple<AxisInfo<Axes>...>& axes,const TemplateLoopCounter<I>&) {
    std::vector<size_t> result {createAxisIndexFactorVector(axes, TemplateLoopCounter<I-1>{})};
    result.push_back(getAxisIndexFactor(axes, TemplateLoopCounter<I-1>{}));
    return result;
  }
  
  static std::vector<size_t> createAxisIndexFactorVector(
            const std::tuple<AxisInfo<Axes>...>&,const TemplateLoopCounter<0>&) {
    return std::vector<size_t> {1};
  }
};

} // end of namespace ChMatrix

#endif	/* CHMATRIX_MATRIXCONSTRUCTIONHELPER_H */

