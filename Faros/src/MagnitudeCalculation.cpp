/*
 * MagnitudeCalculation.cpp
 *
 *  Created on: Jun 17, 2013
 *      Author: admin
 */

#include <sstream>
#include <iostream>
#include <math.h>

#include "ChDataModel/Photometry.h"
#include "ChDataModel/Enumerations/FilterNames.h"
#include "ChDataModel/Source.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/Filter.h"
#include "ElementsKernel/ElementsException.h"
#include "Faros/MagnitudeCalculation.h"
#include "ElementsKernel/Real.h"



using namespace std;
using namespace ChDataModel;



////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////


// Simple linear interpolation: compute Y ordinate from a known abscissa X
// and having two known Points
double  MagnitudeCalculation::linearInterpolation(const Point&  first_point,
                                                  const Point&  second_point,
                                                  const double abscissa) const
{

  double x0 = first_point.getX();
  double y0 = first_point.getY();
  double x1 = second_point.getX();
  double y1 = second_point.getY();

  double ordinate{};

  // Class Point to be created?
  if (abs(x1-x0) >= m_tolerence) {
    ordinate = y0 + ( (y1-y0) * (abscissa-x0)/(x1-x0));
  }
  else
  {
    stringstream errorBuffer;
    errorBuffer << "MagnitudeCalculation::linearInterpolation : Division by zero! "
                << " x1-x0 = " << x1-x0 <<" ,x1 = "<<x1<<" ,x0 = "<<x0<< endl;
    throw ElementsException(errorBuffer.str());
  }

  return (ordinate);
}

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

//
// Function to compute the integration(trapezoidal) of the convolution between
// the FILTER and the SED points using the simpson algorithm
//
pair<double, double> MagnitudeCalculation::convolutionIntegration(const double filter_ordinate,
                                         const double filter_next_ordinate,
                                         const double sed_ordinate,
                                         const double sed_next_ordinate,
                                         const double lambda_mean,
                                         const double delta_abscissa) const
{

   double result_filter{};
   double result_flux{};
   pair<double ,double> result{};

   if (lambda_mean >= m_tolerence)
   {
     // Compute the convolution integration (first part of the Magnitude equation)
     result_flux   = (sed_next_ordinate + sed_ordinate) * (filter_next_ordinate + filter_ordinate) * delta_abscissa  / 4.;
     // Compute the filter integration (second part of the Magnitude equation)
     result_filter = ( (filter_next_ordinate + filter_ordinate) / 2.) * delta_abscissa * c_light_ang / (lambda_mean*lambda_mean);
   }
   else
   {
     stringstream errorBuffer;
     errorBuffer << "MagnitudeCalculation::convolutionIntegration : Division by zero! "
                 << " lambda_mean = " << lambda_mean << endl;
     throw ElementsException(errorBuffer.str());
   }

   result.first  = result_flux;
   result.second = result_filter;

   return (result);
}

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

//
// Function to get the subset of SED points concerned for a delta range of wavelengths
// (between 2 filter points)
//
// outputs:
//        out_sedPointsVector
//        out_filterPointsVector
//
void MagnitudeCalculation::getSedSubsetPoints(const Sed&           sed,
                                              const Point&         filter,
                                              const Point&         filter_next,
                                                    vector<Point>& out_sed_points_vector,
                                                    vector<Point>& out_filter_points_vector) const

