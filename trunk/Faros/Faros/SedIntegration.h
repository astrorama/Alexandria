/**
 * SedIntegration.h
 *
 *  Created on: Sep 25, 2013
 *      Author : Nicolas Morisset
 */

#ifndef SEDINTEGRATION_H_
#define SEDINTEGRATION_H_

#include "ChDataModel/Filter.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/VectorPair.h"

#include "Faros/Interpolation.h"

using namespace ChDataModel;

class SedIntegration {
public:

  SedIntegration(const InterpolationMethod method, const unsigned short redshift_max=0, const double redshift_step=0.0)
                : m_method(method), m_redshift_max(redshift_max), m_redshift_step(redshift_step) {;}
  virtual ~SedIntegration();

  // todo temporary function for data storage
  void StoreDataInFile(const std::vector<double>& wavelengths,
                       const std::vector<double>& flux,
                       const std::string&         filename);

  /**
     * @brief
     *  Compute the cubic simmpson integration
     * @details
     *
     * @param x_step
     *   value defining the regular step between 2 abscissa values
     * @param y_values
     *   vector of the ordinate values you want to integrate
     *
     * @return
     *  The result of the integration
     *
     * @throws
     *  ElementException, cannot achieve a cubic Simpson integration if the step
     *                    number is not a multiple of 3
     */
  double simpsonCubicIntegration(const double x_step, const std::vector<double>& y_values) const;

  /**
     * @brief
     *  Giving a filter and a sed, it computes the integration of the fluxes
     *  as described in the following web page:
     *  http://www.asvo.org.au/blog/2013/03/21/derivation-of-ab-magnitudes/
     *  See the formula at the end of the web page for computing the magnitude.
     *  The integration is computed at any redshift requested.
     *
     * @details
     *  Note that the flux in erg/s/cm^2/A is "converted" in erg/s/cm^2/hz
     *
     * @param filter
     *  Is of Filter type  and contains all information about a filter
     *  ( wavelength(A), flux(erg/s/cm^2/A) )
     * @param sed
     *  Is of SED type and contains all information about a SED
     *  ( wavelength(A), flux(erg/s/cm^2/A) )
     *
     * @return
     *  A vector of the total integration of the flux ((in erg/s/cm/Hz) at any
     *  redshift (The flux integration is used for computing the magnitude)
     *
     * @throws
     *
     */
  std::vector<double> computeFlux(const Filter& filter, const Sed& sed);


  /**
   * @brief
   *  Compute the magnitude
   *
   * @details
   *  The integrated fluxes (in erg/s/cm/Hz) are supposed to come from the computeflux function
   *
   * @param integrated_flux
   *  vector of integrated fluxes
   *
   * @return
   *  Vector of magnitudes
   *
   * @throws
   *
   */
  std::vector<double>  computeMagnitude(const std::vector<double>& integrated_flux);


  /**
   * @brief
   *  Resample FILTER or SED in order to have a regular step between wavelengths
   *
   * @details
   *  Resample FILTER or SED  in order to have a regular step between wavelengths
   *  and make sure the number of intervals is a multiple of 3 due to the
   *  Simpson integration. The fluxes are interpolated.
   *
   * @param wavelength_orig
   *  Vector of wavelengths
   *
   * @param flux_orig
   *  Vector of fluxes
   *
   * @param step
   *  Regular interval between 2 wavelengths
   *
   * @return
   *  A pair of vectors which are the resampled wavelengths values and the
   *  corresponding fluxes
   *
   * @throws
   *
   */
  VectorPair* resampleFilterSed(const std::vector<double>& wavelength_orig, const std::vector<double>& flux_orig, const double step);


  /**
   * @brief
   *  Look for the minimum interval between values.
   *
   * @details
   *
   * @param step
   *  The step in an integer number of wavelength angstrom
   *
   * @return
   *  the minimum interval
   *
   * @throws
   *  ElementsException, "can not determine interval length, not enough values
   *                      (at least 2)!!!"
   */
   double  getMinimumInterval(const std::vector<double>& vector) const;

  /**
   * @brief
   *   Get the interpolation method used(cubic spline linear etc...)
   *
   * @details
   *
   * @param
   *  The step in an integer number of wavelength angstrom
   *
   * @return method
   *  value of InterpolationMethod type
   *
   * @throws
   *
   */
   InterpolationMethod getInterpolationMethod() const { return m_method; }


   /**
    * @brief
    *   Apply redshift to the vector of wavelengths
    *
    * @details
    *
    * @param redshift_step
    *  The redshift step to be apply
    *
    * @return vector of doubles
    *  wavelengths redshifted
    *
    * @throws
    *
    */
   std::vector<double>& applyRedshift(const double redshift_step, std::vector<double>& wavelength);

private:

    InterpolationMethod m_method;
    unsigned short      m_redshift_max;
    double              m_redshift_step;
};

#endif /* SEDINTEGRATION_H_ */
