/**
 * SedIntegration.cpp
 *
 *  Created on: Sep 25, 2013
 *      Author : Nicolas Morisset
 */

#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

#include "ElementsKernel/ElementsException.h"
#include "ChDataModel/Filter.h"
#include "ChDataModel/VectorPair.h"
#include "ChTools/Constants.h"

#include "Faros/SedIntegration.h"
#include "Faros/InterpolationFactory.h"

using namespace std;

////////////////////////////////////////////////////////////////////////////////
//                           Destructor
////////////////////////////////////////////////////////////////////////////////

SedIntegration::~SedIntegration() {
  // TODO Auto-generated destructor stub
}

// TODO temporary function for storage intermediate data
void SedIntegration::StoreDataInFile(const vector<double>& wavelength,
                                     const vector<double>& flux,
                                     const string&         filename)
{

  // Filename for outputs
  stringstream ss;
  ofstream mag_file(filename,ios::out);

  // Write Header
  mag_file<<"#    wavelength flux "<<"\n";

  for (unsigned int i = 0; i< wavelength.size(); ++i )
  {
      if ( !mag_file )
      {
          std::cerr<<"Cannot open the output file."<<std::endl;
          break;
      }  // Loop on ALL SEDs
      else
      {
        // Store in file
        mag_file<< setw(25) << setiosflags(ios::left) << setprecision(15) << wavelength[i]
                << setw(25) << setiosflags(ios::left) << setprecision(15) << flux[i]
                <<"\n" ;
      }// eof if

  } // eof for

  mag_file.close();

}

////////////////////////////////////////////////////////////////////////////////
//                           applyRedshift
////////////////////////////////////////////////////////////////////////////////


vector<double>& SedIntegration::applyRedshift(const double red_index, vector<double>& wavelength)
{
 for (unsigned int i = 0; i< wavelength.size(); ++i)
 {
   wavelength[i] = wavelength[i]*(1 + red_index);
 }

 return wavelength;
}

////////////////////////////////////////////////////////////////////////////////
//                        getMinimumInterval
////////////////////////////////////////////////////////////////////////////////

double  SedIntegration::getMinimumInterval(const vector<double>& vector) const
{
 double min_interval{};

 // Minimum vector size
 if (vector.size() < 2)
 {
   throw ElementsException("SedIntegration::getMinimumInterval: can not compute"
                           " interval length, not enough values (at least 2)!!!");
 }

 min_interval = vector[1] - vector[0];
 double interval{};

 for (unsigned int i = 1; i < vector.size(); ++i)
 {
   interval = vector[i] - vector[i-1];
   if (interval < min_interval)
   {
     min_interval = interval;
     if (!min_interval) {
       stringstream errorBuffer;
       errorBuffer << "SedIntegration::getMinimumInterval: interval can not be null !!! Two values are be identical !!!"
                   << " at line : " << i << endl;
       throw ElementsException(errorBuffer.str());
     }
   }
 }

 return (min_interval);
}

////////////////////////////////////////////////////////////////////////////////
//                        computeMagnitude
////////////////////////////////////////////////////////////////////////////////

// Compute magnitude from a vector of fluxes
vector<double> SedIntegration::computeMagnitude(const vector<double>& flux)
{
 vector<double> magnitude {};

 for (unsigned int i = 0; i < flux.size(); ++i)
 {
   magnitude.push_back(-2.5*log10( flux[i] ) - 48.59);
 }

 return(magnitude);
}

////////////////////////////////////////////////////////////////////////////////
//                        resampleFilterSed
////////////////////////////////////////////////////////////////////////////////

// Resample FILTER or SED  in order to have a regular step between wavelengths
// and make sure the number of intervals is a multiple of 3 due to the
// Simpson integration.
VectorPair* SedIntegration::resampleFilterSed(const vector<double>& orig_wavelengths, const vector<double>& orig_flux, const double step)
{

  vector<double> new_wavelength;
  vector<double> new_efficiency;

  // Get interpolation method
  InterpolationFactory factory;
  BaseInterpolation*   method_ptr = factory.getInterpolationFunction(getInterpolationMethod(), orig_wavelengths, orig_flux);

  // Interpole filter/sed values for a regular step
  double x_wavelength = orig_wavelengths[0];

  while (x_wavelength <= orig_wavelengths[orig_wavelengths.size()-1])
  {
    new_wavelength.push_back(x_wavelength);
    new_efficiency.push_back(method_ptr->interpolate(x_wavelength));
    x_wavelength += step;
  }

  double       last_filter_wavelength = new_wavelength[new_wavelength.size()-1];
  unsigned int increment              = 1;
  unsigned int wave_size              = new_wavelength.size();

  // Check the number of intervals it must be a multiple of 3
  // for the Simpson integration
  // Add missing values for Simpson integration
  while ((wave_size - 1) % 3)
  {
    new_wavelength.push_back(last_filter_wavelength  + increment*step);
    // Set to 0.0 for extra points
    new_efficiency.push_back(0.0);
    ++increment;
    wave_size = new_wavelength.size();
  }

  // Remove pointer
  delete method_ptr;

  return (new VectorPair(new_wavelength, new_efficiency));
}

