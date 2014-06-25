/** 
 * @file PhzConfiguration/ModelingConfiguration.h
 * @date May 21, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZCONFIGURATION_MODELINGCONFIGURATION_H
#define	PHZCONFIGURATION_MODELINGCONFIGURATION_H

#include <memory>
#include <map>
#include <string>
#include <vector>
#include <boost/program_options.hpp>
#include "XYDataset/XYDatasetProvider.h"
#include "XYDataset/QualifiedName.h"

namespace PhzConfiguration {

class ModelingConfiguration {
  
public:
  
  typedef boost::program_options::variable_value option_type;
  
  ModelingConfiguration(std::map<std::string, option_type> options);
  
  virtual ~ModelingConfiguration() = default;
  
  std::unique_ptr<XYDataset::XYDatasetProvider> sedDatasetProvider();
  
  std::unique_ptr<XYDataset::XYDatasetProvider> reddeningCurveDatasetProvider();
  
  std::unique_ptr<XYDataset::XYDatasetProvider> filterDatasetProvider();
  
  std::vector<XYDataset::QualifiedName> sedList();
  
  std::vector<XYDataset::QualifiedName> reddeningCurveList();
  
  std::vector<XYDataset::QualifiedName> filterList();
  
  std::vector<double> zList();
  
  std::vector<double> ebvList();
  
private:
  
  std::map<std::string, option_type> m_options;
  
}; // end of class ModelingConfiguration

} // end of namespace PhzConfiguration

#endif	/* PHZCONFIGURATION_MODELINGCONFIGURATION_H */

