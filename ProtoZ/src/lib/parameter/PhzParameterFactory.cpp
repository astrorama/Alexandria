/** 
 * @file ParameterFactory.cpp
 * @date November 29, 2013
 * @author Nikolaos Apostolakos
 */

#include <memory>
#include "ElementsKernel/ElementsException.h"
#include "ElementsKernel/ElementsLogging.h"
#include "ChDataHandling/AsciiSedImporter.h"
#include "ChDataHandling/AsciiFilterImporter.h"
#include "ChDataHandling/AsciiImporter.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/Enumerations/SedNames.h"
#include "ChDataModel/Filter.h"
#include "ChDataModel/Enumerations/FilterNames.h"
namespace dm = ChDataModel;
#include "ProtoZ/parameter/PhzParameterFactory.h"
#include "ProtoZ/parameter/VectorPhzParameter.h"
#include "ProtoZ/parameter/MapPhzDataParameter.h"

namespace ProtoZ {
namespace parameter {

ElementsLogging& logger = ElementsLogging::getLogger();

std::unique_ptr<PhzDataParameter<dm::SedNames, dm::Sed> > PhzParameterFactory::createSedsParameter(po::variables_map options) {
  if (!options["sed-dir-path"].empty()) {
    std::string path = options["sed-dir-path"].as<std::string>();
    logger.info("PhzParameterFactory::createSedsParameter : "
                "Using SED files in directory %s", path.c_str());
    return createSedParameterFromPath(path);
  }
  throw ElementsException {"Missing or unknown SED program options"};
}

std::unique_ptr<PhzDataParameter<dm::FilterNames, dm::Filter> > PhzParameterFactory::createFiltersParameter(po::variables_map options) {
  if (!options["filter-dir-path"].empty()) {
    std::string path = options["filter-dir-path"].as<std::string>();
    logger.info("PhzParameterFactory::createFiltersParameter : "
                "Using filter files in directory %s", path.c_str());
    return createFilterParameterFromPath(path, dm::FilterTypes::EUCLID);
  }
  throw ElementsException {"Missing or unknown filter program options"};
}

std::unique_ptr<PhzDataParameter<std::string, dm::VectorPair> > PhzParameterFactory::createExtLawsParameter(po::variables_map options) {
  if (!options["red-law-dir-path"].empty()) {
    std::string path = options["red-law-dir-path"].as<std::string>();
    logger.info("PhzParameterFactory::createExtLawsParameter : "
                "Using extinction law files in directory %s", path.c_str());
    return createExtLawParameterFromPath(path);
  }
  throw ElementsException {"Missing or unknown extinction law program options"};
}

std::unique_ptr<PhzParameter<double> > PhzParameterFactory::createEbvsParameter(po::variables_map options) {
  if (!options["ebmv-start"].empty() && !options["ebmv-stop"].empty() && !options["ebmv-step"].empty()) {
  double ebmv_start = options["ebmv-start"].as<double>();
  double ebmv_step = options["ebmv-step"].as<double>();
  double ebmv_stop = options["ebmv-stop"].as<double>();
    logger.info("PhzParameterFactory::createEbvsParameter : "
                "Using E(B-V) values in range [%g, %g] with step %g", ebmv_start, ebmv_stop, ebmv_step);
    return createFixedStepParameter("E(B-V)", ebmv_start, ebmv_stop, ebmv_step);
  }
  throw ElementsException {"Missing or unknown E(B-V) program options"};
}

std::unique_ptr<PhzParameter<double> > PhzParameterFactory::createZsParameter(po::variables_map options) {
  if (!options["z-start"].empty() && !options["z-stop"].empty() && !options["z-step"].empty()) {
  double z_start = options["z-start"].as<double>();
  double z_step = options["z-step"].as<double>();
  double z_stop = options["z-stop"].as<double>();
    logger.info("PhzParameterFactory::createZsParameter : "
                "Using redshift values in range [%g, %g] with step %g", z_start, z_stop, z_step);
    return createFixedStepParameter("Z", z_start, z_stop, z_step);
  }
  throw ElementsException {"Missing or unknown redshift program options"};
}

std::unique_ptr<PhzParameter<double> > PhzParameterFactory::createFixedStepParameter(const std::string& name, double start, double stop, double step) {
  std::vector<double> values{};
  while (start <= stop) {
    values.push_back(start);
    start += step;
  }
  return std::unique_ptr<PhzParameter<double> >(new VectorPhzParameter<double>{name, values});
}

std::unique_ptr<PhzDataParameter<dm::SedNames, dm::Sed> > PhzParameterFactory::createSedParameterFromPath(std::string directory) {
  AsciiSedImporter importer{};
  // Here we have to copy the returned map. This is because the importSeds method
  // returns a reference, so this object is going to be deleted after this method
  // exits.
  // TODO: Make the sed importer more efficient by avoiding all the map copying
  std::map<dm::SedNames, dm::Sed>* sedMap =
    new std::map<dm::SedNames, dm::Sed>(importer.importSeds(directory));
  return std::unique_ptr<PhzDataParameter<dm::SedNames, dm::Sed> >{new MapPhzDataParameter<dm::SedNames, dm::Sed>{"SED", sedMap}};
}

std::unique_ptr<PhzDataParameter<dm::FilterNames, dm::Filter> > PhzParameterFactory::createFilterParameterFromPath(std::string directory, dm::FilterTypes type) {
  AsciiFilterImporter importer{};
  // Here we have to copy the returned map. This is because the importFilters method
  // returns a reference, so this object is going to be deleted after this method
  // exits.
  // TODO: Make the filter importer more efficient by avoiding all the map copying
  std::map<dm::FilterNames, dm::Filter>* filterMap =
    new std::map<dm::FilterNames, dm::Filter>{importer.importFilters(directory, type)};
  return std::unique_ptr<PhzDataParameter<dm::FilterNames, dm::Filter> >{new MapPhzDataParameter<dm::FilterNames, dm::Filter>{"Filter", filterMap}};
}

std::unique_ptr<PhzDataParameter<std::string, dm::VectorPair> > PhzParameterFactory::createExtLawParameterFromPath(std::string directory) {
  // IMPORTANT: We do not have any generic reader of VectorPairs from a directory
  // (this should be done and be used for all sed, filter and ext law), neither a
  // extinction law specific class. As a hack (for the moment) the AsciiSedImporter
  // is used (it provides the importSedData method which is necessary).
  // TODO: THE ABOVE MESS MUST BE FIXED
  AsciiSedImporter importer{};
  std::map<std::string, dm::VectorPair>* result =
    new std::map<std::string, dm::VectorPair>{};
  importer.resolveFileNames(directory);
  for (auto filename : importer.getFileNames()) {
    std::string extLawName = filename.substr(filename.find_last_of('/') + 1);
    extLawName = extLawName.substr(0, extLawName.find_last_of('.'));
    importer.openFile(filename);
    dm::VectorPair data = importer.importSedData();
    result->insert(std::pair<std::string, dm::VectorPair>{extLawName, data});
    importer.closeCurrentFile();
  }
  return std::unique_ptr<PhzDataParameter<std::string, dm::VectorPair> >{new MapPhzDataParameter<std::string, dm::VectorPair>{"Ext_Law", result}};
}

} /* namespace parameter */
} /* namespace ProtoZ */
