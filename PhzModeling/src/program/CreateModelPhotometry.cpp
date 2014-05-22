/** 
 * @file CreateModelPhotometry.cpp
 * @date May 22, 2014
 * @author Nikolaos Apostolakos
 */

#define SVN_ID "SVN $Id$"
#define SVN_URL "SVN $HeadURL$"

#include <string>
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include "ElementsKernel/ElementsProgram.h"
#include "ElementsKernel/Version.h"
#include "PhzConfiguration/ModelingConfiguration.h"

using namespace std;

class CreateModelPhotometry : public ElementsProgram {

public:
  
  CreateModelPhotometry() = default;
  
  virtual ~CreateModelPhotometry() = default;
  
  po::options_description defineSpecificProgramOptions() {
    po::options_description config_file_options("Model Photometry options");
    config_file_options.add_options()
    ("sed-root-path", po::value<string>(),
        "The directory containing the SED datasets, organized in folders")
    ("sed-group", po::value<vector<string>>(),
        "Use all the SEDs in the given group and subgroups")
    ("sed-list", po::value<vector<string>>(),
        "Use all the given SEDs")
    ("reddening-curve-root-path", po::value<string>(),
        "The directory containing the Reddening Curve datasets, organized in folders")
    ("reddening-curve-group", po::value<vector<string>>(),
        "Use all the Reddening Curves in the given group and subgroups")
    ("reddening-curve-list", po::value<vector<string>>(),
        "Use all the given Reddening Curves")
    ("ebv-start", po::value<double>(), "The E(B-V) range lower limit")
    ("ebv-stop", po::value<double>(), "The E(B-V) range upper limit")
    ("ebv-step", po::value<double>(), "The E(B-V) step")
    ("z-start", po::value<double>(), "The redshift range lower limit")
    ("z-stop", po::value<double>(), "The redshift range upper limit")
    ("z-step", po::value<double>(), "The redshift step")
    ("filter-root-path", po::value<string>(),
        "The directory containing the Filter datasets, organized in folders")
    ("filter-group", po::value<vector<string>>(),
        "Use all the Filters in the given group and subgroups")
    ("filter-list", po::value<vector<string>>(),
        "Use all the given Filters");
    return config_file_options;
  }
  
  void mainMethod() {
    ElementsLogging logger = ElementsLogging::getLogger("CreateModelPhotometry");
    
    const po::variables_map options = this->getVariablesMap();
    
    PhzConfiguration::ModelingConfiguration config {std::move(options)};

    auto sed_provider = config.sedDatasetProvider();
    logger.info();
    logger.info() << "Available SEDs:";
    for (auto& v : sed_provider->listContents("")) {
      logger.info() << v.qualifiedName();
    }
    logger.info();
  
    auto sed_list = config.sedList();
    logger.info();
    logger.info() << "Selected SEDs:";
    for (auto& v : sed_list) {
      logger.info() << v.qualifiedName();
    }
    logger.info();

    auto reddening_curve_provider = config.reddeningCurveDatasetProvider();
    logger.info();
    logger.info() << "Available Reddening Curves:";
    for (auto& v : reddening_curve_provider->listContents("")) {
      logger.info() << v.qualifiedName();
    }
    logger.info();
  
    auto reddening_curve_list = config.reddeningCurveList();
    logger.info();
    logger.info() << "Selected Reddening Curves:";
    for (auto& v : reddening_curve_list) {
      logger.info() << v.qualifiedName();
    }
    logger.info();

    auto filter_provider = config.filterDatasetProvider();
    logger.info();
    logger.info() << "Available Filters:";
    for (auto& v : filter_provider->listContents("")) {
      logger.info() << v.qualifiedName();
    }
    logger.info();
  
    auto filter_list = config.filterList();
    logger.info();
    logger.info() << "Selected Filters:";
    for (auto& v : filter_list) {
      logger.info() << v.qualifiedName();
    }
    logger.info();
    
    auto z_list = config.zList();
    logger.info();
    logger.info() << "Selected Zs:";
    for (auto& v : z_list) {
      logger.info() << v;
    }
    logger.info();
    
    auto ebv_list = config.ebvList();
    logger.info();
    logger.info() << "Selected E(B-V)s:";
    for (auto& v : ebv_list) {
      logger.info() << v;
    }
    logger.info();
  }
  
  string getVersion() {
    return getVersionFromSvnKeywords(SVN_URL, SVN_ID);
  }

}; // end of class CreateModelPhotometry

MAIN_FOR(CreateModelPhotometry)