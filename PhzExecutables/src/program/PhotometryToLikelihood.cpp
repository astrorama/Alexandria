/** 
 * @file src/program/PhotometryToLikelihood.cpp
 * @date May 23, 2014
 * @author Nikolaos Apostolakos
 */

#define SVN_ID "SVN $Id$"
#define SVN_URL "SVN $HeadURL$"

#include <fstream>
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include <CCfits/CCfits>
#include "ElementsKernel/Program.h"
#include "ElementsKernel/Version.h"
#include "Table/AsciiReader.h"
#include "PhzDataModel/PhotometryGrid.h"
#include "PhzDataModel/LikelihoodGrid.h"
#include "PhzLikelihood/ModelScaleFunctor.h"
#include "PhzLikelihood/ChiSquareFunctor.h"
#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "SourceCatalog/CatalogFromTable.h"
#include "Table/AsciiWriter.h"
#include "Table/FitsReader.h"

using namespace std;
using namespace Euclid::SourceCatalog;
using namespace Euclid::Table;
using namespace Euclid::PhzDataModel;
using namespace Euclid::PhzLikelihood;

class PhotometryToLikelihood : public Elements::Program {
  
public:
  
  PhotometryToLikelihood() = default;
  
  virtual ~PhotometryToLikelihood() = default;
  
  po::options_description defineSpecificProgramOptions() {
    po::options_description config_file_options("PhotometryToLikelihood options");
    config_file_options.add_options()
    ("photometric-catalog", po::value<string>(),
        "The catalog containing the observed photometric fluxes and their errors")
    ("photometric-catalog-format", po::value<string>()->default_value("ASCII"),
        "The format of the photometric catalog")
    ("model-photometry-grid", po::value<string>(),
        "The file with the grid containing the model photometries")
    ("phz-catalog", po::value<string>(),
        "The file to create the photometric redshift catalog in");
    return config_file_options;
  }
  
  Elements::ExitCode mainMethod() {
    Elements::Logging logger = Elements::Logging::getLogger("PhotometryToLikelihood");
    
    const po::variables_map options = this->getVariablesMap();
    
    string model_phot_grid_file = options["model-photometry-grid"].as<string>();
    logger.info() << "Reading Model photometry grid from file " << model_phot_grid_file;
    ifstream in {model_phot_grid_file};
    PhotometryGrid model_phot_grid = phzGridBinaryImport<vector<Photometry>>(in);
    in.close();
    
    string phot_catalog_file = options["photometric-catalog"].as<string>();
    logger.info() << "Reading photometric catalog from file " << phot_catalog_file;
    string phot_catalog_format = options["photometric-catalog-format"].as<string>();
    Table phot_catalog_table = (phot_catalog_format == "FITS")
                             ? readFitsPhotometricCatalog(phot_catalog_file)
                             : readAsciiPhotometricCatalog(phot_catalog_file);
    
    logger.info() << "Converting the table to catalog";
    vector<pair<string, pair<string, string>>> filter_name_mapping
              = (phot_catalog_format == "FITS")
              ? getFitsFilterNameMapping()
              : getAsciiFilterNameMapping();
    vector<unique_ptr<AttributeFromRow>> attribute_from_row_ptr_vector {};
    attribute_from_row_ptr_vector.push_back(unique_ptr<AttributeFromRow>{new PhotometryAttributeFromRow{phot_catalog_table.getColumnInfo(), filter_name_mapping}});
    string id_column = (phot_catalog_format == "FITS")
                     ? "SOURCE_ID" : "ID";
    CatalogFromTable catalog_from_table {phot_catalog_table.getColumnInfo(), id_column, move(attribute_from_row_ptr_vector)};
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
      
      // Create the chi2 grid
      auto source_phot = source.getAttribute<Photometry>();
      LikelihoodGrid chi2_grid {model_phot_grid.getAxesTuple()};
      auto model_iter = model_phot_grid.begin();
      auto chi2_iter = chi2_grid.begin();
      while (model_iter != model_phot_grid.end()) {
        double alpha = model_scale_functor(*source_phot, *model_iter);
        *chi2_iter = chi_2_functor(*source_phot, *model_iter, alpha);
        ++model_iter;
        ++chi2_iter;
      }
      
      // Get the PHZ value as the maximum of the chi2 grid
      string sed {};
      string reddening_curve {};
      double ebv {};
      double z {};
      double max_chi2 = -1;
      for (auto chi2_iter=chi2_grid.begin(); chi2_iter!=chi2_grid.end(); ++ chi2_iter) {
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
    
    return Elements::ExitCode::OK;
  }
  
  string getVersion() {
    return Elements::getVersionFromSvnKeywords(SVN_URL, SVN_ID);
  }
  
private:
  
  Table readAsciiPhotometricCatalog(string filename) {
    fstream phot_catalog_in {filename};
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
    return AsciiReader(mer_column_types).read(phot_catalog_in);
  }
  
  vector<pair<string, pair<string, string>>> getAsciiFilterNameMapping() {
    vector<pair<string, pair<string, string>>> filter_name_mapping {};
    filter_name_mapping.push_back(make_pair(string{"MER/Ynir_WFC3f105w"}, pair<string, string>{"FLUX_Y","FLUXERR_Y"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Iext_ACSf775w"}, pair<string, string>{"FLUX_I","FLUXERR_I"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Gext_ACSf435w"}, pair<string, string>{"FLUX_G","FLUXERR_G"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Hnir_WFC3f160w"}, pair<string, string>{"FLUX_H","FLUXERR_H"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Rext_ACSf606w"}, pair<string, string>{"FLUX_R","FLUXERR_R"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Jnir_WFC3f125w"}, pair<string, string>{"FLUX_J","FLUXERR_J"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Zext_ACSf850lp"}, pair<string, string>{"FLUX_Z","FLUXERR_Z"}));
    filter_name_mapping.push_back(make_pair(string{"MER/VIS_ACSf814w"}, pair<string, string>{"FLUX_VIS","FLUXERR_VIS"}));
    return filter_name_mapping;
  }
  
  Table readFitsPhotometricCatalog(string filename) {
    CCfits::FITS fits {filename};
    return FitsReader().read(fits.extension(1));
  }
  
  vector<pair<string, pair<string, string>>> getFitsFilterNameMapping() {
    vector<pair<string, pair<string, string>>> filter_name_mapping {};
    filter_name_mapping.push_back(make_pair(string{"MER/Ynir_WFC3f105w"}, pair<string, string>{"NIR_Y","NIR_Y_ERR"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Iext_ACSf775w"}, pair<string, string>{"EXT_i","EXT_i_ERR"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Gext_ACSf435w"}, pair<string, string>{"EXT_g","EXT_g_ERR"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Hnir_WFC3f160w"}, pair<string, string>{"NIR_H","NIR_H_ERR"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Rext_ACSf606w"}, pair<string, string>{"EXT_r","EXT_r_ERR"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Jnir_WFC3f125w"}, pair<string, string>{"NIR_J","NIR_J_ERR"}));
    filter_name_mapping.push_back(make_pair(string{"MER/Zext_ACSf850lp"}, pair<string, string>{"EXT_z","EXT_z_ERR"}));
    filter_name_mapping.push_back(make_pair(string{"MER/VIS_ACSf814w"}, pair<string, string>{"VIS","VIS_ERR"}));
    return filter_name_mapping;
  }
  
}; //end of class PhotometryToLikelihood

MAIN_FOR(PhotometryToLikelihood)