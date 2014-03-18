/** 
 * @file OutputFactory.h
 * @date December 23, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef OUTPUTFACTORY_H
#define	OUTPUTFACTORY_H

#include <string>
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include "ProtoZ/output/FluxModelingOutput.h"
#include "ProtoZ/output/CombinedFluxModelingOutput.h"
#include "ProtoZ/output/BinaryFluxModelingOutput.h"
#include "ProtoZ/output/AsciiFluxModelingOutput.h"

namespace ProtoZ {
namespace output {

ElementsLogging logger = ElementsLogging::getLogger("ProtoZ.output");

class OutputFactory {
  
public:
  
  static std::unique_ptr<FluxModelingOutput> getFluxModelingOutputHandler(po::variables_map options) {
    std::vector<std::shared_ptr<FluxModelingOutput>> handlers {};
    if (!options["binary-output-path"].empty() && !options["binary-output-path"].as<std::string>().empty()) {
      std::string filename = options["binary-output-path"].as<std::string>();
      logger.info("OutputFactory::getFluxModelingOutputHandler : Adding binary "
          "output handler for file %s", filename.c_str());
      handlers.push_back(std::shared_ptr<FluxModelingOutput>{
                                     new BinaryFluxModelingOutput {filename} });
    }
    if (!options["ascii-output-path"].empty() && !options["ascii-output-path"].as<std::string>().empty()) {
      std::string filename = options["ascii-output-path"].as<std::string>();
      logger.info("OutputFactory::getFluxModelingOutputHandler : Adding ASCII "
          "output handler for file %s", filename.c_str());
      handlers.push_back(std::shared_ptr<FluxModelingOutput>{
                                     new AsciiFluxModelingOutput {filename} });
    }
    if (handlers.empty()) {
      logger.warn("Flux modeling is executed without any output options. All "
                  "calculations will be lost.");
    }
    return std::unique_ptr<FluxModelingOutput>{new CombinedFluxModelingOutput {handlers}};
  }
  
};

} /* namespace output */
} /* namespace ProtoZ */

#endif	/* OUTPUTFACTORY_H */

