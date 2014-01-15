/**
 * @file FluxModeling.cpp
 * @date Dec 3, 2013
 * @author Nicolas Morisset
 */


#include "ProtoZ/FluxModeling.h"
#include "ProtoZ/matrix/FluxMatrix.h"

using namespace std;
using namespace ProtoZ::parameter;

////////////////////////////////////////////////////////////////////////////////
//                           Destructor
////////////////////////////////////////////////////////////////////////////////


FluxModeling::~FluxModeling() {
  // TODO Auto-generated destructor stub
}

FluxModeling::FluxModeling(FluxModelingParameters* progParameters) :
      m_params(progParameters) {
  setup();
}

// Get all parameters
void FluxModeling::setup() {

  m_lambdaStep = m_params->getLambdaInterpolationStep();
  m_method     = m_params->getInterpolationPolyDegree();

}

////////////////////////////////////////////////////////////////////////////////
//                           computeFluxMatrix
////////////////////////////////////////////////////////////////////////////////

ProtoZ::matrix::FluxMatrix FluxModeling::computeFluxMatrix() {

  // Create the matrix
  ProtoZ::matrix::FluxMatrix matrix {*m_params};

 // Resampled all Filters
 vector<unique_ptr<VectorPair>> resampledFilters = resampledAllFilters();

 // Compute Filter integral
 vector<double> filtersIntegralVector = computeFilterIntegral(resampledFilters);

 for (uint32_t sedIndex = 0; sedIndex < m_params->getSeds().size(); ++sedIndex) {

   auto sed = m_params->getSeds().indexToData(sedIndex);

   for (uint32_t ebvIndex=0; ebvIndex<m_params->getEbvs().size(); ++ebvIndex) {

     for (uint32_t extLawIndex=0; extLawIndex<m_params->getExtLaws().size(); ++extLawIndex) {

       vector<double> sedIntensitiesVector = sed.getIntensities();
       vector<double> extLawVector         = (m_params->getExtLaws().indexToData(extLawIndex)).getAxisY();

       vector<double> extLawAppliedOnSed   = applyExtinctionLaw(sed.getWaveLengths(),
                                                                sedIntensitiesVector,
                                                                extLawVector,
                                                                m_params->getEbvs().indexToValue(ebvIndex));

       for (uint32_t zIndex = 0; zIndex < m_params->getZs().size(); ++zIndex) {

         double z = m_params->getZs().indexToValue(zIndex);

         vector<double> redshiftAppliedOnSed = applyRedshift(z, sed.getWaveLengths());

         for (uint32_t filterIndex = 0; filterIndex < resampledFilters.size(); ++filterIndex) {

           // Compute & store the flux
           double fluxIntegrated = integrateSed(*resampledFilters[filterIndex],
                                                 redshiftAppliedOnSed,
                                                 extLawAppliedOnSed,
                                                 filtersIntegralVector[filterIndex]);

           matrix.setValue(sedIndex, ebvIndex, extLawIndex, zIndex, filterIndex, fluxIntegrated);

         } // Eof filter

       } // Eof redshift

     } // Eof extLaw

   } // Eof E(B-V)

 } // Eof SEDs

 return(matrix);
}

////////////////////////////////////////////////////////////////////////////////
//                           computeFilterIntegral
////////////////////////////////////////////////////////////////////////////////

vector<double> FluxModeling::computeFilterIntegral(const vector< unique_ptr<VectorPair> >& filterVectorPair) {

  vector<double> integralResult;

  integralResult.clear();

  for (const unique_ptr<VectorPair>& it : filterVectorPair ) {

    vector<double> filter_wavelengths  = it->getAxisX();
    vector<double> filter_efficiencies = it->getAxisY();

    // Apply conversion
    vector<double> integration_part;
    for (uint32_t i = 0; i< filter_efficiencies.size(); ++i) {
      integration_part.push_back(filter_efficiencies[i]*SPEED_LIGHT/(filter_wavelengths[i]*filter_wavelengths[i]));
    }

    // Compute integration for filter
    integralResult.push_back(simpsonCubicIntegration(m_lambdaStep, integration_part));
  }

  return (integralResult);
}

////////////////////////////////////////////////////////////////////////////////
//                           applyExtinctionLaw
////////////////////////////////////////////////////////////////////////////////

vector<double> FluxModeling::applyExtinctionLaw(
                                         const vector<double>& wavelength,
                                         const vector<double>& intensity,
                                         const vector<double>& kExtension,
                                         const double          ebmv) {

 // Store new computed flux
 vector<double> newIntensity;

 double exponent{};

 for (uint32_t i=0; i< wavelength.size(); ++i )
 {
   // Get interpolation method
   InterpolationFactory factory;
   unique_ptr<BaseInterpolation> method_ptr = factory.getInterpolationFunction(getInterpolationMethod(), wavelength, kExtension);

   exponent = -0.4 * method_ptr->interpolate(wavelength[i]) * ebmv;
   newIntensity.push_back(intensity[i]*pow(10., exponent));
 }

 return (newIntensity);
}

