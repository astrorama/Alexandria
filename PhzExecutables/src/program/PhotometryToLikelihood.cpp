/** 
 * @file PhotometryToLikelihood.cpp
 * @date May 23, 2014
 * @author Nikolaos Apostolakos
 */

#define SVN_ID "SVN $Id$"
#define SVN_URL "SVN $HeadURL$"

#include <fstream>
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include "ElementsKernel/ElementsProgram.h"
#include "ElementsKernel/Version.h"
#include "ChTable/AsciiReader.h"
#include "PhzDataModel/PhotometryMatrix.h"
#include "PhzLikelihood/ModelScaleFunctor.h"
#include "PhzLikelihood/ChiSquareFunctor.h"
#include "ChCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "ChCatalog/CatalogFromTable.h"
#include "ChTable/AsciiWriter.h"

using namespace std;
using namespace ChCatalog;
using namespace ChTable;
using namespace PhzDataModel;
using namespace PhzLikelihood;

class PhotometryToLikelihood : public ElementsProgram {
  
public:
  
  PhotometryToLikelihood() = default;
  
  virtual ~PhotometryToLikelihood() = default;
  
  po::options_description defineSpecificProgramOptions() {
    po::options_description config_file_options("PhotometryToLikelihood options");
    config_file_options.add_options()
    ("photometric-catalog", po::value<string>(),
        "The catalog containing the observed photometric fluxes and their errors")
    ("model-photometry-matrix", po::value<string>(),
        "The file with the matrix containing the model photometries")
    ("phz-catalog", po::value<string>(),
        "The file to create the photometric redshift catalog in");
    return config_file_options;
  }
  
