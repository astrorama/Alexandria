/** 
 * @file src/lib/ModelingConfiguration.cpp
 * @date May 21, 2014
 * @author Nikolaos Apostolakos
 */

#include <set>
#include <sstream>
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"
#include "XYDataset/FileParser.h"
#include "XYDataset/AsciiParser.h"
#include "XYDataset/FileSystemProvider.h"
#include "PhzConfiguration/ModelingConfiguration.h"

namespace Euclid {
namespace PhzConfiguration {

Elements::Logging logger = Elements::Logging::getLogger("ModelingConfiguration");

ModelingConfiguration::ModelingConfiguration(std::map<std::string, option_type> options)
          : m_options{std::move(options)} { }

std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> ModelingConfiguration::sedDatasetProvider() {
  if (!m_options["sed-root-path"].empty()) {
    std::string path = m_options["sed-root-path"].as<std::string>();
    logger.info() << "Using SED root directory " << path;
    logger.info() << "Assuming SED files are ASCII files";
    std::unique_ptr<Euclid::XYDataset::FileParser> file_parser {new Euclid::XYDataset::AsciiParser{}};
    return std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> {
      new Euclid::XYDataset::FileSystemProvider{path, std::move(file_parser)}
    };
  }
  logger.error() << "The option 'sed-root-path' is not set";
  throw Elements::Exception {"Missing or unknown SED dataset provider options"};
}

std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> ModelingConfiguration::reddeningCurveDatasetProvider() {
  if (!m_options["reddening-curve-root-path"].empty()) {
    std::string path = m_options["reddening-curve-root-path"].as<std::string>();
    logger.info() << "Using Reddening Curve root directory " << path;
    logger.info() << "Assuming Reddening Curve files are ASCII files";
    std::unique_ptr<Euclid::XYDataset::FileParser> file_parser {new Euclid::XYDataset::AsciiParser{}};
    return std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> {
      new Euclid::XYDataset::FileSystemProvider{path, std::move(file_parser)}
    };
  }
  logger.error() << "The option 'reddening-curve-root-path' is not set";
  throw Elements::Exception {"Missing or unknown Reddening Curve dataset provider options"};
}

std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> ModelingConfiguration::filterDatasetProvider() {
  if (!m_options["filter-root-path"].empty()) {
    std::string path = m_options["filter-root-path"].as<std::string>();
    logger.info() << "Using Filter root directory " << path;
    logger.info() << "Assuming Filter files are ASCII files";
    std::unique_ptr<Euclid::XYDataset::FileParser> file_parser {new Euclid::XYDataset::AsciiParser{}};
    return std::unique_ptr<Euclid::XYDataset::XYDatasetProvider> {
      new Euclid::XYDataset::FileSystemProvider{path, std::move(file_parser)}
    };
  }
  logger.error() << "The option 'filter-root-path' is not set";
  throw Elements::Exception {"Missing or unknown Filter dataset provider options"};
}

std::vector<Euclid::XYDataset::QualifiedName> ModelingConfiguration::sedList() {
  logger.info() << "Creating SED list...";
  // We use a set to avoid duplicate entries
  std::set<Euclid::XYDataset::QualifiedName> selected {};
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
      selected.insert(Euclid::XYDataset::QualifiedName{name});
    }
  }
  if (selected.empty()) {
    logger.error() << "SED list is empty (check the options sed-group and sed-list)";
    throw Elements::Exception() << "Empty SED list";
  }
  return std::vector<Euclid::XYDataset::QualifiedName> {selected.begin(), selected.end()};
}

std::vector<Euclid::XYDataset::QualifiedName> ModelingConfiguration::reddeningCurveList() {
  logger.info() << "Creating Reddening Curve list...";
  // We use a set to avoid duplicate entries
  std::set<Euclid::XYDataset::QualifiedName> selected {};
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
      selected.insert(Euclid::XYDataset::QualifiedName{name});
    }
  }
  if (selected.empty()) {
    logger.error() << "Reddening Curve list is empty (check the options reddening-curve-group and reddening-curve-list)";
    throw Elements::Exception() << "Empty Reddening Curve list";
  }
  return std::vector<Euclid::XYDataset::QualifiedName> {selected.begin(), selected.end()};
}

std::vector<Euclid::XYDataset::QualifiedName> ModelingConfiguration::filterList() {
  logger.info() << "Creating Filter list...";
  // We use a set to avoid duplicate entries
  std::set<Euclid::XYDataset::QualifiedName> selected {};
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
      selected.insert(Euclid::XYDataset::QualifiedName{name});
    }
  }
  if (selected.empty()) {
    logger.error() << "Filter list is empty (check the options filter-group and filter-list)";
    throw Elements::Exception() << "Empty Filter list";
  }
  return std::vector<Euclid::XYDataset::QualifiedName> {selected.begin(), selected.end()};
}

std::vector<double> ModelingConfiguration::zList() {
  logger.info() << "Creating Z list...";
  // We use a set to avoid duplicates and to order the different entries
  std::set<double> selected {};
  if (!m_options["z-range"].empty()) {
    auto ranges_list = m_options["z-range"].as<std::vector<std::string>>();
    for (auto& range_string : ranges_list) {
      std::stringstream range_stream {range_string};
      double min {};
      double max {};
      double step {};
      range_stream >> min >> max >> step;
      logger.info() << "Adding Z values in range [" << min << "," << max
                    << "] with step " << step;
      for (double value=min; value<=max; value+=step) {
        selected.insert(value);
      }
    }
  }
  if (!m_options["z-list"].empty()) {
    auto values_list = m_options["z-list"].as<std::vector<std::string>>();
    for (auto& values_string : values_list) {
      logger.info() << "Adding Z values " << values_string;
      std::stringstream values_stream {values_string};
      while (values_stream.good()) {
        double value {};
        values_stream >> value;
        selected.insert(value);
      }
    }
  }
  if (selected.empty()) {
    logger.error() << "Z list is empty (check the options z-range and z-list)";
    throw Elements::Exception() << "Empty Z list";
  }
  return std::vector<double> {selected.begin(), selected.end()};
}

std::vector<double> ModelingConfiguration::ebvList() {
  logger.info() << "Creating E(B-V) list...";
  // We use a set to avoid duplicates and to order the different entries
  std::set<double> selected {};
  if (!m_options["ebv-range"].empty()) {
    auto ranges_list = m_options["ebv-range"].as<std::vector<std::string>>();
    for (auto& range_string : ranges_list) {
      std::stringstream range_stream {range_string};
      double min {};
      double max {};
      double step {};
      range_stream >> min >> max >> step;
      logger.info() << "Adding E(B-V) values in range [" << min << "," << max
                    << "] with step " << step;
      for (double value=min; value<=max; value+=step) {
        selected.insert(value);
      }
    }
  }
  if (!m_options["ebv-list"].empty()) {
    auto values_list = m_options["ebv-list"].as<std::vector<std::string>>();
    for (auto& values_string : values_list) {
      logger.info() << "Adding E(B-V) values " << values_string;
      std::stringstream values_stream {values_string};
      while (values_stream.good()) {
        double value {};
        values_stream >> value;
        selected.insert(value);
      }
    }
  }
  if (selected.empty()) {
    logger.error() << "E(B-V) list is empty (check the options ebv-range and ebv-list)";
    throw Elements::Exception() << "Empty E(B-V) list";
  }
  return std::vector<double> {selected.begin(), selected.end()};
}

} // end of namespace PhzConfiguration
} // end of namespace Euclid