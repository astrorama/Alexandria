/** 
 * @file ModelDatasetGrid.h
 * @date August 10, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZMODELING_MODELDATASETGRID_H
#define	PHZMODELING_MODELDATASETGRID_H

#include "XYDataset/XYDataset.h"
#include "XYDataset/XYDatasetProvider.h"
#include "PhzDataModel/PhzModel.h"
#include "PhzModeling/ModelDatasetGenerator.h"

namespace Euclid {
namespace PhzModeling {
  
struct ModelDatasetCellManager {
  size_t m_size;
};

}
} // end of namespace Euclid

namespace Euclid {
namespace Grid {

template<>
struct GridCellManagerTraits<Euclid::PhzModeling::ModelDatasetCellManager> {
  typedef Euclid::XYDataset::XYDataset data_type;
  typedef Euclid::PhzModeling::ModelDatasetGenerator iterator;
  static std::unique_ptr<Euclid::PhzModeling::ModelDatasetCellManager> factory(size_t size) {
    return std::unique_ptr<Euclid::PhzModeling::ModelDatasetCellManager>{new Euclid::PhzModeling::ModelDatasetCellManager {size}};
  }
  static size_t begin(const Euclid::PhzModeling::ModelDatasetCellManager&) {
    return 0;
  }
  static size_t end(const Euclid::PhzModeling::ModelDatasetCellManager& manager) {
    return manager.m_size;
  }
};

}
} // end of namespace Euclid

namespace Euclid {
namespace PhzModeling {

class ModelDatasetGrid : public Euclid::PhzDataModel::PhzGrid<ModelDatasetCellManager> {
  
public:
  
//  class model_iterator;
  
  ModelDatasetGrid(Euclid::PhzDataModel::ModelAxesTuple axes_tuple, std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> sed_provider,
                   std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> reddening_curve_provider) : Euclid::PhzDataModel::PhzGrid<ModelDatasetCellManager>(axes_tuple) {
    // We calculate the total size based on the given tuple
    size_t z_size = std::get<Euclid::PhzDataModel::ModelParameter::Z>(m_axes_tuple).size();
    size_t ebv_size = std::get<Euclid::PhzDataModel::ModelParameter::EBV>(m_axes_tuple).size();
    size_t reddening_curve_size = std::get<Euclid::PhzDataModel::ModelParameter::REDDENING_CURVE>(m_axes_tuple).size();
    size_t sed_size = std::get<Euclid::PhzDataModel::ModelParameter::SED>(m_axes_tuple).size();
    m_size = z_size * ebv_size * reddening_curve_size * sed_size;
    
    // We locally load all the SED datasets for IO performance reasons
    for (auto& sed_name : std::get<Euclid::PhzDataModel::ModelParameter::SED>(m_axes_tuple)) {
      auto sed_data = sed_provider->getDataset(sed_name);
      if (!sed_data) {
        throw Elements::Exception() << "SED with name " << sed_name.qualifiedName()
                                  << " does not exist";
      }
      m_sed_data_vector.push_back(std::move(sed_data));
    } 
    
    // We locally load all the reddening curve datasets for IO performance reasons
    for (auto& reddening_curve_name : std::get<Euclid::PhzDataModel::ModelParameter::REDDENING_CURVE>(m_axes_tuple)) {
      auto reddening_curve_data = reddening_curve_provider->getDataset(reddening_curve_name);
      if (!reddening_curve_data) {
        throw Elements::Exception() << "Reddening curve with name " << reddening_curve_name.qualifiedName()
                                  << " does not exist";
      }
      m_reddening_curve_functor_vector.emplace_back(*reddening_curve_data);
    }       
  }

  Euclid::PhzDataModel::PhzGrid<ModelDatasetCellManager>::iterator begin() {
    return Euclid::PhzDataModel::PhzGrid<ModelDatasetCellManager>::iterator{*this, ModelDatasetGenerator{m_axes_tuple, m_sed_data_vector, m_reddening_curve_functor_vector, 0}};
  }

  Euclid::PhzDataModel::PhzGrid<ModelDatasetCellManager>::iterator end() {
    return Euclid::PhzDataModel::PhzGrid<ModelDatasetCellManager>::iterator{*this, ModelDatasetGenerator{m_axes_tuple, m_sed_data_vector, m_reddening_curve_functor_vector, m_size}};
  }
  
private:
  
  Euclid::PhzDataModel::ModelAxesTuple m_axes_tuple {getAxesTuple()};
  size_t m_size;
  std::vector<std::unique_ptr<Euclid::XYDataset::XYDataset>> m_sed_data_vector;
  std::vector<ExtinctionFunctor> m_reddening_curve_functor_vector;
  
};

} // end of namespace PhzModeling
} // end of namespace Euclid

#endif	/* PHZMODELING_MODELDATASETGRID_H */