{

  unsigned int sed_index          = 0;  // index for SED
  int          sed_index_begin    = -1; // -1 --> no value found
  int          sed_index_end      = -1; // -1 --> no value found

  double filter_x      = filter.getX(); // Filter abscissa
  double filter_next_x = filter_next.getX();

  // Clear vectors
  out_sed_points_vector.clear();
  out_filter_points_vector.clear();

  SedNames sed_name  = sed.getSedName();

  //
  //---------------------------------------------------------------------------
  //

  // Throw exception if not SED point at all in filter

  // Filter wavelengths must increase
  if (filter_x >= filter_next_x )
    {
      stringstream errorBuffer;
      errorBuffer << "MagnitudeCalculation::getSedSubsetPoints : filter wavelength "
                  << " not increasing? filter_x : "<< filter_x
                  << " filter_next_x : "<<filter_next_x << endl;
      throw ElementsException(errorBuffer.str());
    }

  // Throw exception if not SED point at all in filter

  // Before the filter point or after the second filter point
  if (sed.getWaveLength(sed.size()-1) < filter_x ||
      sed.getWaveLength(0) > filter_next_x )
    {
      stringstream errorBuffer;
      errorBuffer << "MagnitudeCalculation::getSedSubsetPoints : No SED points "
                  << " found in the filter, sed name : "<< sed_name << endl;
      throw ElementsException(errorBuffer.str());
    }

  //
  //---------------------------------------------------------------------------
  //

  // Loop on SED rows to find which SED points is part of the filter

  bool alreadyFound = false;

  while( sed_index < sed.size() )
  {
    // Look for the first point
    if (sed.getWaveLength(sed_index) < filter_x)
      sed_index_begin = sed_index;

    // Look for the point just after the filter abscissa
    if (sed.getWaveLength(sed_index) > filter_next_x && !alreadyFound) {
      sed_index_end = sed_index;
      alreadyFound = true;
    }

    ++sed_index;
  } // eof while

  // SED index can not be negative!
  if (sed_index_begin == -1 || sed_index_end == -1)
  {
      stringstream errorBuffer;
      errorBuffer << "MagnitudeCalculation::getSedSubsetPoints : SED index negative! "
                  << " sed_index_begin = " << sed_index_begin
                  << " sed_index_end = "<<sed_index_end<< endl;
      throw ElementsException(errorBuffer.str());
  }

  //
  //---------------------------------------------------------------------------
  //

  // Fill up the SED vector with SED points selected

  Point sedPoint;

  for (int i = sed_index_begin; i <= sed_index_end; i++)
  {
    sedPoint.setXY(sed.getWaveLength(i), sed.getIntensity(i));

    if ( !isEqual(sed.getWaveLength(i), filter_x) &&
         !isEqual(sed.getWaveLength(i), filter_next_x) )
    {
      out_sed_points_vector.push_back(sedPoint);
    }

  }

  Point newFilterPoint; // For new filter point
  Point newSedPoint;    // For new sed point

  vector<Point> newPointVector; // Temporary storage for new points

  //
  //---------------------------------------------------------------------------
  //

  // Compute additionnal FILTER points of the SED points selected
  // The first and last SED points are excluded
  for (auto it = out_sed_points_vector.begin()+1; it != out_sed_points_vector.end()-1; it++)
  {
    double new_filterX = it->getX();
    double new_filterY{};

    try
    {
       new_filterY = linearInterpolation(filter, filter_next, new_filterX);
    }
    catch(ElementsException& e)
    {
      cout<<"Exception: from getSedSubsetPoints, #1 "<<endl;
      cout << e.what() << endl;
    }

    // For each SED point, compute corresponding filter point
    newFilterPoint.setXY(new_filterX, new_filterY);

    // Store new filter point
    newPointVector.push_back(newFilterPoint);

  } //eof for

  // Add first filter point to filter vector
  out_filter_points_vector.push_back(filter);

  // Add new filter points to the filter vector
  for (auto it = newPointVector.begin(); it != newPointVector.end(); it++)
  {
    out_filter_points_vector.push_back(*it);
  }

  // Add next filter point to the end of filter vector
  out_filter_points_vector.push_back(filter_next);

  // Sort vector following abscissa
  std::sort(out_filter_points_vector.begin(), out_filter_points_vector.end());
  std::reverse(out_filter_points_vector.begin(), out_filter_points_vector.end());

  //
  //---------------------------------------------------------------------------
  //

  // Compute the 2 new SED points corresponding to the two FILTER points provided

  // Minimum SED points required
  if (out_sed_points_vector.size() < 2)
  {
      stringstream errorBuffer;
      errorBuffer << "MagnitudeCalculation::getSedSubsetPoints : Not enough"
                  << " SED points to compute the SED points corresponding"
                  << " to the given filter point, SED name : "<< sed_name
                  << " SED selected vector size : "<< out_sed_points_vector.size()
                  << endl;
      throw ElementsException(errorBuffer.str());
  }

  try
  {
    bool first_point_to_add  = false;
    bool next_point_to_add   = false;
    // Add the 2 new SED points corresponding to the 2 provided filter points
    // if they don't already exist

    Point sedFirstNew;

   // Compute new point only when sed abscissa not equal to filter abscissa
   // of the first filter point
   if ((*out_sed_points_vector.begin()).getX() != filter_x)
    {
      double y = linearInterpolation(*out_sed_points_vector.begin(),
                                  *(out_sed_points_vector.begin()+1), filter_x);
      sedFirstNew.setXY(filter_x, y);
      first_point_to_add = true;
    }

    Point sedNextNew;

    // Compute new point only when sed abscissa not equal to filter abscissa
    // of the next filter point
    if (filter_next_x != (*(out_sed_points_vector.end()-1)).getX() )
    {
       double y = linearInterpolation(*(out_sed_points_vector.end()-2),
                               *(out_sed_points_vector.end()-1), filter_next_x);
       sedNextNew.setXY(filter_next_x, y);
       next_point_to_add = true;
    }

    if (first_point_to_add)
      out_sed_points_vector.push_back(sedFirstNew);
    if (next_point_to_add)
      out_sed_points_vector.push_back(sedNextNew);

  }
  catch(ElementsException& e)
  {
    cout<<"Exception: from getSedSubsetPoints, #2"<<endl;
    cout << e.what() << endl;
  }

  // Sort vector following abscissa and reverse the sorting
  std::sort(out_sed_points_vector.begin(), out_sed_points_vector.end());
  std::reverse(out_sed_points_vector.begin(), out_sed_points_vector.end());

  // Remove first and last SED points outside filter point following the abscissa
  if (out_sed_points_vector.begin()->getX() < filter_x)
    out_sed_points_vector.erase(out_sed_points_vector.begin());
  if (out_sed_points_vector.end()->getX() > filter_next_x)
    out_sed_points_vector.erase(out_sed_points_vector.end());

// zzz ------------------------ Display vectors ---------------------------------
  //displayVector(out_filter_points_vector, "FILTER getSedSubsetPoints");
  //displayVector(out_sed_points_vector, "SED getSedSubsetPoints");

} // eof getSedSubsetPoints

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

