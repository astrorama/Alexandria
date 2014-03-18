/*
 * ImportCosmosAscii_main.cpp
 *
 *
 *  Created on: Feb 12, 2013
 *      Author: Pavel Binko
 */

#include "ChDataHandling/ImportCosmosAscii.h"

#include "ChTools/Configuration.h"
#include "ElementsKernel/ElementsException.h"

#include <string>
#include <vector>
#include <fstream>
#include <iostream>

#include "ChDataModel/Survey.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"
#include "ChDataModel/Photometry.h"

#include "ChDataHandling/CosmosAsciiMapping.h"

#include <boost/program_options.hpp>

using namespace std;
using namespace ChDataModel;

namespace po = boost::program_options;

//-----------------------------------------------------------------------------

void printUsage() {
  cout << "ImportCosmosAscii\n"
      "\n"
      "Program to read the data from a COSMOS ASCII file\n"
      "\n"
      "Input parameter : COSMOS ASCII file name\n"
      "\n"
      "Usage: ImportCosmosAscii --FileName={full path COSMOS ASCII file name}\n"
      "or"
      "Usage: ImportCosmosAscii {full path COSMOS ASCII file name}\n";
  cout << endl;
} // Eof PrintUsage

//-----------------------------------------------------------------------------

int setupConfiguration(Configuration &conf, int argc, const char* argv[]) {

  po::options_description control("Import COSMOS ASCII control");
  conf.setPrintUsage(printUsage);

  control.add_options()("DataSetName", var<string>("DefaultValue"),
      "Data set name, e.g. COSMOS") // default_value "DefaultValue", if prog (--DataSetVersion absent)
  ("DataSetVersion", var<int64_t>()->implicit_value(123),
      "Data set version, e.g. 2006") // implicit_value, if prog --DataSetVersion (=value absent)
  ("FileName", var<string>()->required(), "Input file name")   // Required
  ("Path", var<string>(), "PATH env");
  conf.addOptions(control);

  // Define, that "Path" can be taken from the environment variable PATH,
  //   if not defined with higher priority
  conf.addEnv("Path", "PATH");

  // For options with optional description
  po::positional_options_description p;
  p.add("DataSetName", 1); // The 1st positional option
  p.add("DataSetVersion", 2); // The 2nd positional option
  conf.setArgumentPositions(p);

  // Parse the options (returns <>0 if --help or --print-all, etc.)
  if (!conf.doParse(argc, argv)) {
    return 127;
  }

  // Check the options
  if (!conf.has("DataSetName")) {
    cout << "ERROR - --DataSetName missing." << endl;
    return 1;
  }

  return 0;

} // Eof SetupConfiguration

//-----------------------------------------------------------------------------

void printFromSurvey(Survey & surv) {

  cout << "##############################################\n";
  cout << "#\n";
  cout << "#    Print from survey" << endl;
  cout << "#\n";
  cout << "##############################################\n\n";

  // In survey

  cout << "In Survey : Survey name         = " << surv.getSurveyName() << endl;
  cout << "In Survey : Number of catalogs  = " << surv.getCatalogMap().size()
      << endl;

  // Loop over catalogs

  int catNr = 0;
  // it1 is a catalog iterator
  for (auto it1 = surv.getCatalogMap().begin();
      it1 != surv.getCatalogMap().end(); ++it1) {

    cout << "\n***** Catalog no. " << ++catNr
        << " *************************\n";
    cout << "In Catalog : Survey name         = "
        << it1->second.getSurveyPtr()->getSurveyName() << endl;
    cout << "In Catalog : Number of sources   = "
        << it1->second.getSourceMap().size() << endl;

    int srcNr = 0;
    // it2 is a source iterator
    for (auto it2 = it1->second.getSourceMap().begin();
        it2 != it1->second.getSourceMap().end(); ++it2) {

      cout << "\n===== Source no. " << ++srcNr
          << " =========================\n";
      cout << "In Source : Source ID    = " << it2->second.getSourceId()
          << endl;
      cout << "In Source : RA           = " << it2->second.getRa() << endl;
      cout << "In Source : DEC          = " << it2->second.getDec() << endl;

      int photNr = 0;
      // it3 is a photometry iterator
      for (auto it3 = it2->second.getPhotometryMap().begin();
          it3 != it2->second.getPhotometryMap().end(); ++it3) {

        cout << "----- Photometry no. " << ++photNr << " ---------\n";
        cout << "In Photometry : FilterName  = " << it3->second.getFilterName()
            << endl;
        cout << "In Photometry : Value       = " << it3->second.getValue()
            << endl;
        cout << "In Photometry : Value error = " << it3->second.getValueError()
            << endl;

      } // Eof for (photometry)

    } // Eof for (sources)

    cout
        << "***** End of Catalog *************************\n\n";

  } // Eof for(catalogs)

  cout
      << "##### End of printout ########################\n\n\n";

} // Eof printFromSurvey

