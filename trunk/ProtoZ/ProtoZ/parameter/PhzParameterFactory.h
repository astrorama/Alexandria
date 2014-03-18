/** 
 * @file ParameterFactory.h
 * @date November 29, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef PARAMETERFACTORY_H
#define	PARAMETERFACTORY_H

#include <memory>
#include <string>
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include "ChDataModel/Sed.h"
#include "ChDataModel/Enumerations/SedNames.h"
#include "ChDataModel/Filter.h"
#include "ChDataModel/Enumerations/FilterNames.h"
namespace dm = ChDataModel;
#include "ProtoZ/parameter/PhzParameter.h"
#include "ProtoZ/parameter/PhzDataParameter.h"

namespace ProtoZ {
namespace parameter {

/**
 * @class PhzParameterFactory
 * @brief
 *      Factory class for creating PHZ parameter objects
 * @details
 *      The main factory method of the PhzParameterFactory class is the method
 *      PhzParameterFactory::createPhzParameterSet() which constructs a complete
 *      set of PHZ algorithm parameters, based on the options given. The rest
 *      of the factories are specific cases for the parameters which are used
 *      by the createPhzParameterSet method. They can always used though as
 *      stand alone factory methods for individual parameter objects (for example
 *      for testing).
 */
class PhzParameterFactory {

public:
  
  /**
   * @brief
   *    Creates a parameter describing the SEDs based on the program options
   *    given as parameter.
   * @details
   *    This method is responsible for recognizing from the options the way to
   *    get the SEDs and to delegate the PhzParameter construction to the
   *    correct method.
   *    The currently supported SED parameter types are:
   *    - Options: sed-dir-path (string)
   *      SED ASCII files in a directory
   * 
   * @param options
   *    The program options
   * @return
   *    A PhzParameter representing the SEDs
   * @throws
   *    ElementsException, if the given options do not describe any supported type
   */
  static std::unique_ptr<PhzDataParameter<dm::SedNames, dm::Sed> > createSedsParameter(po::variables_map options);
  
  /**
   * @brief
   *    Creates a parameter describing the filters based on the program options
   *    given as parameter.
   * @details
   *    This method is responsible for recognizing from the options the way to
   *    get the filters and to delegate the PhzParameter construction to the
   *    correct method.
   *    The currently supported filter parameter types are:
   *    - Options: filter-dir-path (string)
   *      Filter ASCII files in a directory
   * 
   * @param options
   *    The program options
   * @return
   *    A PhzParameter representing the filters
   * @throws
   *    ElementsException, if the given options do not describe any supported type
   */
  static std::unique_ptr<PhzDataParameter<dm::FilterNames, dm::Filter> > createFiltersParameter(po::variables_map options);
  
  /**
   * @brief
   *    Creates a parameter describing the extinction laws based on the program options
   *    given as parameter.
   * @details
   *    This method is responsible for recognizing from the options the way to
   *    get the extinction laws and to delegate the PhzParameter construction to the
   *    correct method.
   *    The currently supported extinction law parameter types are:
   *    - Options: red-law-dir-path (string)
   *      Extinction law ASCII files in a directory
   * 
   * @param options
   *    The program options
   * @return
   *    A PhzParameter representing the extinction laws
   * @throws
   *    ElementsException, if the given options do not describe any supported type
   */
  static std::unique_ptr<PhzDataParameter<std::string, dm::VectorPair> > createExtLawsParameter(po::variables_map options);
  
  /**
   * @brief
   *    Creates a parameter describing the E(B-V) values based on the program options
   *    given as parameter.
   * @details
   *    This method is responsible for recognizing from the options the way to
   *    get the E(B-V) values and to delegate the PhzParameter construction to the
   *    correct method.
   *    The currently supported E(B-V) parameter types are:
   *    - Options: ebmv-start, ebmv-stop, ebmv-step (all doubles)
   *      Values in a range, with a fixed distance
   * 
   * @param options
   *    The program options
   * @return
   *    A PhzParameter representing the E(B-V) values
   * @throws
   *    ElementsException, if the given options do not describe any supported type
   */
  static std::unique_ptr<PhzParameter<double> > createEbvsParameter(po::variables_map options);
  
  /**
   * @brief
   *    Creates a parameter describing the redshift values based on the program options
   *    given as parameter.
   * @details
   *    This method is responsible for recognizing from the options the way to
   *    get the redshift values and to delegate the PhzParameter construction to the
   *    correct method.
   *    The currently supported redshift parameter types are:
   *    - Options: z-start, z-stop, z-step (all doubles)
   *      Values in a range, with a fixed distance
   * 
   * @param options
   *    The program options
   * @return
   *    A PhzParameter representing the redshift values
   * @throws
   *    ElementsException, if the given options do not describe any supported type
   */
  static std::unique_ptr<PhzParameter<double> > createZsParameter(po::variables_map options);
  
  /**
   * @brief
   *    Creates a double PHZ parameter of fixed step
   * @details
   *    Creates a PHZ parameter object which has values in the range [start,stop]
   *    with the fixed given step. It is the responsibility of the caller to do
   *    the memory management for the returned object.
   * 
   * @param name
   *    The name of the parameter
   * @param start
   *    The starting value of the parameter
   * @param stop
   *    The stopping value of the parameter
   * @param step
   *    The step between the parameter values
   * @return
   *    A pointer to the double PHZ parameter
   */
  static std::unique_ptr<PhzParameter<double> > createFixedStepParameter(const std::string& name, double start, double stop, double step);
  
  /**
   * @brief
   *    Creates a SED parameter for the SEDs contained in the given directory
   * @param directory
   *    The directory containing the SEDs
   * @return 
   *    The SED parameter
   */
  static std::unique_ptr<PhzDataParameter<dm::SedNames, dm::Sed> > createSedParameterFromPath(std::string directory);
  
  /**
   * @brief
   *    Creates a filter parameter for the filters contained in the given directory
   * @param directory
   *    The directory containing the filters
   * @return 
   *    The filter parameter
   */
  static std::unique_ptr<PhzDataParameter<dm::FilterNames, dm::Filter> > createFilterParameterFromPath(std::string directory, dm::FilterTypes type);
  
  /**
   * @brief
   *    Creates a extinction law parameter for the extinction laws contained in the given directory
   * @param directory
   *    The directory containing the extinction laws
   * @return 
   *    The extinction law parameter
   */
  static std::unique_ptr<PhzDataParameter<std::string, dm::VectorPair> > createExtLawParameterFromPath(std::string directory);

private:

  /**
   * Private default constructor to not allow instantiation of the class
   */
  PhzParameterFactory() { }

};

} /* namespace parameter */
} /* namespace ProtoZ */

#endif	/* PARAMETERFACTORY_H */

