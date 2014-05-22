/** 
 * @file ModelingConfiguration.cpp
 * @date May 21, 2014
 * @author Nikolaos Apostolakos
 */

#include <set>
#include "ElementsKernel/ElementsException.h"
#include "ElementsKernel/ElementsLogging.h"
#include "XYDataset/FileParser.h"
#include "XYDataset/AsciiParser.h"
#include "XYDataset/FileSystemProvider.h"
#include "PhzConfiguration/ModelingConfiguration.h"

namespace PhzConfiguration {

ElementsLogging logger = ElementsLogging::getLogger("ModelingConfiguration");

ModelingConfiguration::ModelingConfiguration(std::map<std::string, option_type> options)
          : m_options{std::move(options)} { }

std::unique_ptr<XYDataset::XYDatasetProvider> ModelingConfiguration::sedDatasetProvider() {
  if (!m_options["sed-root-path"].empty()) {
    std::string path = m_options["sed-root-path"].as<std::string>();
    logger.info() << "Using SED root directory " << path;
    logger.info() << "Assuming SED files are ASCII files";
    std::unique_ptr<XYDataset::FileParser> file_parser {new XYDataset::AsciiParser{}};
    return std::unique_ptr<XYDataset::XYDatasetProvider> {
      new XYDataset::FileSystemProvider{path, std::move(file_parser)}
    };
  }
  logger.error() << "The option 'sed-root-path' is not set";
  throw ElementsException {"Missing or unknown SED dataset provider options"};
}

std::unique_ptr<XYDataset::XYDatasetProvider> ModelingConfiguration::reddeningCurveDatasetProvider() {
  if (!m_options["reddening-curve-root-path"].empty()) {
    std::string path = m_options["reddening-curve-root-path"].as<std::string>();
    logger.info() << "Using Reddening Curve root directory " << path;
    logger.info() << "Assuming Reddening Curve files are ASCII files";
    std::unique_ptr<XYDataset::FileParser> file_parser {new XYDataset::AsciiParser{}};
    return std::unique_ptr<XYDataset::XYDatasetProvider> {
      new XYDataset::FileSystemProvider{path, std::move(file_parser)}
    };
  }
  logger.error() << "The option 'reddening-curve-root-path' is not set";
  throw ElementsException {"Missing or unknown Reddening Curve dataset provider options"};
}

std::unique_ptr<XYDataset::XYDatasetProvider> ModelingConfiguration::filterDatasetProvider() {
  if (!m_options["filter-root-path"].empty()) {
    std::string path = m_options["filter-root-path"].as<std::string>();
    logger.info() << "Using Filter root directory " << path;
    logger.info() << "Assuming Filter files are ASCII files";
    std::unique_ptr<XYDataset::FileParser> file_parser {new XYDataset::AsciiParser{}};
    return std::unique_ptr<XYDataset::XYDatasetProvider> {
      new XYDataset::FileSystemProvider{path, std::move(file_parser)}
    };
  }
  logger.error() << "The option 'filter-root-path' is not set";
  throw ElementsException {"Missing or unknown Filter dataset provider options"};
}

std::vector<XYDataset::QualifiedName> ModelingConfiguration::sedList() {
  logger.info() << "Creating SED list...";
  // We use a set to avoid duplicate entries
  std::set<XYDataset::QualifiedName> selected {};
  if (!m_options["sed-group"].empty()) {
    auto provider = sedDatasetProvider();
    auto group_list = m_options["sed-group"].as<std::vector<std::string>>();
    for (auto& group : group_list) {
      logger.info() << "Adding SEDs of group " << group;
      for (auto& name : provider->listContents(group)) {
        selected.insert(name);
      }
    }
  }
  if (!m_options["sed-list"].empty()) {
    auto name_list = m_options["sed-list"].as<std::vector<std::string>>();
    for (auto& name : name_list) {
      logger.info() << "Adding SED " << name;
      selected.insert(XYDataset::QualifiedName{name});
    }
  }
  return std::vector<XYDataset::QualifiedName> {selected.begin(), selected.end()};
}

std::vector<XYDataset::QualifiedName> ModelingConfiguration::reddeningCurveList() {
  logger.info() << "Creating Reddening Curve list...";
  // We use a set to avoid duplicate entries
  std::set<XYDataset::QualifiedName> selected {};
  if (!m_options["reddening-curve-group"].empty()) {
    auto provider = reddeningCurveDatasetProvider();
    auto group_list = m_options["reddening-curve-group"].as<std::vector<std::string>>();
    for (auto& group : group_list) {
      logger.info() << "Adding Reddening Curves of group " << group;
      for (auto& name : provider->listContents(group)) {
        selected.insert(name);
      }
    }
  }
  if (!m_options["reddening-curve-list"].empty()) {
    auto name_list = m_options["reddening-curve-list"].as<std::vector<std::string>>();
    for (auto& name : name_list) {
      logger.info() << "Adding Reddening Curve " << name;
      selected.insert(XYDataset::QualifiedName{name});
    }
  }
  return std::vector<XYDataset::QualifiedName> {selected.begin(), selected.end()};
}

std::vector<XYDataset::QualifiedName> ModelingConfiguration::filterList() {
  logger.info() << "Creating Filter list...";
  // We use a set to avoid duplicate entries
  std::set<XYDataset::QualifiedName> selected {};
  if (!m_options["filter-group"].empty()) {
    auto provider = filterDatasetProvider();
    auto group_list = m_options["filter-group"].as<std::vector<std::string>>();
    for (auto& group : group_list) {
      logger.info() << "Adding Filters of group " << group;
      for (auto& name : provider->listContents(group)) {
        selected.insert(name);
      }
    }
  }
  if (!m_options["filter-list"].empty()) {
    auto name_list = m_options["filter-list"].as<std::vector<std::string>>();
    for (auto& name : name_list) {
      logger.info() << "Adding Filter " << name;
      selected.insert(XYDataset::QualifiedName{name});
    }
  }
  return std::vector<XYDataset::QualifiedName> {selected.begin(), selected.end()};
}

std::vector<double> ModelingConfiguration::zList() {
  logger.info() << "Creating Z list...";
  if (!m_options["z-start"].empty() && !m_options["z-stop"].empty() && !m_options["z-step"].empty()) {
    double z_start = m_options["z-start"].as<double>();
    double z_stop = m_options["z-stop"].as<double>();
    double z_step = m_options["z-step"].as<double>();
    logger.info() << "Adding Z values in range [" << z_start << "," << z_stop
                  << "] with step " << z_step;
    std::vector<double> selected {};
    for (double z=z_start; z<=z_stop; z+=z_step) {
      selected.push_back(z);
    }
    return selected;
  }
  logger.error() << "Some of the z-start, z-stop or z-step parameters are not set";
  throw ElementsException {"Missing or unknown Z options"};
}

std::vector<double> ModelingConfiguration::ebvList() {
  logger.info() << "Creating E(B-V) list...";
  if (!m_options["ebv-start"].empty() && !m_options["ebv-stop"].empty() && !m_options["ebv-step"].empty()) {
    double ebv_start = m_options["ebv-start"].as<double>();
    double ebv_stop = m_options["ebv-stop"].as<double>();
    double ebv_step = m_options["ebv-step"].as<double>();
    logger.info() << "Adding E(B-V) values in range [" << ebv_start << "," << ebv_stop
                  << "] with step " << ebv_step;
    std::vector<double> selected {};
    for (double ebv=ebv_start; ebv<=ebv_stop; ebv+=ebv_step) {
      selected.push_back(ebv);
    }
    return selected;
  }
  logger.error() << "Some of the ebv-start, ebv-stop or ebv-step parameters are not set";
  throw ElementsException {"Missing or unknown E(B-V) options"};
}

} // end of namespace PhzConfiguration