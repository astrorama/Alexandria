/** 
 * @file PhzLikelihood/ModelScaleFunctor.h
 * @date May 24, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZLIKELIHOOD_MODELSCALEFUNCTOR_H
#define	PHZLIKELIHOOD_MODELSCALEFUNCTOR_H

#include "ChCatalog/SourceAttributes/Photometry.h"

namespace PhzLikelihood {

class ModelScaleFunctor {
  
public:
  
  ModelScaleFunctor() = default;
  
  virtual ~ModelScaleFunctor() = default;
  
  double operator()(const ChCatalog::Photometry& phot_obs, const ChCatalog::Photometry& phot_model) {
    double alpha_up {0};
    double alpha_down {0};
    auto obs_iter = phot_obs.begin();
    auto model_iter = phot_model.begin();
    while (obs_iter != phot_obs.end()) {
      alpha_up += ((*model_iter).flux * (*obs_iter).flux) / ((*obs_iter).error * (*obs_iter).error);
      alpha_down += ((*model_iter).flux * (*model_iter).flux) / ((*obs_iter).error * (*obs_iter).error);
      ++obs_iter;
      ++model_iter;
    }
    return alpha_up / alpha_down;
  }
  
};

} // end of namespace PhzLikelihood

#endif	/* PHZLIKELIHOOD_MODELSCALEFUNCTOR_H */

