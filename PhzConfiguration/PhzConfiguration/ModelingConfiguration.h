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

#include "ElementsKernel/Export.h"

#include "XYDataset/XYDatasetProvider.h"
#include "XYDataset/QualifiedName.h"

namespace Euclid {
namespace PhzConfiguration {

class ELEMENTS_API ModelingConfiguration {

public:

  typedef boost::program_options::variable_value option_type;

  ModelingConfiguration(std::map<std::string, option_type> options);

  virtual ~ModelingConfiguration() = default;

  std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> sedDatasetProvider();

  std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> reddeningCurveDatasetProvider();

  std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> filterDatasetProvider();

  std::vector<Euclid::XYDataset::QualifiedName> sedList();

  std::vector<Euclid::XYDataset::QualifiedName> reddeningCurveList();

  std::vector<Euclid::XYDataset::QualifiedName> filterList();

  std::vector<double> zList();

  std::vector<double> ebvList();

private:

  std::map<std::string, option_type> m_options;

}; // end of class ModelingConfiguration

} // end of namespace PhzConfiguration
} // end of namespace Euclid

#endif	/* PHZCONFIGURATION_MODELINGCONFIGURATION_H */