  void mainMethod() {
    ElementsLogging logger = ElementsLogging::getLogger("PhotometryToLikelihood");
    
    const po::variables_map options = this->getVariablesMap();
    
    string model_phot_matrix_file = options["model-photometry-matrix"].as<string>();
    logger.info() << "Reading Model photometry matrix from file " << model_phot_matrix_file;
    unique_ptr<PhotometryMatrix> model_phot_marix;
    {
      ifstream in {model_phot_matrix_file};
      model_phot_marix = binaryImportPhzMatrix<vector<Photometry>>(in);
    }
    
    string phot_catalog_file = options["photometric-catalog"].as<string>();
    logger.info() << "Reading photometric catalog from file " << phot_catalog_file;
    fstream phot_catalog_in {phot_catalog_file};
    vector<std::type_index> mer_column_types {
      typeid(int64_t), // ID
      typeid(double), // FLUX_G
      typeid(double), // FLUX_R
      typeid(double), // FLUX_I
      typeid(double), // FLUX_VIS
      typeid(double), // FLUX_Z
      typeid(double), // FLUX_Y
      typeid(double), // FLUX_J
      typeid(double), // FLUX_H
      typeid(double), // FLUXERR_G
      typeid(double), // FLUXERR_R
      typeid(double), // FLUXERR_I
      typeid(double), // FLUXERR_VIS
      typeid(double), // FLUXERR_Z
      typeid(double), // FLUXERR_Y
      typeid(double), // FLUXERR_J
      typeid(double), // FLUXERR_H
      typeid(double), // ZSPEC
      typeid(int32_t), // AGN_FLAG
      typeid(int64_t) // SUPER_ID
    };
    Table phot_catalog_table = AsciiReader(mer_column_types).read(phot_catalog_in);
    
    logger.info() << "Converting the table to catalog";
    map<string, pair<string, string>> filter_name_mapping {};
    filter_name_mapping["MER/Ynir_WFC3f105w"] = pair<string, string>{"FLUX_Y","FLUXERR_Y"};
    filter_name_mapping["MER/Iext_ACSf775w"] = pair<string, string>{"FLUX_I","FLUXERR_I"};
    filter_name_mapping["MER/Gext_ACSf435w"] = pair<string, string>{"FLUX_G","FLUXERR_G"};
    filter_name_mapping["MER/Hnir_WFC3f160w"] = pair<string, string>{"FLUX_H","FLUXERR_H"};
    filter_name_mapping["MER/Rext_ACSf606w"] = pair<string, string>{"FLUX_R","FLUXERR_R"};
    filter_name_mapping["MER/Jnir_WFC3f125w"] = pair<string, string>{"FLUX_J","FLUXERR_J"};
    filter_name_mapping["MER/Zext_ACSf850lp"] = pair<string, string>{"FLUX_Z","FLUXERR_Z"};
    filter_name_mapping["MER/VIS_ACSf814w"] = pair<string, string>{"FLUX_VIS","FLUXERR_VIS"};
    vector<unique_ptr<AttributeFromRow>> attribute_from_row_ptr_vector {};
    attribute_from_row_ptr_vector.push_back(unique_ptr<AttributeFromRow>{new PhotometryAttributeFromRow{phot_catalog_table.getColumnInfo(), filter_name_mapping}});
    CatalogFromTable catalog_from_table {phot_catalog_table.getColumnInfo(), "ID", move(attribute_from_row_ptr_vector)};
    Catalog phot_catalog = catalog_from_table.createCatalog(phot_catalog_table);
    
    shared_ptr<ColumnInfo> column_info {new ColumnInfo {{
      ColumnInfo::info_type("ID", typeid(int64_t)),
      ColumnInfo::info_type("SED", typeid(string)),
      ColumnInfo::info_type("ReddeningCurve", typeid(string)),
      ColumnInfo::info_type("E(B-V)", typeid(double)),
      ColumnInfo::info_type("Z", typeid(double))
    }}};
    vector<Row> row_list {};
    
    ModelScaleFunctor model_scale_functor {};
    ChiSquareFunctor chi_2_functor {};
    logger.info() << "Processing " << phot_catalog.size() << " sources";
    int counter {0};
    for (auto source_iter=phot_catalog.cbegin(); source_iter!=phot_catalog.cend(); ++source_iter) {
      const Source& source_const = *source_iter;
      Source& source = const_cast<Source&>(source_const);
      ++counter;
      if (counter%100 == 0) {
        logger.info() << "Processing source " << counter << " with ID " << source.getId();
      }
      
      // Create the chi2 matrix
      auto source_phot = source.getAttribute<Photometry>();
      PhzMatrix<vector<double>> chi2_matrix {model_phot_marix->axisInfoTuple()};
      auto model_iter = model_phot_marix->begin();
      auto chi2_iter = chi2_matrix.begin();
      while (model_iter != model_phot_marix->end()) {
        double alpha = model_scale_functor(*source_phot, *model_iter);
        *chi2_iter = chi_2_functor(*source_phot, *model_iter, alpha);
        ++model_iter;
        ++chi2_iter;
      }
      
      // Get the PHZ value as the maximum of the chi2 matrix
      string sed {};
      string reddening_curve {};
      double ebv {};
      double z {};
      double max_chi2 = -1;
      for (auto chi2_iter=chi2_matrix.begin(); chi2_iter!=chi2_matrix.end(); ++ chi2_iter) {
        if (*chi2_iter > max_chi2) {
          max_chi2 = *chi2_iter;
          sed = chi2_iter.axisValue<ModelParameter::SED>().qualifiedName();
          reddening_curve = chi2_iter.axisValue<ModelParameter::REDDENING_CURVE>().qualifiedName();
          ebv = chi2_iter.axisValue<ModelParameter::EBV>();
          z = chi2_iter.axisValue<ModelParameter::Z>();
        }
      }
      
      // Add a row for the output catalog
      row_list.push_back(Row{{source.getId(), sed, reddening_curve, ebv, z}, column_info});
    }
    
    Table phz_table {row_list};
    {
      ofstream out {options["phz-catalog"].as<string>()};
      AsciiWriter().write(out, phz_table);
    }
  }
  
  string getVersion() {
    return getVersionFromSvnKeywords(SVN_URL, SVN_ID);
  }
  
}; //end of class PhotometryToLikelihood

MAIN_FOR(PhotometryToLikelihood)