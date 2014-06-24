/** 
 * @file ExportModelDataset.cpp
 * @date May 24, 2014
 * @author Nikolaos Apostolakos
 */

#define SVN_ID "SVN $Id$"
#define SVN_URL "SVN $HeadURL$"

#include <sstream>
#include <iomanip>
#include <fstream>
#include <boost/filesystem.hpp>
namespace fs = boost::filesystem;
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include <CCfits/CCfits>
#include "ElementsKernel/ElementsProgram.h"
#include "ElementsKernel/Version.h"
#include "ChTable/Table.h"
#include "ChTable/AsciiWriter.h"
#include "ChTable/FitsWriter.h"
#include "PhzConfiguration/ModelingConfiguration.h"
#include "PhzDataModel/PhzModel.h"
#include "PhzModeling/ModelMatrix.h"
#include "PhzModeling/ModelDataManager.h"

using namespace std;
using namespace XYDataset;
using namespace PhzDataModel;
using namespace ChTable;

class ExportModelDataset : public ElementsProgram {
  
public:
  
  ExportModelDataset() = default;
  
  virtual ~ExportModelDataset() = default;
  
  po::options_description defineSpecificProgramOptions() {
    po::options_description config_file_options("Model Photometry options");
    config_file_options.add_options()
    ("output-dir", po::value<string>(),
        "The directory to export the model datasets")
    ("output-format", po::value<string>(),
        "The format to export the datasets in (FITS or ASCII)")
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
    ("ebv-range", po::value<vector<string>>(), "Use the E(B-V) values in the given range (min max step)")
    ("ebv-list", po::value<vector<string>>(), "Use the given space separated E(B-V) values")
    ("z-range", po::value<vector<string>>(), "Use the Z values in the given range (min max step)")
    ("z-list", po::value<vector<string>>(), "Use the given space separated Z values");
    return config_file_options;
  }
  
  void mainMethod() {
    ElementsLogging logger = ElementsLogging::getLogger("CreateModelPhotometry");
    
    const po::variables_map options = this->getVariablesMap();
    
    PhzConfiguration::ModelingConfiguration config {std::move(options)};
    
    auto axes_tuple = createAxesTuple(config.zList(), config.ebvList(),
                                  config.reddeningCurveList(), config.sedList());

    std::unique_ptr<PhzModeling::ModelDataManager> model_function_manager {
            new PhzModeling::ModelDataManager {axes_tuple,
                config.sedDatasetProvider(), config.reddeningCurveDatasetProvider()}};
    
    PhzModeling::ModelMatrix model_matrix {std::move(model_function_manager), axes_tuple};
    
    // We get the output directory
    if (options["output-dir"].empty()) {
      logger.error("Missing parameter output-dir");
      throw ElementsException() << "Missing parameter output-dir";
    }
    string out_dir_string = options["output-dir"].as<string>();
    fs::path out_dir {out_dir_string};
    if (!fs::is_directory(out_dir)) {
      logger.error() << "Output directory " << out_dir << " does not exist";
      throw ElementsException() << "Output directory " << out_dir << " does not exist";
    }
    
    // We get the format
    if (options["output-format"].empty()) {
      logger.error("Missing parameter output-format");
      throw ElementsException() << "Missing parameter output-format";
    }
    string out_format = options["output-format"].as<string>();
    if (out_format != "FITS" && out_format != "ASCII") {
      logger.error("Parameter output-format must be either 'FITS' or 'ASCII'");
      throw ElementsException() << "Parameter output-format must be either 'FITS' or 'ASCII'";
    }
    
    size_t size = model_matrix.size();
    size_t size_length = boost::lexical_cast<std::string>(size).size();
    size_t counter {};
    logger.info() << "Exporting " << size << " datasets in "
                  << out_dir << " in " << out_format << " format...";
    for (auto iter=model_matrix.begin(); iter!=model_matrix.end(); ++iter) {
      ++counter;
      QualifiedName sed = iter.axisValue<ModelParameter::SED>();
      QualifiedName reddening_curve = iter.axisValue<ModelParameter::REDDENING_CURVE>();
      double ebv = iter.axisValue<ModelParameter::EBV>();
      double z = iter.axisValue<ModelParameter::Z>();
      stringstream filename {};
      filename << out_dir.string() << "/" << setfill('0') << setw(size_length)
               << counter << "-" << sed.datasetName() << "_" << reddening_curve.datasetName()
               << "_EBV" << ebv << "_Z" << z;
      if (out_format == "FITS") {
        filename << ".fits";
      } else {
        filename << ".dat";
      }
      logger.info() << "Exporting model " << counter << " with SED=" << sed.qualifiedName()
                    << ", Reddening Curve=" << reddening_curve.qualifiedName()
                    << ", E(B-V)=" << ebv << " and Z=" << z << " in file " << filename.str();
      
      shared_ptr<ColumnInfo> column_info {new ColumnInfo {{
        ColumnInfo::info_type("Wavelength", typeid(double)),
        ColumnInfo::info_type("Flux", typeid(double))
      }}};
      vector<Row> row_list {};
      for (auto& xy : *iter) {
        row_list.push_back(Row{{xy.first, xy.second}, column_info});
      }
      Table table {row_list};
      {
        if (out_format == "FITS") {
          std::unique_ptr<CCfits::FITS> fits {new CCfits::FITS("!"+filename.str(), CCfits::RWmode::Write)};
          FitsWriter().write(*fits, "ModelDataset", table);
        } else {
          ofstream out {filename.str()};
          AsciiWriter().write(out, table);
        }
      }
    }
    logger.info() << "Finished exporting model datasets. Exiting...";
  }
  
  string getVersion() {
    return getVersionFromSvnKeywords(SVN_URL, SVN_ID);
  }
  
}; // end of class ExportModelDataset

MAIN_FOR(ExportModelDataset)
