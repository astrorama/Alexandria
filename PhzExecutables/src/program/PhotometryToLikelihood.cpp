/** 
 * @file PhotometryToLikelihood.cpp
 * @date May 23, 2014
 * @author Nikolaos Apostolakos
 */

#define SVN_ID "SVN $Id$"
#define SVN_URL "SVN $HeadURL$"

#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include "ElementsKernel/ElementsProgram.h"
#include "ElementsKernel/Version.h"

using namespace std;

class PhotometryToLikelihood : public ElementsProgram {
  
public:
  
  PhotometryToLikelihood() = default;
  
  virtual ~PhotometryToLikelihood() = default;
  
  po::options_description defineSpecificProgramOptions() {
    po::options_description config_file_options("PhotometryToLikelihood options");
    return config_file_options;
  }
  
  void mainMethod() {
    ElementsLogging logger = ElementsLogging::getLogger("PhotometryToLikelihood");
    logger.info() << "Hi";
  }
  
  string getVersion() {
    return getVersionFromSvnKeywords(SVN_URL, SVN_ID);
  }
  
}; //end of class PhotometryToLikelihood

MAIN_FOR(PhotometryToLikelihood)