// Function just for internal used, displaying a vector of points
void MagnitudeCalculation::displayVector(vector<Point>& points_vector,
                                         const string&  message) const
{

  cout <<""<<endl;
  cout <<" --- "<< message << " --- "<<endl;
  for (auto it = points_vector.begin(); it != points_vector.end(); it++)
  {
    it->print();
  }
  cout <<""<<endl;

}

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

// Function to compute the integration of a subset of points
pair<double,double> MagnitudeCalculation::subsetIntegration(vector<Point>& sed_points_vector,
                                                            vector<Point>& filter_points_vector) const
{

  double integrationSum  = 0.0;
  double filterSum       = 0.0;

  pair <double, double> sed_filter_sum{};

  if (sed_points_vector.size() != filter_points_vector.size()) {
    stringstream errorBuffer;
    errorBuffer << "MagnitudeCalculation::subsetIntegration : SED and FILTER "
                << "vectors have not the same size! SED size :"
                << sed_points_vector.size() << " FILTER size : "
                << filter_points_vector.size() << endl;
    throw ElementsException(errorBuffer.str());
  }

  for (unsigned int i = 0; i < sed_points_vector.size()-1; i++ )
  {

    double filter_x        = filter_points_vector[i].getX();
    double filter_x_next   = filter_points_vector[i+1].getX();
    double deltaWavelength = filter_x_next - filter_x;
    double lambda_mean     = (filter_x_next + filter_x) / 2.;

    try {

      sed_filter_sum = convolutionIntegration(filter_points_vector[i].getY(),
                                  filter_points_vector[i+1].getY(),
                                  sed_points_vector[i].getY(),
                                  sed_points_vector[i+1].getY(),
                                  lambda_mean,
                                  deltaWavelength);
      integrationSum += sed_filter_sum.first;
      filterSum      += sed_filter_sum.second;
    }
    catch (ElementsException& e)
    {
      cout<<"Exception message: "<<e.what()<<endl;
      return (sed_filter_sum);
    }

  } //eof for

  sed_filter_sum.first  = integrationSum;
  sed_filter_sum.second = filterSum;

  return (sed_filter_sum);

} //eof subsetIntegration

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