//#############################################################################

void printFromSurveyItr(Survey & surv) {

  cout << "##############################################\n";
  cout << "#\n";
  cout << "#    Print from survey" << endl;
  cout << "#\n";
  cout << "##############################################\n\n";

  // In survey

  cout << "In Survey : Survey name         = " << surv.getSurveyName() << endl;
  cout << "In Survey : Number of catalogs  = " << surv.getCatalogMap().size()
      << endl;

  // Loop over catalogs

  int catNr = 0;
  // it1 is a catalog iterator
  for (Survey::CatalogIterator it1 = surv.catalogBegin(); it1 != surv.catalogEnd(); ++it1) {

    cout << "\n***** Catalog no. " << ++catNr
        << " *************************\n";
    cout << "In Catalog : Survey name         = "
        << it1->getSurveyPtr()->getSurveyName() << endl;

    cout << "In Catalog : Number of sources   = " << it1->size() << endl;

    int srcNr = 0;
    // it2 is a source iterator
    for (Catalog::SourceIterator it2 = it1->begin(); it2 != it1->end(); ++it2) {

      cout << "\n===== Source no. " << ++srcNr
          << " =========================\n";
      cout << "In Source : Source ID    = " << it2->getSourceId() << endl;
      cout << "In Source : RA           = " << it2->getRa() << endl;
      cout << "In Source : DEC          = " << it2->getDec() << endl;

      int photNr = 0;
      // it3 is a photometry iterator
      for (Source::PhotometryIterator it3 = it2->begin(); it3 != it2->end(); ++it3) {

        cout << "----- Photometry no. " << ++photNr << " ---------\n";
        cout << "In Photometry : FilterName  = " << it3->getFilterName()
            << endl;
        cout << "In Photometry : Value       = " << it3->getValue() << endl;
        cout << "In Photometry : Value error = " << it3->getValueError()
            << endl;

      } // Eof for (photometry)

    } // Eof for (sources)

    cout
        << "***** End of Catalog *************************\n\n";

  } // Eof for(catalogs)

  cout
      << "##### End of printout ########################\n\n\n";

} // Eof printFromSurveyItr

//#############################################################################

void printFromSurveyMemberFunction(Survey & surv) {

  surv.printSurvey();

} // Eof printFromSurveyItr

//#############################################################################

