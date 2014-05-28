/** 
 * @file ExtinctionFunctor.h
 * @date May 28, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZMODELING_EXTINCTIONFUNCTOR_H
#define	PHZMODELING_EXTINCTIONFUNCTOR_H

#include <memory>
#include "XYDataset/XYDataset.h"
#include "ChMath/function/Function.h"
#include "ChMath/interpolation/interpolation.h"

namespace PhzModeling {

class ExtinctionFunctor {
  
public:
  
  ExtinctionFunctor(const XYDataset::XYDataset& reddening_curve) {
    m_reddening_curve = ChMath::interpolate(reddening_curve, ChMath::InterpolationType::LINEAR);
  }
  
  ExtinctionFunctor(ExtinctionFunctor&&) = default;
  
  ExtinctionFunctor& operator=(ExtinctionFunctor&&) = default;
  
  virtual ~ExtinctionFunctor() = default;
  
  std::unique_ptr<XYDataset::XYDataset> operator()(const XYDataset::XYDataset& sed, double ebv) const {
    std::vector<std::pair<double, double>> reddened_values {};
    for (auto& sed_pair : sed) {
      double exponent = -0.4 * (*m_reddening_curve)(sed_pair.first) * ebv;
      double reddened_value = sed_pair.second * std::pow(10, exponent);
      reddened_values.push_back(std::make_pair(sed_pair.first, reddened_value));
    }
    return std::unique_ptr<XYDataset::XYDataset> {new XYDataset::XYDataset {std::move(reddened_values)}};
  }
  
private:
  
  std::unique_ptr<ChMath::Function> m_reddening_curve;
  
};

} // end of namespace PhzModeling

#endif	/* PHZMODELING_EXTINCTIONFUNCTOR_H */