pair<double,double> MagnitudeCalculation::brokenLineIntegration( ChDataModel::Sed& sed,  ChDataModel::Filter& filter) const
{

  vector<Point>  sedPointsVector{};
  vector<Point>  filterPointsVector{};
  vector<double> integrationSedSumVector{};
  vector<double> integrationFilterSumVector{};

  pair<double, double> integration_sed_filter;
  pair<double, double> total_integration;

  // Loop on filter
  for (unsigned int i_filter = 0; i_filter < filter.size()-1 ; ++i_filter) {

    filterPointsVector.clear();

    // For a interval of wavelength(delta_lambda), look for SED points in the filter
    // included one point before wavelength(i) and one after wavelength(i+1)
    // with delta_lambda = wavelength(i+1)-wavelength(i)

    // Set filter point
    Point filter_point(filter.getWaveLength(i_filter), filter.getEfficiencyValue(i_filter));
    Point filter_point_next(filter.getWaveLength(i_filter+1), filter.getEfficiencyValue(i_filter+1));

    // Add filter point to vector
    filterPointsVector.push_back(filter_point);
    filterPointsVector.push_back(filter_point_next);

    try
    {

      // Get SED subset points and compute new points for SED and FILTER
      getSedSubsetPoints(sed, filter_point, filter_point_next, sedPointsVector, filterPointsVector);

    }
    catch(ElementsException& e)
      {
        cout <<""<<endl;
        cout << "Filter name : " << filter.getFilterName() <<endl;
        cout << "SED name    : " << sed.getSedName() <<endl;
        cout << "Exception Message: "<<e.what()<<endl;
        cout << "Exception: following filter points not integrated!"<<endl;
        filter_point.print();
        filter_point_next.print();
        cout <<""<<endl;
        // clear vectors
        sedPointsVector.clear();
        filterPointsVector.clear();
        continue;
      }

    try
    {
      // Integrate a subset of points
       integration_sed_filter = subsetIntegration(sedPointsVector, filterPointsVector);
    }
    catch(const ElementsException& e)
    {
       cout <<""<<endl;
       cout << "Exception Message: "<<e.what()<<endl;
       cout << "Exception: following filter points not integrated!"<<endl;
       filter_point.print();
       filter_point_next.print();
       cout <<""<<endl;
       // clear vectors
       sedPointsVector.clear();
       filterPointsVector.clear();
       continue;
    }

    // Store all integrations
    integrationSedSumVector.push_back(integration_sed_filter.first);
    integrationFilterSumVector.push_back(integration_sed_filter.second);

    // clear vectors
    sedPointsVector.clear();
    filterPointsVector.clear();

  } // endfor filter

  // Compute total integration for the full filter
  double totalSedIntegration = std::accumulate(integrationSedSumVector.begin(),
                                            integrationSedSumVector.end(),
                                            0.0);
  double totalFilterIntegration = std::accumulate(integrationFilterSumVector.begin(),
                                            integrationFilterSumVector.end(),
                                            0.0);

  total_integration.first = totalSedIntegration;
  total_integration.second = totalFilterIntegration;

  return (total_integration);

} // eof brokenLineIntegration

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

double MagnitudeCalculation::computeMagnitude( const double convolution_integration,
                         const double filter_integration) const
{

  if (!filter_integration)
  {
   stringstream errorBuffer;
   errorBuffer << "MagnitudeCalculation::computeMagnitude : Division by zero! "
              << " filter_integration = " << filter_integration << endl;
   throw ElementsException(errorBuffer.str());
  }

  double magnitude = -2.5*log10(convolution_integration / filter_integration ) - 48.6;

  return (magnitude);

}// eof computeMagnitude

