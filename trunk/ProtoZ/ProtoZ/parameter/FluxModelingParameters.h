/**
 * @file FluxModelingParameters.h
 * @date Nov 28, 2013
 * @author Pierre Dubath
 */
#ifndef FLUXMODELINGPARAMETERS_H_
#define FLUXMODELINGPARAMETERS_H_

#include <string>
#include <memory>
#include <boost/program_options.hpp>
namespace po = boost::program_options;
#include "ProtoZ/parameter/PhzParameterFactory.h"
#include "ProtoZ/parameter/PhzDataParameter.h"
#include "ProtoZ/parameter/PhzParameter.h"

namespace ProtoZ {
namespace parameter {

class FluxModelingParameters {

public:
  
  FluxModelingParameters(std::unique_ptr<PhzParameter<double> > zs,
                         std::unique_ptr<PhzParameter<double> > ebvs,
                         std::unique_ptr<PhzDataParameter<dm::SedNames, dm::Sed> > seds,
                         std::unique_ptr<PhzDataParameter<dm::FilterNames, dm::Filter> > filters,
                         std::unique_ptr<PhzDataParameter<std::string, dm::VectorPair> > ext_laws,
                         const double lambda_interpolation_step,
                         const std::string interpolation_poly_degree)
      : m_zs{std::move(zs)}, m_ebvs{std::move(ebvs)}, m_seds{std::move(seds)},
        m_filters{std::move(filters)}, m_ext_laws{std::move(ext_laws)},
        m_lambda_interpolation_step{lambda_interpolation_step},
        m_interpolation_poly_degree{interpolation_poly_degree} { }

  FluxModelingParameters(const po::variables_map& options)
      : FluxModelingParameters{
            PhzParameterFactory::createZsParameter(options),
            PhzParameterFactory::createEbvsParameter(options),
            PhzParameterFactory::createSedsParameter(options),
            PhzParameterFactory::createFiltersParameter(options),
            PhzParameterFactory::createExtLawsParameter(options),
            options["lambda-interpolation-step"].as<double>(),
            options["interpolation-type"].as<std::string>()
        } { }

  virtual ~FluxModelingParameters() {}

  
  /**
   * Returns a reference to the parameter describing the redshift.
   * @return The redshift parameter
   */
  const PhzParameter<double>& getZs() const {
    return *(m_zs.get());
  }
  /**
   * Returns a reference to the parameter describing the reddening constant E(B-V)
   * @return The E(B-V) parameter
   */
  const PhzParameter<double>& getEbvs() const {
    return *(m_ebvs.get());
  }

  /**
   * Returns a reference to the parameter describing the SEDs
   * @return The SEDs parameter
   */
  const PhzDataParameter<dm::SedNames, dm::Sed>& getSeds() const {
    return *(m_seds.get());
  }

  /**
   * Returns a reference to the parameter describing the filters
   * @return The filters parameter
   */
  const PhzDataParameter<dm::FilterNames, dm::Filter>& getFilters() const {
    return *(m_filters.get());
  }

  /**
   * Returns a reference to the parameter describing the extinction laws
   * @return The extinction laws parameter
   */
  const PhzDataParameter<std::string, dm::VectorPair>& getExtLaws() const {
    return *(m_ext_laws.get());
  }

  std::string getInterpolationPolyDegree() const {
    return m_interpolation_poly_degree;
  }

  double getLambdaInterpolationStep() const {
    return m_lambda_interpolation_step;
  }

private:

  std::unique_ptr<PhzParameter<double> > m_zs;
  std::unique_ptr<PhzParameter<double> > m_ebvs;
  std::unique_ptr<PhzDataParameter<dm::SedNames, dm::Sed> > m_seds;
  std::unique_ptr<PhzDataParameter<dm::FilterNames, dm::Filter> > m_filters;
  std::unique_ptr<PhzDataParameter<std::string, dm::VectorPair> > m_ext_laws;
  const double m_lambda_interpolation_step;
  const std::string m_interpolation_poly_degree;

};

} /* namespace parameter */
} /* namespace ProtoZ */

#endif /* FLUXMODELINGPARAMETERS_H_ */
