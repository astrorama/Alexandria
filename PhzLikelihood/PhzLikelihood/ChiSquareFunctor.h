/** 
 * @file ChiSquareFunctor.h
 * @date May 24, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZLIKELIHOOD_CHISQUAREFUNCTOR_H
#define	PHZLIKELIHOOD_CHISQUAREFUNCTOR_H

namespace PhzLikelihood {

class ChiSquareFunctor {
  
public:
  
  ChiSquareFunctor() = default;
  
  virtual ~ChiSquareFunctor() = default;
  
  double operator()(const ChCatalog::Photometry& phot_obs, const ChCatalog::Photometry& phot_model, double model_scale) {
    double chi_square {0};
    for (auto obs_iter=phot_obs.begin(); obs_iter!=phot_obs.end(); ++obs_iter) {
      auto model = phot_model.find(obs_iter.filterName());
      double model_flux = model->flux;
      double difference = model_scale * model_flux - (*obs_iter).flux;
      chi_square += difference * difference / ((*obs_iter).error * (*obs_iter).error);
    }
//    auto obs_iter = phot_obs.begin();
//    auto model_iter = phot_model.begin();
//    while (obs_iter != phot_obs.end()) {
//      double difference = model_scale * (*model_iter).flux - (*obs_iter).flux;
//      chi_square += difference * difference / ((*obs_iter).flux * (*obs_iter).flux);
//      ++obs_iter;
//      ++model_iter;
//    }
    return exp(-1 * chi_square / 2);
  }
  
};

} // end of namespace PhzLikelihood

#endif	/* PHZLIKELIHOOD_CHISQUAREFUNCTOR_H */

