/**
 * @file ProtoZpdf.cpp
 * @date Dec 18, 2013
 * @author Pierre Dubath
 */
/**
 * This macro includes svn tags that are expanded upon any commit. The program version
 * output on screen with the option --version is extracted from these keywords
 *
 * When creating a new file, naked svn tag (see below) should be introduced, they are then
 * expanded with the first commit.
 *
 *    \#define VERSION "SVN $Id: ElementsProgramExample.cpp 3176 2013-08-28 13:13:04Z pdubath $"
 *    \#define REVISION "SVN $Revision: 3176 $"
 *    \#define URL "SVN $HeadURL: http://euclid.esac.esa.int/svn/EC/SGS/SDC/CH/Projects/Elements/trunk/ElementsExamples/src/Program/ElementsProgramExample.cpp $"
 */
#define SVN_ID "SVN $Id$"
#define SVN_URL "SVN $HeadURL$"
#define MY_ASCII_TABLE_COLUMN_WIDTH 15

// System includes
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
// BOOST includes
#include <boost/program_options.hpp>
namespace po = boost::program_options;
// Service includes
#include "ElementsKernel/ElementsLogging.h"
#include "ElementsKernel/ElementsException.h"
// Other includes
#include "ElementsKernel/ElementsProgram.h"
#include "ElementsKernel/Version.h"

#include "ChDataHandling/Factory.h"
#include "ChDataHandling/Areader.h"
#include "ChDataModel/Survey.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"
#include "ChDataModel/Enumerations/SurveyNames.h"

#include "ProtoZ/parameter/FluxModelingParameters.h"
namespace param = ProtoZ::parameter;
#include "ProtoZ/matrix/FluxMatrix.h"
#include "ProtoZ/matrix/PdfMatrix.h"
#include "ProtoZ/matrix/serialize.h"
#include "ProtoZ/matrix/MatrixAsciiExporter.h"
#include "ProtoZ/output/PdfDataFitsOutput.h"
#include "ProtoZ/FluxToPdf.h"
namespace matrix = ProtoZ::matrix;

using namespace std;
using namespace ChDataModel;

/**
 * @class ElementsProgramExample
 * @brief
 * 		Example of an Elements program
 * @details
 * 		This class is an example of a program based on the ElementsProgram class. It can be copied/pasted
 * 		conveniently to write a new program.
 */
class ProtoZpdf: public ElementsProgram {

public:

  /**
   * @brief Constructor
   */
  ProtoZpdf() {
  }

  /**
   * @brief Destructor
   */
  virtual ~ProtoZpdf() {
  }

  /**
   * @brief
   *    Allows to define the (command line and configuration file) options specific to
   *    this program
   * @details
   *    See the ElementsProgram documentation for more details.
   * @return
   *    A BOOST program options_description
   */
  po::options_description defineSpecificProgramOptions() {

    /**
     * Document all program options specific to this program
     */
    po::options_description config_file_options("Configuration options");
    config_file_options.add_options()
    // A example string option
    ("survey-name", po::value<string>()->default_value(string { }),
        "The name of the Survey, i.e., COSMOS or EUCLID so far")
    // A example string option
    ("flux-matrix-path", po::value<string>()->default_value(string { }),
        "The flux matrix path")
    // A example string option
    ("photometric-catalog-path", po::value<string>()->default_value(string { }),
        "The photometric catalog path")
    // A int option
    ("catalog-start-line", po::value<int>()->default_value(2),
        "The start line in the catalog")
    // A int option
    ("source-number", po::value<int>()->default_value(10),
        "The number of to-be-processed sources")
    // Path of the file for the catalog output results
    ("catalog-output-file", po::value<string>()->default_value(string { }),
        "Path of the catalog output results")
    // Path of the file for the PDF data output results
    ("pdf-data-output-file", po::value<string>()->default_value(string { }),
        "Path of the PDF data output results");

//    // A string vector option
//    ("string-vector",
//        po::value<vector<string>>()->multitoken()->default_value(
//            vector<string> { }, "Empty"), "A string vector")
//    // A int vector option
//    ("int-vector",
//        po::value<vector<int>>()->multitoken()->default_value(vector<int> { },
//            "Empty"), "An int vector")
//    // A double vector option
//    ("double-vector",
//        po::value<vector<double>>()->multitoken()->default_value(
//            vector<double> { }, "Empty"), "A double vector");

    return config_file_options;
  }

