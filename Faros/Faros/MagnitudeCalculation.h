/*
 * MagnitudeCalculation.h
 *
 *  Created on: Jun 17, 2013
 *      Author: Nicolas Morisset
 */

#ifndef MAGNITUDECALCULATION_H_
#define MAGNITUDECALCULATION_H_


#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>

//#include "ChDataModel/Catalog.h"
//#include "ChDataModel/Source.h"
//
#include "ChDataModel/Filter.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/VectorPair.h"
#include "ChTools/Constants.h"
#include "Faros/Point.h"

/**
 * @class MagnitudeCalculation.
 * @brief Compute magnitude by integrating SEDs though a set of filters
 */
class MagnitudeCalculation{

public:

  /**
   * @brief Constructor
   *   Initialize the data members
   */
  MagnitudeCalculation() : m_tolerence(0.0000000001) {};

  /**
   * @brief Destructor
   */
  virtual ~MagnitudeCalculation() {};

  /**
   * @brief linearInterpolation
   *   Realize a simple interpolation from two given points.
   * @details
   *   Two points of type Point are given to the function for making the line
   *   interpolation of point.
   *
   * @param[in]
   *   first_point  : this is the first necessary point (of type Point)
   *   second_point : this is the second necessary point (of type Point)
   *   abscissa     : abscissa of the point we look for the ordinate
   *
   * @throw Exception : Division by zero!
   *
   * @return double
   *         it returns the point ordinate corresponding to the abscissa given
   */

  double linearInterpolation(const Point& first_point,
                             const Point& second_point,
                                   double abscissa) const;

  /**
   * @brief convolutionIntegration
   *   Integrate of the convolution between SED and FILTER points using the
   *    simpson algorithm
   * @details
   *   The FILTER and SED ordinates respectively have the same abscissas.
   *
   * throw exception:
   *                 ExceptionFarosDivisionByZero
   *
   * @param[in]
   *
   *   filter_ordinate      : ordinate of a filter point
   *   filter_next_ordinate : ordinate of the next filter point
   *   sed_ordinate         : ordinate of of a sed point
   *   sed_next_ordinate    : ordinate of the next sed point
   *   lambda_mean          : lambda mean of the filter point abscissas
   *   delta_abscissa       : difference between the FILTER abscissas
   *
   * @throw Exception : Division by zero!
   *
   * @return double(1) double(2)
   *         (1) convolution integration
   *         (2) integration of the filter
   *
   */

  std::pair<double,double> convolutionIntegration(
                                      const double filter_ordinate,
                                      const double filter_next_ordinate,
                                      const double sed_ordinate,
                                      const double sed_next_ordinate,
                                      const double lambda_mean,
                                      const double delta_abscissa
                                                 ) const;


  /**
   * @brief getSedSubsetPoints
   *   Extract a subset of SED points to be considered for two
   *   FILTER points (abscissas)
   *
   * @details
   *
   *
   * @param[in]
   *   sed             : vector containing all SED points of one SED
   *   wavelength      : point of FILTER data
   *   wavelength_next : next point of the FILTER data
   *
   * @param[out]
   * sed_points_vector    : vector of SED points selected
   * filter_points_vector : vector of FILTER points selected
   *
   * @throw Exception : No SED points found in the filter
   * @throw Exception : SED index negative
   * @throw Exception : Not enough SED points
   * @throw Exception : SED and FILTER vectors have not the same size
   *
   * @return
   *
   */
  void getSedSubsetPoints(const ChDataModel::Sed&   sed,
                          const Point&              wavelength,
                          const Point&              wavelength_next,
                                std::vector<Point>& sed_points_vector,
                                std::vector<Point>& filter_points_vector) const;

  /**
   * @brief subsetIntegration
   * Compute the integration of a set of SED and FILTER points calling
   * the convolutionIntegration function
   *
   * @details
   * Compute the integration of a set of SED and FILTER points. The SED
   * and FILTER vectors must contain the same number of points
   *
   * @throw Exception : SED and FILTER vectors have not the same size
   *
   * @param[in]
   * sed_points_vector    : vector of SED points
   * filter_points_vector : vector of FILTER points
   *
   * @return double(1) double(2)
   *        (1) the integration of the convolution between the SED and FILTER
   *            points in sed_points_vector and filter_points_vector
   *        (2) the filter integration part of the filter_points_vector
   *            (needed for the computation of magnitude)
   */

  std::pair<double, double> subsetIntegration(
                                      std::vector<Point>& sed_points_vector,
                                      std::vector<Point>& filter_points_vector
                                             ) const;

  /**
   * @brief brokenLineIntegration
   *   Compute the full integration between a SED and a FILTER
   *   The SED units must be:
   *            Wavelength in Angstrom
   *            flux in ergs/s/cm^2/Angstrom
   *   The FILTER units must be:
   *            Wavelength in Angstrom
   *
   * @details
   *
   * @param[in]
   *   sed      : vector containing all SED points of one SED
   *   filter           : vector containing all FILTER points on one filter
   *
   * @return double(1) double(2)
   *         it returns the total integration of the full SED through the FILTER
   *         (1) full integration of the convolution
   *         (2) full integration of the filter
   */
  std::pair<double, double> brokenLineIntegration( ChDataModel::Sed&    sed,
                                                   ChDataModel::Filter& filter) const;

  /**
   * @brief computeMagnitude
   *   Compute the AB magnitude as follows :
   *
   *   Magnitude_AB = −2.5*(log10(∫fλ*t dλ) − log10(∫t*c / λ*λ dλ) − 48.6
   *
   *   with :
   *        fλ -> SED flux
   *        λ  -> wavelength in Angstrom
   *        t  -> value in % of the filter for a specific wavelength
   *
   *        In the code there is a reference to 2 integration as follows
   *        - integration (1) is refered to ∫fλ*t dλ
   *        - filter intergation (2) is refered to ∫t*c / λ*λ dλ
   *
   * @details
   *
   * @param[in]
   *   convolution_integration : integration value of the convolution between
   *                             a SED and a FILTER
   *   filter_integration      : integration value of a FILTER
   *
   * @return double
   *         it returns the apparent AB magnitude
   */
  double computeMagnitude( const double convolution_integration,
                           const double filter_integration) const;


private:


  /**
    * @brief displayVector
    *   For internal use, display all Points of a vector
    * @details
    *
    *
    * @param[in]
    *   points_vector : vector containing Point objects
    *   message       : string message
    *
    * @return
    *
    */
  void displayVector( std::vector<Point>& points_vector,
                      const std::string&  message = " ") const;



 double m_tolerence{}; // Tolerence for comparison of a double

};


#endif /* MAGNITUDECALCULATION_H_ */
