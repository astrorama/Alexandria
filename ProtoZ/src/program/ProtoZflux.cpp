/**
 * @file ProtoZflux.cpp
 * @date Nov 28, 2013
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

#include "ProtoZ/parameter/FluxModelingParameters.h"
namespace param = ProtoZ::parameter;
#include "ProtoZ/matrix/FluxMatrix.h"
#include "ProtoZ/matrix/serialize.h"
#include "ProtoZ/matrix/MatrixAsciiExporter.h"
#include "ProtoZ/FluxModeling.h"
namespace matrix = ProtoZ::matrix;
#include "ProtoZ/output/OutputFactory.h"
#include "ProtoZ/output/FluxModelingOutput.h"
namespace output = ProtoZ::output;


using namespace std;

/**
 * @class ElementsProgramExample
 * @brief
 * 		Example of an Elements program
 * @details
 * 		This class is an example of a program based on the ElementsProgram class. It can be copied/pasted
 * 		conveniently to write a new program.
 */
class ProtoZflux: public ElementsProgram {

public:

  /**
   * @brief Constructor
   */
  ProtoZflux() {
  }

  /**
   * @brief Destructor
   */
  virtual ~ProtoZflux() {
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
    ("binary-output-path", po::value<string>()->default_value(string { }),
     "The file where the Flux matrix will be stored in binary format")
    ("ascii-output-path", po::value<string>()->default_value(string { }),
     "The file where the Flux matrix will be stored in ascii format")
    // A example string option
    ("sed-dir-path", po::value<string>()->default_value(string { }),
     "The SED directory path")
    // A example string option
    ("filter-dir-path", po::value<string>()->default_value(string { }),
     "The Filter directory path")
    // A example string option
    ("red-law-dir-path", po::value<string>()->default_value(string { }),
     "The Reddening law directory path")
    // A double option
    ("z-start", po::value<double>()->default_value(double { }),
     "The redshift range lower limit")
    // A double option
    ("z-step", po::value<double>()->default_value(double { }),
     "The redshift step")
    // A double option
    ("z-stop", po::value<double>()->default_value(double { }),
     "The redshift range upper limits")
    // A double option
    ("ebmv-start", po::value<double>()->default_value(double { }),
     "The E(B-V) range lower limit")
    // A double option
    ("ebmv-step", po::value<double>()->default_value(double { }),
     "The E(B-V) step")
    // A double option
    ("ebmv-stop", po::value<double>()->default_value(double { }),
     "The E(B-V) range upper limits")
    // A double option
    ("lambda-interpolation-step", po::value<double>()->default_value(double { }),
     "The wavelength interpolation step")
    // A example long int option
    ("interpolation-type", po::value<std::string>()->default_value(std::string { }),
     "Type of the polynomial function used for the interpolation");

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
    ElementsLogging& logger = ElementsLogging::getLogger();

    logger.info("#");
    logger.info(
        "#  Logging from the mainMethod() of the ProtoZflux ");
    logger.info("#");

    // Get the required input parameters according the program options given by
    // the user. Note that the FluxModeling is taking ownership of the parameters
    // pointer and handles its deletion.
    const po::variables_map variables_map = this->getVariablesMap();
    param::FluxModelingParameters* fmp = new param::FluxModelingParameters{variables_map};
    
    FluxModeling fluxModeling {fmp};
    matrix::FluxMatrix fluxMatrix = fluxModeling.computeFluxMatrix();
    
    auto fmo = output::OutputFactory::getFluxModelingOutputHandler(variables_map);
    fmo->outputFluxMatrix(fluxMatrix);

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
MAIN_FOR(ProtoZflux)
