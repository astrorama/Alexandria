/**
 * @file FluxModeling.h
 * @date Dec 3, 2013
 * @author Nicolas Morisset
 */

#ifndef FLUXMODELING_H_
#define FLUXMODELING_H_

#include <map>
#include <memory>

#include "ChDataModel/Filter.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/VectorPair.h"
#include "ElementsKernel/ElementsException.h"

#include "ProtoZ/parameter/FluxModelingParameters.h"
#include "ProtoZ/Interpolation.h"
#include "ProtoZ/matrix/FluxMatrix.h"
#include "ProtoZ/InterpolationFactory.h"


using namespace ChDataModel;
using namespace ProtoZ::parameter;

static const double SPEED_LIGHT = 2.99792458e+18; // in Angstrom unit

class FluxModeling
{
 public:

  /**
   * @brief Constructor
   */

  FluxModeling(FluxModelingParameters* progParameters);

  virtual ~FluxModeling();

  /**
   * @brief
   * Computes the integrated fluxes and fills up a matrix
   *
   * @details
   * Following a set of Seds, Filters, extension laws and the reddening
   * a integrated flux is computed and stored into a matrix in memory
   * (see the Matrix class for more information on the storage)
   *
   * @return
   * A matrix with the integrated fluxes
   *
   */
  ProtoZ::matrix::FluxMatrix computeFluxMatrix();

  /**
   * @brief
   *   Apply the extinction model (K extension laws and reddening)
   *
   * @details
   *  it applies an extinction model and take account of the reddening
   *
   * @param wavelength : vector of wavelengths
   * @param intensity  : vector of intensity values
   * @param kExtension : vector of the extension law values
   * @param ebmv       : reddening value to be applied
   *
   * @return
   * vector of converted intensity values
   */
  std::vector<double> applyExtinctionLaw(
                                    const std::vector<double>& wavelength,
                                    const std::vector<double>& intensity,
                                    const std::vector<double>& kExtension,
                                    const double ebmv
                                    );

  /**
   * @brief
   *   Compute the full integration of the sed through the filter
   *
   * @details
   * Make the flux computation as described in the photoZalgo document, formula (1)
   *
   * @param filterResampledVPair : re-sampled filter information (wavelengths,
   *         efficiencies) in a VectorPair object
   * @param sedRedshiftedWavelengths : sed wavelengths redshifted
   * @param sedExtLawAppliedFluxes : sed fluxes with extension law applied
   * @param filterIntegral : filter integration (see also photoZalgo document, formula (1) )
   *
   * @return
   *  the value of the integrated flux.
   */
  double integrateSed(const VectorPair&           filterResampledVPair,
                      const std::vector<double>&  sedRedshiftedWavelengths ,
                      const std::vector<double>&  sedExtLawAppliedFluxes ,
                      const double                filterIntegral);
 /**
   * @brief
   *   Apply redshift to a vector of wavelengths
   *
   * @param redshift_step : the redshift step(aka z) to be applied
   * @param wavelength    : vector of wavelength values
   *
   * @return
   *  the wavelength values shifted
   */
  std::vector<double> applyRedshift(const double& redshift_step, const std::vector<double>& wavelength);


  /**
   * @brief
   *   Get the interpolation method used (CUBIC, LINEAR)
   *
   * @return method
   *  The interpolation method to be applied
   */
   std::string getInterpolationMethod() const { return m_method; }

   /**
    * @brief
    *  Compute the cubic simpson integratio
    *
    * @details
    *  It implements the so-called Simpson 3/8 rule of integration
    *
    * @param x_step   : value defining the regular step between 2 abscissa values
    * @param y_values : vector of the ordinate values to be integrated
    *
    * @return
    *  The result of the integration
    *
    * @throws ElementException
    *  can not achieve a cubic Simpson integration if the step number is not
    *  a multiple of 3
    */
   double simpsonCubicIntegration(const double x_step, const std::vector<double>& y_values) const;

   /**
    * @brief
    *  Resample FILTER or SED in order to have a regular step between wavelengths
    *
    * @details
    *  Resample FILTER or SED  in order to have a regular step between wavelengths
    *  and make sure the number of intervals is a multiple of 3 due to the
    *  Simpson integration. The fluxes are interpolated.
    *
    * @param wavelength : vector of wavelength values
    * @param flux       : vector of flux values
    *
    * @return
    *  A unique pointer of VectorPair which is the resampled wavelength values
    *  and the corresponding fluxes
    */
   std::unique_ptr<VectorPair> resample(const std::vector<double>& wavelength, const std::vector<double>& flux);

   /**
    * @brief
    * computer the filter integration specified in the photoZalgo document,
    * formula (1)
    *
    * @param filterVector : vector of unique pointers to the VectorPair object
    *
    * @return
    * vector containing the integration of each filter
    */
   std::vector<double> computeFilterIntegral(const std::vector<std::unique_ptr<VectorPair>>& filterVector);

   /**
    * @brief
    *  resample all filters
    *
    * @return
    * a unique pointer of VectorPair objects containing the filter
    * information (wavelengths, efficiencies)
    */
   std::vector<std::unique_ptr<VectorPair>> resampledAllFilters();

 private:

  void setup();

  std::unique_ptr<FluxModelingParameters> m_params;     /// Parameter object
  std::string                             m_method;     /// Interpolation method
  double                                  m_lambdaStep; /// Lambda step


};

#endif /* FLUXMODELING_H_ */
