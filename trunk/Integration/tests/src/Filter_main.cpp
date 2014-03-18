/*
 * Fliter_main.cpp
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

#include "ChDataModel/Filter.h"

#include "ChDataHandling/CosmosAsciiMapping.h"
#include "ChDataHandling/Factory.h"

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

  control.add_options()
      ("DataSetName", var<string>("DefaultValue"), "Data set name, e.g. COSMOS") // default_value "DefaultValue", if prog (--DataSetVersion absent)
      ("FileName", var<string>("blabla"), "Input file name");
//      ("FileName", var<string>()->required(), "Input file name");
  conf.addOptions(control);

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
    cout << "#    In the try block, short source code test" << endl;
    cout << "#\n";
    cout
        << "##########################################################################\n";

    // Print all input parameters
    conf.printOptions();

    // Get all input parameters
    string fileName = conf.get<string>("FileName");
    string dataSetName = conf.get<string>("DataSetName");

    // Create survey
    Survey* survey = Factory::createSurvey(dataSetName);

    // Create filters in survey
    Factory::createFiltersInSurvey(survey, fileName, ChDataModel::FilterTypes::EUCLID);

    // Print filters
    survey->printFiltersInSurvey();


  } // Eof try
  catch (const ElementsException & e) {
    cout << "Euclid exception caught : " << e.what() << endl;
  } catch (const std::exception & e) {
    cout << "std::exception caught : " << e.what() << endl;
  } catch (...) {
    cout << "Unknown exception caught : " << endl;
  }

  return 0;

} // Eof main()
