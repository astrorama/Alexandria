/** 
 * @file ProtoZmarg.cpp
 * @date January 22, 2014
 * @author Nikolaos Apostolakos
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
#include <set>
#include <fstream>
#include <iostream>
// BOOST includes
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include <boost/filesystem.hpp>
namespace fs = boost::filesystem;
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
#include "ProtoZ/matrix/MatrixFitsExporter.h"
#include "ProtoZ/FluxToPdf.h"
namespace matrix = ProtoZ::matrix;

using namespace std;
using namespace ChDataModel;

/**
 * @class ProtoZmag
 * @brief
 * 		Example of an Elements program
 * @details
 * 		This class is an example of a program based on the ElementsProgram class. It can be copied/pasted
 * 		conveniently to write a new program.
 */
class ProtoZmag: public ElementsProgram {

public:

  /**
   * @brief Constructor
   */
  ProtoZmag() {
  }

  /**
   * @brief Destructor
   */
  virtual ~ProtoZmag() {
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
    // Path of the directory for the PDF output results
    ("pdf-output-dir", po::value<string>()->default_value(string { }),
        "Directory of the PDF output results")
    // Flag to produce binary output or not
    ("binary-output", po::value<bool>()->default_value(false),
        "Flag to produce binary output or not")
    // Flag to produce ASCII output or not
    ("ascii-table-output", po::value<bool>()->default_value(false),
        "Flag to produce ASCII table output or not")
    // Flag to produce FITS output or not
    ("fits-output", po::value<bool>()->default_value(false),
        "Flag to produce FITS output or not")
    ("source-id",
        po::value<vector<int>>()->multitoken()->default_value(vector<int> { },
            "Empty"), "The IDs of the sources to calculate the PDF for");

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
    ElementsLogging logger = ElementsLogging::getLogger("ProtoZmag");

    logger.info("#");
    logger.info("#  Logging from the mainMethod() of the ProtoZmag ");
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
    string pdf_output_dir = variables_map["pdf-output-dir"].as<string>();
    if (!fs::is_directory(pdf_output_dir)) {
      fs::create_directories(pdf_output_dir);
    }
    bool binary_output = variables_map["binary-output"].as<bool>();
    bool ascii_table_output = variables_map["ascii-table-output"].as<bool>();
    bool fits_output = variables_map["fits-output"].as<bool>();
    vector<int> source_id_vector = variables_map["source-id"].as<vector<int>>();
    set<int> source_id_set {source_id_vector.begin(), source_id_vector.end()};

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
      
      for (auto source : source_map) {
        if (source_id_set.find(source.second.getSourceId()) != source_id_set.end()) {
          ostringstream convert;
          convert << source.second.getSourceId();
          std::string sourceIdStr = convert.str();
          logger.info("Processing source with ID " + sourceIdStr);
          pdfMatrix = fluxToPdf.compute(source.second);
          
          std::vector<double> margValues = fluxToPdf.marginalizePdf(pdfMatrix);
          auto margMatrix = matrix::Matrix<double, double>(pdfMatrix.getZAxis());
          for (uint i = 0; i < margValues.size(); i++) {
            uint32_t coord[] = { i };
            margMatrix.setValue(coord, margValues[i]);
          }
          if (binary_output) {
            pdfMatrix.writeInFile(pdf_output_dir + "/" + sourceIdStr + "FullPDF.bin");
            matrix::writeMatrixInFile(pdf_output_dir + "/" + sourceIdStr + "MargPDF.bin", margMatrix);
          }
          if (ascii_table_output) {
            pdfMatrix.exportAsAscii(pdf_output_dir + "/" + sourceIdStr + "FullPDF.dat");
            matrix::MatrixAsciiExporter::exportMatrixAsAsciiFile(
                    pdf_output_dir + "/" + sourceIdStr + "MargPDF.dat", margMatrix);
          }
          if (fits_output) {
            pdfMatrix.exportAsFits(pdf_output_dir + "/" + sourceIdStr + "FullPDF.fits");
            matrix::MatrixFitsExporter::exportMatrixAsFitsFile(
                    pdf_output_dir + "/" + sourceIdStr + "MargPDF.fits", margMatrix);
          }
        }
      }

      logger.info("#");
      logger.info("#    The pdf calculation and result extraction is completed ");
      logger.info("#");

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
MAIN_FOR(ProtoZmag)
