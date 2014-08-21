/** 
 * @file ModelDatasetGenerator.h
 * @date August 10, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZMODELING_MODELDATASETGENERATOR_H
#define	PHZMODELING_MODELDATASETGENERATOR_H

#include "XYDataset/XYDataset.h"
#include "PhzDataModel/PhzModel.h"
#include "PhzModeling/ExtinctionFunctor.h"

namespace PhzModeling {

class ModelDatasetGenerator {
  
public:
  
  ModelDatasetGenerator(const PhzDataModel::ModelAxesTuple& axes_tuple,
                        const std::vector<std::unique_ptr<XYDataset::XYDataset>>& sed_data_vector,
                        const std::vector<ExtinctionFunctor>& reddening_curve_functor_vector,
                        size_t current_index)
      : m_index_helper{Grid::makeGridIndexHelper(axes_tuple)}, m_axes_tuple(axes_tuple), m_current_index{current_index},
        m_size{m_index_helper.m_axes_index_factors.back()}, m_sed_data_vector(sed_data_vector),
        m_reddening_curve_functor_vector(reddening_curve_functor_vector) { }
       
  ModelDatasetGenerator(const ModelDatasetGenerator& other) 
      : m_index_helper{Grid::makeGridIndexHelper(other.m_axes_tuple)}, m_axes_tuple(other.m_axes_tuple), m_current_index{other.m_current_index},
        m_size{other.m_size}, m_sed_data_vector(other.m_sed_data_vector),
        m_reddening_curve_functor_vector(other.m_reddening_curve_functor_vector) { }
  
  ModelDatasetGenerator& operator=(const ModelDatasetGenerator& other) {
    m_current_index = other.m_current_index;
    m_current_reddened_sed.reset();
    return *this;
  }
  
  ModelDatasetGenerator& operator=(size_t other) {
    m_current_index = other;
    m_current_reddened_sed.reset();
    return *this;
  }
  
  ModelDatasetGenerator& operator++() {
    if (m_current_index < m_size) {
      ++m_current_index;
    }
    return *this;
  }
  
  ModelDatasetGenerator& operator+=(int n) {
    m_current_index += n;
    if (m_current_index > m_size) {
      m_current_index = m_size;
    }
    return *this;
  }
  
  int operator-(size_t other) const {
    return m_current_index - other;
  }
  
  int operator-(const ModelDatasetGenerator& other) const {
    return m_current_index - other.m_current_index;
  }
  
  bool operator==(size_t other) const {
    return m_current_index == other;
  }
  
  bool operator==(const ModelDatasetGenerator& other) const {
    return m_current_index == other.m_current_index;
  }
  
  bool operator!=(size_t other) const {
    return m_current_index != other;
  }
  
  bool operator!=(const ModelDatasetGenerator& other) const {
    return m_current_index != other.m_current_index;
  }
  
  bool operator>(size_t other) const {
    return m_current_index > other;
  }
  
  bool operator>(const ModelDatasetGenerator& other) const {
    return m_current_index > other.m_current_index;
  }
  
  bool operator<(size_t other) const {
    return m_current_index < other;
  }
  
  bool operator<(const ModelDatasetGenerator& other) const {
    return m_current_index < other.m_current_index;
  }
  
  XYDataset::XYDataset& operator*() {
    // We calculate the parameter indices for the current index
    size_t new_sed_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::SED, m_current_index);
    size_t new_reddening_curve_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::REDDENING_CURVE, m_current_index);
    size_t new_ebv_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::EBV, m_current_index);
    size_t new_z_index = m_index_helper.axisIndex(PhzDataModel::ModelParameter::Z, m_current_index);
    // We check if we need to recalculate the reddened SED
    if (new_sed_index != m_current_sed_index || new_reddening_curve_index != m_current_reddening_curve_index
        || new_ebv_index != m_current_ebv_index || !m_current_reddened_sed) {
      const ExtinctionFunctor& extinction_functor = m_reddening_curve_functor_vector[new_reddening_curve_index];
      double ebv = std::get<PhzDataModel::ModelParameter::EBV>(m_axes_tuple)[new_ebv_index];
      m_current_reddened_sed = extinction_functor(*m_sed_data_vector[new_sed_index], ebv);
    }
    if (new_sed_index != m_current_sed_index || new_reddening_curve_index != m_current_reddening_curve_index
        || new_ebv_index != m_current_ebv_index || new_z_index != m_current_z_index || !m_current_redshifted_sed) {
      double z = std::get<PhzDataModel::ModelParameter::Z>(m_axes_tuple)[new_z_index];
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
  
  // An object to convert the parameter space coordinates to a long index and vice versa
  decltype(Grid::makeGridIndexHelper(std::declval<PhzDataModel::ModelAxesTuple>())) m_index_helper;
  const PhzDataModel::ModelAxesTuple& m_axes_tuple;
  
  // The current long 1D index
  size_t m_current_index;
  size_t m_size;
  
  // The indices of the parameters last calculated
  size_t m_current_sed_index {0};
  size_t m_current_reddening_curve_index {0};
  size_t m_current_ebv_index {0};
  size_t m_current_z_index {0};
  
  // The latest calculated reddened and redshifted SEDs
  std::unique_ptr<XYDataset::XYDataset> m_current_reddened_sed;
  std::unique_ptr<XYDataset::XYDataset> m_current_redshifted_sed;
  
  // vector with the SED datasets the generator uses
  const std::vector<std::unique_ptr<XYDataset::XYDataset>>& m_sed_data_vector;
  
  // vector with the reddening curves the generator uses
  const std::vector<ExtinctionFunctor>& m_reddening_curve_functor_vector;
  
}; // End of ModelDatasetGenerator class

} // end of namespace PhzModeling

#endif	/* PHZMODELING_MODELDATASETGENERATOR_H */