////////////////////////////////////////////////////////////////////////////////
//                           applyRedshift
////////////////////////////////////////////////////////////////////////////////


vector<double> FluxModeling::applyRedshift(const double& z, const vector<double>& wavelength) {
 vector<double> new_vector;

 for (uint32_t i=0; i< wavelength.size(); ++i)
 {
   new_vector.push_back( wavelength[i]*(1 + z) );
 }

 return new_vector;
}

////////////////////////////////////////////////////////////////////////////////
//                           resampledAllFilters
////////////////////////////////////////////////////////////////////////////////

vector<unique_ptr<VectorPair>> FluxModeling::resampledAllFilters() {

  vector< unique_ptr<VectorPair> > result;

  for (uint32_t filterIndex=0; filterIndex < m_params->getFilters().size(); ++filterIndex )
  {
      Filter filter = m_params->getFilters().indexToData(filterIndex);
      unique_ptr<VectorPair> pFilter = resample(filter.getWaveLengths(), filter.getEfficiencyValues());
      result.push_back(std::move(pFilter));
  }

  return(result);
}


////////////////////////////////////////////////////////////////////////////////
//                                resample
////////////////////////////////////////////////////////////////////////////////

// Resample a vector of wavelengths and it makes sure the number of intervals
// is a multiple of 3 due to the SIMPSON integration to be applied later

unique_ptr<VectorPair> FluxModeling::resample(const vector<double>& wavelengths, const vector<double>& flux) {

  vector<double> new_wavelength;
  vector<double> new_efficiency;

  // Get interpolation method
  InterpolationFactory factory;
  unique_ptr<BaseInterpolation> method_ptr = factory.getInterpolationFunction(getInterpolationMethod(), wavelengths, flux);

  // Interpole filter/sed values for a regular step
  double x_wavelength = wavelengths[0];

  while (x_wavelength <= wavelengths[wavelengths.size()-1])
  {
    new_wavelength.push_back(x_wavelength);
    new_efficiency.push_back(method_ptr->interpolate(x_wavelength));
    x_wavelength += m_lambdaStep;
  }

  double       last_filter_wavelength = new_wavelength[new_wavelength.size()-1];
  unsigned int increment              = 1;
  unsigned int wave_size              = new_wavelength.size();

  // Check the number of intervals it must be a multiple of 3
  // for the Simpson integration
  // Add missing values for Simpson integration
  while ((wave_size - 1) % 3)
  {
    new_wavelength.push_back(last_filter_wavelength  + increment*m_lambdaStep);
    // Set to 0.0 for extra points
    new_efficiency.push_back(0.0);
    ++increment;
    wave_size = new_wavelength.size();
  }

  return ( unique_ptr<VectorPair> (new VectorPair(new_wavelength, new_efficiency)) );
}

////////////////////////////////////////////////////////////////////////////////
//                        integrateSed
////////////////////////////////////////////////////////////////////////////////
double FluxModeling::integrateSed(const VectorPair&     filterResampledVPair,
                                  const vector<double>& sedRedshiftedWavelengths ,
                                  const vector<double>& sedExtLawAppliedFluxes ,
                                  const double          filterIntegral) {


  long double    flux_integrated {};
  vector<double> y_values {}; // Storage of the interpolated values

  vector<double> filter_wavelengths  = filterResampledVPair.getAxisX();
  vector<double> filter_efficiencies = filterResampledVPair.getAxisY();

  // Get interpolation method
  InterpolationFactory factory;
  unique_ptr<BaseInterpolation> methodForSed_ptr = factory.getInterpolationFunction(getInterpolationMethod(), sedRedshiftedWavelengths, sedExtLawAppliedFluxes);

  // Compute Y values necessary for the convolution
  for (uint32_t i=0; i < filter_wavelengths.size(); ++i)
  {
    y_values.push_back( filter_efficiencies[i] * methodForSed_ptr->interpolate(filter_wavelengths[i]) );
  }

  // Compute the Simpson integration for this filter
  double convolutionIntegration = simpsonCubicIntegration(m_lambdaStep, y_values);

  // Flux
  flux_integrated = convolutionIntegration / filterIntegral ;

  return ( flux_integrated );

}


////////////////////////////////////////////////////////////////////////////////
//                        simpsonCubicIntegration
////////////////////////////////////////////////////////////////////////////////

/*
 * This implement the so-called Simpson 3/8 rule of integration, see e.g,
 * http://www.google.ch/url?sa=t&rct=j&q=&esrc=s&source=web&cd=12&ved=0CDYQFjABOAo&url=http%3A%2F%2Fmathforcollege.com%2Fnm%2Fmws%2Fgen%2F07int%2Fmws_gen_int_txt_simpson3by8.doc&ei=R9M2UuLeMePE7AaLk4CQDQ&usg=AFQjCNH73-8KmV886cscCRSW-oOi5UK6IQ&sig2=oW0V-mBbGlfnXdAJBk0UsQ&cad=rja
 */
double FluxModeling::simpsonCubicIntegration(const double x_step, const std::vector<double>& y_values) const {

  double sum{0};
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
