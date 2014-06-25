/** 
 * @file PhzModeling/ModelDataManager.h
 * @date May 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZMODELING_MODELDATAMANAGER_H
#define	PHZMODELING_MODELDATAMANAGER_H

#include <iterator>
#include <memory>
#include <vector>
#include <cmath>
#include <functional>
#include "ElementsKernel/ElementsException.h"
#include "ChMath/function/Function.h"
#include "ChMath/interpolation/interpolation.h"
#include "ChMatrix/MatrixIndexHelper.h"
#include "XYDataset/XYDatasetProvider.h"
#include "XYDataset/XYDataset.h"
#include "PhzDataModel/PhzModel.h"
#include "PhzModeling/ExtinctionFunctor.h"

namespace PhzModeling {

class ModelDataManager {
  
public:
  
//  typedef ChMath::Function data_type;
  typedef XYDataset::XYDataset data_type;
  
  class iterator : public std::iterator<std::random_access_iterator_tag, data_type> {
  public:
    iterator(ModelDataManager& owner, size_t current_index) : m_owner(owner), m_current_index{current_index} { }
    iterator(const iterator& other) : m_owner(other.m_owner), m_current_index{other.m_current_index} { }
    iterator& operator=(const iterator& other) {
      m_current_index = other.m_current_index;
      m_current_reddened_sed.reset();
      return *this;
    }
    iterator& operator++() {
      if (m_current_index < m_owner.m_size) {
        ++m_current_index;
      }
      return *this;
    }
    iterator& operator+=(int n) {
      m_current_index += n;
      if (m_current_index > m_owner.m_size) {
        m_current_index = m_owner.m_size;
      }
      return *this;
    }
    int operator-(const iterator& other) const {
      return m_current_index - other.m_current_index;
    }
    bool operator==(const iterator& other) const {
      return m_current_index == other.m_current_index;
    }
    bool operator!=(const iterator& other) const {
      return m_current_index != other.m_current_index;
    }
    bool operator>(const iterator& other) const {
      return m_current_index > other.m_current_index;
    }
    bool operator<(const iterator& other) const {
      return m_current_index < other.m_current_index;
    }
    data_type& operator*() {
      size_t new_sed_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::SED, m_current_index);
      size_t new_reddening_curve_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::REDDENING_CURVE, m_current_index);
      size_t new_ebv_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::EBV, m_current_index);
      size_t new_z_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::Z, m_current_index);
      if (new_sed_index != m_current_sed_index || new_reddening_curve_index != m_current_reddening_curve_index
          || new_ebv_index != m_current_ebv_index || !m_current_reddened_sed) {
        ExtinctionFunctor& extinction_functor = m_owner.m_reddening_curve_functor_vector[new_reddening_curve_index];
        double ebv = std::get<PhzDataModel::ModelParameter::EBV>(m_owner.m_axes_tuple)[new_ebv_index];
        m_current_reddened_sed = extinction_functor(*m_owner.m_sed_data_vector[new_sed_index], ebv);
      }
      if (new_sed_index != m_current_sed_index || new_reddening_curve_index != m_current_reddening_curve_index
          || new_ebv_index != m_current_ebv_index || new_z_index != m_current_z_index || !m_current_redshifted_sed) {
        double z = std::get<PhzDataModel::ModelParameter::Z>(m_owner.m_axes_tuple)[new_z_index];
        std::vector<std::pair<double, double>> new_redshifted_values {};
        for (auto& sed_pair : *m_current_reddened_sed) {
          new_redshifted_values.push_back(std::make_pair(sed_pair.first*(1+z),sed_pair.second/((1+z)*(1+z))));
        }
        m_current_redshifted_sed.reset(new XYDataset::XYDataset{new_redshifted_values});
      }
      m_current_sed_index = new_sed_index;
      m_current_reddening_curve_index = new_reddening_curve_index;
      m_current_ebv_index = new_ebv_index;
      m_current_z_index = new_z_index;
      return *m_current_redshifted_sed;
    }
  private:
    ModelDataManager& m_owner;
    size_t m_current_index;
    decltype(ChMatrix::makeMatrixIndexHelper(std::declval<PhzDataModel::ModelAxesTuple>()))
        m_index_helper = ChMatrix::makeMatrixIndexHelper(m_owner.m_axes_tuple);
    size_t m_current_sed_index {0};
    size_t m_current_reddening_curve_index {0};
    size_t m_current_ebv_index {0};
    size_t m_current_z_index {0};
    std::unique_ptr<XYDataset::XYDataset> m_current_reddened_sed;
    std::unique_ptr<XYDataset::XYDataset> m_current_redshifted_sed;
  }; // end of class iterator
  
  ModelDataManager(PhzDataModel::ModelAxesTuple axes_tuple,
                           std::unique_ptr<XYDataset::XYDatasetProvider> sed_provider,
                           std::unique_ptr<XYDataset::XYDatasetProvider> reddening_curve_provider)
              : m_axes_tuple{std::move(axes_tuple)} {
    // We calculate the total size based on the given tuple
    size_t z_size = std::get<PhzDataModel::ModelParameter::Z>(m_axes_tuple).size();
    size_t ebv_size = std::get<PhzDataModel::ModelParameter::EBV>(m_axes_tuple).size();
    size_t reddening_curve_size = std::get<PhzDataModel::ModelParameter::REDDENING_CURVE>(m_axes_tuple).size();
    size_t sed_size = std::get<PhzDataModel::ModelParameter::SED>(m_axes_tuple).size();
    m_size = z_size * ebv_size * reddening_curve_size * sed_size;
    
    // We locally load all the SED datasets for IO performance reasons
    for (auto& sed_name : std::get<PhzDataModel::ModelParameter::SED>(m_axes_tuple)) {
      auto sed_data = sed_provider->getDataset(sed_name);
      if (!sed_data) {
        throw ElementsException() << "SED with name " << sed_name.qualifiedName()
                                  << " does not exist";
      }
      m_sed_data_vector.push_back(std::move(sed_data));
    }
    
    // We locally load all the reddening curve datasets for IO performance reasons
    for (auto& reddening_curve_name : std::get<PhzDataModel::ModelParameter::REDDENING_CURVE>(m_axes_tuple)) {
      auto reddening_curve_data = reddening_curve_provider->getDataset(reddening_curve_name);
      if (!reddening_curve_data) {
        throw ElementsException() << "Reddening curve with name " << reddening_curve_name.qualifiedName()
                                  << " does not exist";
      }
      m_reddening_curve_functor_vector.emplace_back(*reddening_curve_data);
    }
  }
  
  size_t size() const {
    return m_size;
  }
  
  iterator begin() {
    return iterator(*this, 0);
  }
  
  iterator end() {
    return iterator(*this, m_size);
  }

private:
  
  PhzDataModel::ModelAxesTuple m_axes_tuple;
  size_t m_size;
  std::vector<std::unique_ptr<XYDataset::XYDataset>> m_sed_data_vector;
  std::vector<std::unique_ptr<ChMath::Function>> m_reddening_curve_function_vector;
  std::vector<ExtinctionFunctor> m_reddening_curve_functor_vector;
  
}; // end of class ModelFunctionDataManager

} // end of namespace PhzModeling

#endif	/* PHZMODELING_MODELDATAMANAGER_H */