////////////////////////////////////////////////////////////////////////////////
//                        computeFlux
////////////////////////////////////////////////////////////////////////////////


// The filter provided to this method is sampled on a fine wavelength grid with a element number multiple of 3
vector<double> SedIntegration::computeFlux(const Filter& filter, const Sed& sed)
{

  vector<double> all_flux_integrated {};
  vector<double> y_values {};


  // Get filter step for resample
  double filter_step = getMinimumInterval(filter.getWaveLengths());

  // Resample FILTER
  VectorPair* vectorpair_filter = resampleFilterSed(filter.getWaveLengths(), filter.getEfficiencyValues(), filter_step);
  Filter      filterComputed(*vectorpair_filter,  filter.getFilterType(), filter.getFilterName());

  // Get the new wavelength & efficiency vectors
  vector<double> filter_wavelengths_computed  = filterComputed.getWaveLengths();
  vector<double> filter_efficiencies_computed = filterComputed.getEfficiencyValues();

  double sed_step = getMinimumInterval(sed.getWaveLengths());

  // Resample SED
  VectorPair* vectorpair_sed = resampleFilterSed(sed.getWaveLengths(), sed.getIntensities(), sed_step);
  Sed         sedComputed(*vectorpair_sed, sed.getSedName());

  vector<double> integration_part;

  integration_part.resize(filterComputed.size());

  // Apply conversion
  for (unsigned int i = 0; i< filter_efficiencies_computed.size(); i++)
  {
      integration_part[i] = filter_efficiencies_computed[i]*c_light_ang/(filter_wavelengths_computed[i]*filter_wavelengths_computed[i]);
  }

  // Compute integration for filter
  double filter_integration = simpsonCubicIntegration(filter_step, integration_part);

  vector<double> sed_shifted_wavelengths {};
  vector<double> sed_intensities = sedComputed.getIntensities();

  // Computation for each redshift step
  double red_index = 0;
  do
  {

      sed_shifted_wavelengths.clear();
      sed_shifted_wavelengths = sedComputed.getWaveLengths();

      // Apply redshift
      sed_shifted_wavelengths = applyRedshift(red_index, sed_shifted_wavelengths);

      // Get interpolation method
      InterpolationFactory factory;
      BaseInterpolation*   method_ptr = factory.getInterpolationFunction(getInterpolationMethod(), sed_shifted_wavelengths, sed_intensities);

      // Compute Y values necessary for the convolution
      y_values.clear();
      for (unsigned int i = 0; i < filter_wavelengths_computed.size(); ++i)
      {
        y_values.push_back( filter_efficiencies_computed[i] * method_ptr->interpolate(filter_wavelengths_computed[i]) );
      }

      // Compute the Simpson integration for this filter
      double convolutionIntegration = simpsonCubicIntegration(filter_step, y_values);

      // Flux
      all_flux_integrated.push_back( convolutionIntegration / filter_integration );

      red_index += m_redshift_step;

      // Remove pointer
      delete method_ptr;

   } while  (red_index < m_redshift_max);

  // Remove pointers
  delete vectorpair_filter;
  delete vectorpair_sed;

  return ( all_flux_integrated );
}


////////////////////////////////////////////////////////////////////////////////
//                        simpsonCubicIntegration
////////////////////////////////////////////////////////////////////////////////

/*
 * This implement the so-called Simpson 3/8 rule of integration, see e.g,
 * http://www.google.ch/url?sa=t&rct=j&q=&esrc=s&source=web&cd=12&ved=0CDYQFjABOAo&url=http%3A%2F%2Fmathforcollege.com%2Fnm%2Fmws%2Fgen%2F07int%2Fmws_gen_int_txt_simpson3by8.doc&ei=R9M2UuLeMePE7AaLk4CQDQ&usg=AFQjCNH73-8KmV886cscCRSW-oOi5UK6IQ&sig2=oW0V-mBbGlfnXdAJBk0UsQ&cad=rja
 */
double SedIntegration::simpsonCubicIntegration(const double x_step, const std::vector<double>& y_values) const
{
  double sum{};
  // x_num is the number of intervals, i.e., if the vector has 0, 1, 2, 3 elements, the number of intervals is 3
  size_t x_num = y_values.size() - 1;

  if (x_num % 3 != 0) {
    throw ElementsException("SedIntegration::simpsonCubicIntegration: Cannot "
                            "achieve a cubic Simpson integration if the step "
                            "number is not a multiple of 3");
  }

  // compute the sum for the first and the last 3 values
  sum = y_values.at(0) + y_values.at(x_num)
      + 3 * (y_values.at(x_num - 1) + y_values.at(x_num - 2));

  // if x_num equal 3, all terms have been added alread
  if (x_num > 3) {
    size_t index = 1;
    // carry out the sum for the all other terms, from 1 to (x_num - 5) + 2 = x_num - 3
    while (index <= (x_num-5) ) {
      sum = sum + 3 * (y_values.at(index) + y_values.at(index + 1))
          + 2 * y_values.at(index + 2);
      index += 3;
    }
  }
  return (3.0 * x_step / 8.0) * sum;
}