  /**
   * @brief
   *    The "main" method.
   * @details
   *    This method is the entry point to the program. In this sense, it is similar to a main
   *    (and it is why it is called mainMethod()). The code below provides only example stuff
   *    which should be replaced by real code in any program.
   *
   *    See the ElementsProgram documentation for more details.
   *
   */
  void mainMethod() {

    // Get logger and log the entry into the mainMethod
    ElementsLogging logger = ElementsLogging::getLogger("ProtoZpdf");

    logger.info("#");
    logger.info("#  Logging from the mainMethod() of the ProtoZpdf ");
    logger.info("#");

    // Get the map with all program options
    const po::variables_map variables_map = this->getVariablesMap();

    // Retrieve values from the po::variables_map
    string survey_name = variables_map["survey-name"].as<string>();
    string flux_matrix_path = variables_map["flux-matrix-path"].as<string>();
    string photometric_catalog_path =
        variables_map["photometric-catalog-path"].as<string>();
    int catalog_start_line = variables_map["catalog-start-line"].as<int>();
    int source_number = variables_map["source-number"].as<int>();
    string catalog_output_file = variables_map["catalog-output-file"].as<string>();
    string pdf_data_output_file = variables_map["pdf-data-output-file"].as<string>();

    //    double z_step = variables_map["z-step"].as<double>();
//    double z_stop = variables_map["z-stop"].as<double>();
//    double ebmv_start = variables_map["ebmv-start"].as<double>();
//    double ebmv_step = variables_map["ebmv-step"].as<double>();
//    double ebmv_stop = variables_map["ebmv-stop"].as<double>();
//    double lambda_interpolation_step = variables_map["lambda-interpolation-step"].as<double>();
//    int64_t interpolation_poly_degree = variables_map["interpolation-poly-degree"].as<int64_t>();

    try {

      // Do something here
      logger.info("#");
      logger.info("#    This is the place where we will do the job ");
      logger.info("#");

      ProtoZ::matrix::FluxMatrix flux_matrix { flux_matrix_path };

      FluxToPdf fluxToPdf { flux_matrix };

      Survey* survey { };
      Catalog catalog { };
      Areader aReader { };

      if (survey_name == "COSMOS") {
        survey = Factory::createSurvey(SurveyNames::COSMOS);
        catalog = *(Factory::createCatalogInSurvey(survey,
            photometric_catalog_path, 5, 5));
      } else if (survey_name == "EUCLID") {
        survey = Factory::createSurvey(SurveyNames::EUCLID);
        catalog = aReader.getCatalog(photometric_catalog_path,
            catalog_start_line, source_number);
      };

      logger.info("#");
      logger.info("#    The catalog is loaded with %d sources ",
          catalog.size());
      logger.info("#");

      std::map<int64_t, Source> source_map = catalog.getSourceMap();
      ProtoZ::matrix::PdfMatrix pdfMatrix { flux_matrix };

      std::vector<std::string> catalog_results;
      std::stringstream source_results;
      
      PdfDataFitsOutput pdfOutput {pdf_data_output_file};
      // We calculate the zValues vector here because it is the same for all objects
      std::vector<double> zValues {};
      for (uint i=0; i<pdfMatrix.getZAxis().size(); i++) {
        zValues.push_back(pdfMatrix.getZAxis().indexToValue(i));
      }

      SedNames sedName { };
      double ebv { };
      string extLaw { };
      double redshift { };
      double max = 0.0;
      
      int i {0};
      for (auto source : source_map) {
        i++;
        if ( i%10 == 0 ) { logger.info("Processing source no %d, with ID %d", i, source.second.getSourceId()); }
        if (source.second.getSpecZ() > 0.0
            && source.second.getAgnFlag() < 990) {
          pdfMatrix = fluxToPdf.compute(source.second);
          std::tie(sedName, ebv, extLaw, redshift, max) = fluxToPdf.getMax(pdfMatrix);
          // Get the marginalization
          double z_marginalization = fluxToPdf.analyzePdf(pdfMatrix);
          // Save the marginalized PDF to file
          pdfOutput.addPdf(source.first, zValues, fluxToPdf.marginalizePdf(pdfMatrix));
          // Save data to file
          source_results.str(std::string());
          source_results << source.second.getSourceId()
              << std::setw(MY_ASCII_TABLE_COLUMN_WIDTH)
              << source.second.getSpecZ() << std::setw(MY_ASCII_TABLE_COLUMN_WIDTH)
              << redshift << std::setw(MY_ASCII_TABLE_COLUMN_WIDTH)
              << sedName << std::setw(MY_ASCII_TABLE_COLUMN_WIDTH)
              << ebv << std::setw(MY_ASCII_TABLE_COLUMN_WIDTH)
              << max << std::setw(MY_ASCII_TABLE_COLUMN_WIDTH)
              << z_marginalization;
          catalog_results.push_back(source_results.str());

        }
      }

//      std::vector<ProtoZ::matrix::PdfMatrix> pdf_vector = fluxToPdf.process(
//          catalog);

      logger.info("#");
      logger.info("#    The pdf calculation and result extraction is completed ");
      logger.info("#");

      aReader.writeAsciiFile(catalog_results, catalog_output_file);

//      pdf_vector.at(1).exportAsAscii("/tmp/pdftable.dat");

    } catch (const ElementsException & e) {
      logger.info("#");
      logger.info("  In ElementsProgramExample::mainMethod(),");
      logger.info("      an exception: ");
      logger.info("#");
      logger.info("         %s", e.what());
      logger.info("#");
      logger.info("      is caught.");
      logger.info(
          "      Pretending we do not know what to do, it is thrown again");
      logger.info("      (to show what happens when a program crashes)");
      logger.info("#");
      throw ElementsException(e.what());
    }

    // Get the result and log it

    logger.info("#");
    logger.info("#     This is it folks! ");
    logger.info("#");

    /*
     * Here we might later introduce a standard mechanism to persist results
     */

  }

  /*
   * This is a standard implementation of getVersion()
   * This must be copy/paste in all programs
   */
  string getVersion() {
    return getVersionFromSvnKeywords(SVN_URL, SVN_ID);
  }
};

/*
 * Implementation of a main using a base class macro
 * This must be copy/paste in all programs
 */
MAIN_FOR(ProtoZpdf)
