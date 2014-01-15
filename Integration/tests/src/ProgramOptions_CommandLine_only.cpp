/*
 * ProgramOptions_CommandLine_only.cpp
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

//#############################################################################

int main(int argc, const char* argv[]) {

  try {

    cout << "##########################################################\n";
    cout << "#\n";
    cout << "#    ProgramOptions_CommandLine_only : In the try block" << endl;
    cout << "#\n";
    cout << "##########################################################\n";

    // First way how to get the values of the program options is
    // to put them as parameters of the function po::value<>()
    string defaultDataSetName       = "blabla";
    int64_t implicitDataSetVersion  = -99;
    string requiredFileName         = "blabla";

    po::options_description desc("Allowed options");
    desc.add_options()
        ("help",           "produce help message")
        ("DataSetName",    po::value<string>(&defaultDataSetName)->default_value("DefaultValue"), "Data set name, e.g. COSMOS") // default_value "DefaultValue", if prog (--DataSetVersion absent)
        ("DataSetVersion", po::value<int64_t>(&implicitDataSetVersion)->implicit_value(123), "Data set version, e.g. 2006") // implicit_value, if prog --DataSetVersion (=value absent)
        ("FileName",       po::value<string>(&requiredFileName)->required(), "Input file name");   // Required

    // The map with all variables (of different types)
    po::variables_map vm;
    // Parse the command line
    po::store(po::parse_command_line(argc, argv, desc), vm);
    // Raises any errors encountered, e.g. for required variables
    po::notify(vm);

    // The program options are available after the execution
    // of the function po::parse_command_line() :

    // If the program option --help is present, print the test and return
    if (vm.count("help")) {
      cout << desc << "\n";
      return 0;
    }

    cout << "After parse " << endl;
    cout << "defaultDataSetName     = " << defaultDataSetName << endl;
    cout << "implicitDataSetVersion = " << implicitDataSetVersion << endl;
    cout << "requiredFileName       = " << requiredFileName << endl << endl;

    // The other way how to get the values of the program options is
    // to retrieve them from the po::variables_map :
    string fileName = vm["FileName"].as<string>();
    string dataSetName = vm["DataSetName"].as<string>();
    int64_t dataSetVersion = vm["DataSetVersion"].as<int64_t>();

    cout << "From the po::variables_map " << endl;
    cout << "FileName        = " << fileName << endl;
    cout << "DataSetName     = " << dataSetName << endl;
    cout << "DataSetVersion  = " << dataSetVersion << endl << endl << endl;

    // The presence of values can be enforced by the functions :
    //   - po::value<>()->default_value
    //   - po::value<>()->implicit_value
    //   - po::value<>()->required

    // The presence of the values can be checked also e.g. :
    if (vm.count("DataSetName")) {
      cout << "DataSetName was set to " << vm["DataSetName"].as<string>() << endl;
    }
    else {
      cout << "DataSetName was not set." << endl;;
    }

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
