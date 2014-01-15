/*
 * ProgramOptions_CommandLine_2_only.cpp
 *
 *
 *  Created on: Feb 12, 2013
 *      Author: Pavel Binko
 */

#include "ChDataHandling/ImportCosmosAscii.h"
#include "ChDataHandling/Factory.h"

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
namespace po = boost::program_options;

using namespace std;
using namespace ChDataModel;

//-----------------------------------------------------------------------------

int setupProgramOptions(int argc, const char* argv[], po::variables_map & vm) {

  po::options_description desc("Allowed options");
  desc.add_options()
      ("help",           "produce help message")
      ("DataSetName",    po::value<string>()->default_value("COSMOS"), "Data set name, e.g. COSMOS")
      ("DataSetVersion", po::value<int64_t>()->default_value(2006), "Data set version, e.g. 2006")
      ("FileName",       po::value<string>()->default_value("PhotometryData/Cosmos"), "Input file name");

  po::store(po::parse_command_line(argc, argv, desc), vm);
  po::notify(vm);

  // If the program option --help is present, print the test and return
  if (vm.count("help")) {
    cout << desc << "\n";
    exit(1);
  }

  // If the program option --FileName is not present, exit
  if (!vm.count("FileName")) {
    cout << "The required program option FileName is missing\n";
    exit(1);
  }

  return 0;

} // Eof SetupConfiguration
//#############################################################################

int main(int argc, const char* argv[]) {

  try {

    cout << "##########################################################\n";
    cout << "#\n";
    cout << "#    ProgramOptions_CommandLine_2_only : In the try block" << endl;
    cout << "#\n";
    cout << "##########################################################\n";

    // The map with all variables (of different types)
    po::variables_map vm;

    setupProgramOptions(argc, argv, vm);

    // Retrieve the values from the po::variables_map
    string fileName = vm["FileName"].as<string>();
    string dataSetName = vm["DataSetName"].as<string>();
    int64_t dataSetVersion = vm["DataSetVersion"].as<int64_t>();

    cout << "\nProgram options\n";
    cout << "FileName        = " << fileName << endl;
    cout << "DataSetName     = " << dataSetName << endl;
    cout << "DataSetVersion  = " << dataSetVersion << "\n\n\n";

    cout << "----------------------------------------------------------\n\n";

    //-------------------------------------------------------------------------
    // Create the survey and a catalog in it

    Survey * surv = Factory::createSurvey(dataSetName);
    Factory::createCatalogInSurvey(surv, fileName, 3, 1);

    //-------------------------------------------------------------------------
    // Print the results

    surv->printCatalogsInSurvey();

    //-------------------------------------------------------------------------
    // Clean up

    delete surv;

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