int main(int argc, const char* argv[]) {

  Configuration conf(argv[0]);
  int setup = setupConfiguration(conf, argc, argv);

  if (setup != 0) {
    cout << "Setup configuration return code : " << setup << endl;
    return 127;
  }

  //===========================================================================

  try {

    cout
        << "##########################################################################\n";
    cout << "#\n";
    cout << "#    In the try block, getSource test" << endl;
    cout << "#\n";
    cout
        << "##########################################################################\n";

    // Print all input parameters
    conf.printOptions();

    // Get all input parameters
    string fileName = conf.get<string>("FileName");
    string dataSetName = conf.get<string>("DataSetName");
//    int64_t dataSetVersion = conf.get<int64_t>("DataSetVersion");
//    string path = conf.get<string>("Path");

    //=========================================================================
    // Create the importer

    cout
        << "-------------------------------------------------------------------------\n\n";

    IImport* input;

    if ("COSMOS" == dataSetName) {
      cout << "Create the COSMOS ASCII Importer" << endl << endl;
      input = new ImportCosmosAscii(fileName);
    }
    else if ("VVDS" == dataSetName) {
      cout << "Create the VVDS Importer" << endl << endl;
      cout << "Apologies, the VVDS Importer is currently not available" << endl
          << endl;
      return 1;
    }
    else {
      cout << "No - I cannot read such a data set" << endl << endl;
      return 1;
    }

    //-------------------------------------------------------------------------
    // Create the survey

    Survey surv(dataSetName);

    //-------------------------------------------------------------------------
    // Create new empty catalog, attached to the survey

    Catalog & catInSurv = surv.createCatalog();
//    Catalog & catInSurv222 = surv.createCatalog();

    //-------------------------------------------------------------------------
    // Create all sources and attach them into the catalog

    while (true == input->createSource(catInSurv)) {
    }

    //-------------------------------------------------------------------------
    // Print the results

    printFromSurvey(surv);

    //-------------------------------------------------------------------------
    // Clean up

    delete input;

  } // Eof try
  catch (const ElementsException & e) {
    cout << "Euclid exception caught : " << e.what() << endl;
  }
  catch (const std::exception & e) {
    cout << "std::exception caught : " << e.what() << endl;
  }
  catch (...) {
    cout << "Unknown exception caught : " << endl;
  }

  //===========================================================================

  try {

    cout
        << "##########################################################################\n";
    cout << "#\n";
    cout << "#    In the try block, getCatalog test" << endl;
    cout << "#\n";
    cout
        << "##########################################################################\n";

    // Print all input parameters
    conf.printOptions();

    // Get all input parameters
    string fileName = conf.get<string>("FileName");
    string dataSetName = conf.get<string>("DataSetName");
//    int64_t dataSetVersion = conf.get<int64_t>("DataSetVersion");
//    string path = conf.get<string>("Path");

    //=========================================================================
    // Create the importer

    cout
        << "-------------------------------------------------------------------------\n\n";

    IImport* input;

    if ("COSMOS" == dataSetName) {
      cout << "Create the COSMOS ASCII Importer" << endl << endl;
      input = new ImportCosmosAscii(fileName);
    }
    else if ("VVDS" == dataSetName) {
      cout << "Create the VVDS Importer" << endl << endl;
      cout << "Apologies, the VVDS Importer is currently not available" << endl
          << endl;
      return 1;
    }
    else {
      cout << "No - I cannot read such a data set" << endl << endl;
      return 1;
    }

    //-------------------------------------------------------------------------
    // Create the survey

    Survey surv(dataSetName);

    //-------------------------------------------------------------------------
    // Create new catalog, attached to the survey, containing all sources

    bool b = input->createCatalog(surv);
    if (false == b) {
      delete input ;
      throw ElementsException("main : Create catalog failed.");
    }

    //-------------------------------------------------------------------------
    // Print the results

    printFromSurveyItr(surv);

    //-------------------------------------------------------------------------
    // Clean up

    delete input;

  } // Eof try
  catch (const ElementsException & e) {
    cout << "Euclid exception caught : " << e.what() << endl;
  }
  catch (const std::exception & e) {
    cout << "std::exception caught : " << e.what() << endl;
  }
  catch (...) {
    cout << "Unknown exception caught : " << endl;
  }

  //===========================================================================

  try {

    cout
        << "##########################################################################\n";
    cout << "#\n";
    cout << "#    In the try block, short source code test" << endl;
    cout << "#\n";
    cout
        << "##########################################################################\n";

    // Print all input parameters
    conf.printOptions();

    // Get all input parameters
    string fileName = conf.get<string>("FileName");
    string dataSetName = conf.get<string>("DataSetName");
//    int64_t dataSetVersion = conf.get<int64_t>("DataSetVersion");
//    string path = conf.get<string>("Path");

    //=========================================================================
    // Create the importer

    cout
        << "-------------------------------------------------------------------------\n\n";

    //-------------------------------------------------------------------------
    // Create the survey

    Survey surv(dataSetName);

    //-------------------------------------------------------------------------
    // Create the importer and fill it with the data (in the constructor)


    if ("COSMOS" == dataSetName) {
      cout << "Create the COSMOS ASCII Importer" << endl << endl;
      ImportCosmosAscii input(fileName, surv);
    }
    else if ("VVDS" == dataSetName) {
      cout << "Create the VVDS Importer" << endl << endl;
      cout << "Apologies, the VVDS Importer is currently not available" << endl
          << endl;
      return 1;
    }
    else {
      cout << "No - I cannot read such a data set" << endl << endl;
      return 1;
    }

    //-------------------------------------------------------------------------
    // Print the results

    printFromSurveyMemberFunction(surv);

    //-------------------------------------------------------------------------
    // Clean up

  } // Eof try
  catch (const ElementsException & e) {
    cout << "Euclid exception caught : " << e.what() << endl;
  }
  catch (const std::exception & e) {
    cout << "std::exception caught : " << e.what() << endl;
  }
  catch (...) {
    cout << "Unknown exception caught : " << endl;
  }

  return 0;

} // Eof main()
