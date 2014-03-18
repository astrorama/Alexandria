/*
 * Interpolation.cpp
 *
 *  Created on: Sep 16, 2013
 *      Author:
 */

#include <iostream>
#include <algorithm>
#include "Faros/Interpolation.h"
#include "ElementsKernel/ElementsException.h"

using namespace std;


////////////////////////////////////////////////////////////////////////////////
//                            BaseInterpolation class
////////////////////////////////////////////////////////////////////////////////


BaseInterpolation::BaseInterpolation(const vector<double> &x, const double *y, int m)
                   : xx(&x[0]), yy(y), m_x_size(x.size()), m_x_subset_size(m), m_j_saved(0), m_hunt_or_locate(0)
{
    m_delta_j = min(1, (int)pow((double)m_x_size, 0.25));
}

double BaseInterpolation::interpolate(const double x)
{
    int j_low = m_hunt_or_locate ? hunt(x) : locate(x);
    return rawinterp(j_low, x);
}

int BaseInterpolation::locate(const double x)
{
  int j_low, j_medium, j_up;

  if (m_x_size < 2 || m_x_subset_size < 2 || m_x_subset_size > m_x_size)
  {
    throw("locate size error");
  }

  // ascending_order: True if ascending order
  bool ascending_order=(xx[m_x_size-1] >= xx[0]);

  j_low = 0;          // Init lower limit
  j_up  = m_x_size-1; // Init upper limit

  // Compute medium point
  while (j_up - j_low > 1)
  {
    j_medium = (j_up + j_low) >> 1;
    if ((x >= xx[j_medium]) == ascending_order)
      j_low = j_medium;
    else
      j_up = j_medium;
  }

  // Set the use of the hunt or locate function next time
  m_hunt_or_locate = abs(j_low - m_j_saved) > m_delta_j ? 0 : 1;
  m_j_saved        = j_low;

  return max(0, min(m_x_size - m_x_subset_size, j_low - ((m_x_subset_size-2)>>1)) );

}

int BaseInterpolation::hunt(const double x)
{
  int j_medium, j_up;
  int j_low     = m_j_saved;
  int increment = 1;

  if (m_x_size < 2 || m_x_subset_size < 2 || m_x_subset_size > m_x_size)
    throw("hunt size error");

  bool ascending_order=(xx[m_x_size-1] >= xx[0]);

  if (j_low < 0 || j_low > m_x_size-1) {
    j_low = 0;
    j_up  = m_x_size-1;
  }
  else
  {
    if ((x >= xx[j_low]) == ascending_order)
    {
      for (;;)
      {
        j_up = j_low + increment;
        if (j_up >= m_x_size-1) { j_up = m_x_size-1; break;}
        else if ((x < xx[j_up]) == ascending_order)
          break;
        else
        {
          j_low = j_up;
          increment += increment;
        }
      } // eof for

    }
    else
    {
      j_up = j_low;
      for (;;)
      {
        j_low = j_low - increment;
        if (j_low <= 0)
        {
          j_low = 0;
          break;
        }
        else if ((x >= xx[j_low]) == ascending_order)
          break;
        else
        {
          j_up = j_low;
          increment += increment;
        }
      }
    }
  }

  while (j_up - j_low > 1) {
    j_medium = (j_up + j_low) >> 1;
    if ((x >= xx[j_medium]) == ascending_order)
      j_low = j_medium;
    else
      j_up = j_medium;
  }

  m_hunt_or_locate = abs(j_low - m_j_saved) > m_delta_j ? 0 : 1;
  m_j_saved        = j_low;

  return max(0, min(m_x_size-m_x_subset_size, j_low-((m_x_subset_size-2)>>1)) );

}


////////////////////////////////////////////////////////////////////////////////
//                                 Cubic class
////////////////////////////////////////////////////////////////////////////////


void CubicSplineInterpolation::sety2(const double *xv, const double *yv, double yp1, double ypn)
{
  int i,k;
  double p,qn,sig,un;

  int n = y2.size();

  vector<double> u;
  u.resize(n-1);

  if (yp1 > 0.99e99)
  {
    y2.at(0) = u.at(0) = 0.0;
  }
  else {
    y2.at(0) = -0.5;
    u.at(0)  = (3.0/(xv[1] - xv[0])) * ((yv[1]-yv[0])/(xv[1]-xv[0])-yp1);
  }

  for (i = 1; i < n-1; i++) {
    sig      = (xv[i] - xv[i-1]) / (xv[i+1] - xv[i-1]);
    p        = sig*y2.at(i-1) + 2.0;
    y2.at(i) = (sig-1.0)/p;
    u.at(i)  = ( yv[i+1]-yv[i])/(xv[i+1]-xv[i]) - (yv[i]-yv[i-1])/(xv[i]-xv[i-1]);
    u.at(i)  = ( 6.0*u.at(i)/(xv[i+1]-xv[i-1]) - sig*u.at(i-1)) / p;
// todo put exceptions here division by zero

  }

  if (ypn > 0.99e99)
    qn = un = 0.0;
  else
  {
    qn = 0.5;
    un = (3.0/(xv[n-1]-xv[n-2]))*(ypn-(yv[n-1]-yv[n-2])/(xv[n-1]-xv[n-2]));
  }

  y2.at(n-1) = (un-qn*u.at(n-2)) / (qn*y2.at(n-2) + 1.0);

  for (k=n-2;k>=0;k--)
  {
    y2.at(k) = y2.at(k)*y2.at(k+1) + u.at(k);
  }

}

double CubicSplineInterpolation::rawinterp(const int jl, const double x)
{
  int klo=jl,khi=jl+1;
  double y,h,b,a;

  h=xx[khi]-xx[klo];

//todo modify this exception
  if (h == 0.0)
    throw("Bad input to routine splint");

  a = (xx[khi] - x) / h;
  b = (x - xx[klo]) / h;
  y = a * yy[klo] + b*yy[khi] + ( (a*a*a-a)*y2[klo] + (b*b*b-b)*y2[khi] ) *(h*h)/6.0;

  return y;
}


////////////////////////////////////////////////////////////////////////////////
//                                 Linear class
////////////////////////////////////////////////////////////////////////////////

double LinearInterpolation::rawinterp(const int j, const double x)
{
 double result{};

 if (xx[j] == xx[j+1])
 {
   result = yy[j];
 }
 else
 {
   result = yy[j] + ( (x - xx[j]) / (xx[j+1] - xx[j]) ) * (yy[j+1] - yy[j]);
 }

 return (result);
}


