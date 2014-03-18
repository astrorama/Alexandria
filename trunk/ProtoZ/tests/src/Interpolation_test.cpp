/*
 * Interpolation_test.cpp
 *
 *  Created on: Sep 17, 2013
 *  Author : Nicolas Morisset
 */

#include <vector>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem/path.hpp>
#include <iostream>
#include <iomanip>
#include "ChTools/Constants.h"

#include "ProtoZ/Interpolation.h"


using namespace std;

//____________________________________________________________________________//

// This is the function to be interpolated
double exact(double x)
{
    return (x-5.0)*(x-5.0);
}

// Analytic derivative for calculating yp1 and ypn
double exactd(double x)
{
    return 2*x - 10.;
}


struct InterpolationFix {

  double tolerence;

  InterpolationFix() {

    tolerence = 1e-5;


  } // eof MagnitudeCalculationFix

  ~InterpolationFix() {
    // teardown
  }

  InterpolationFix(const InterpolationFix &) = delete ;

};

//=============================================================================
// Starting test
//=============================================================================

BOOST_AUTO_TEST_SUITE( CubicSplineInterpolation_test)

//-----------------------------------------------------------------------------
//                       CubicSplineInterpolation_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( filt_interpolation_Test, InterpolationFix ) {

  BOOST_TEST_MESSAGE("--> Testing splineInterpolation function according to wed site");
  BOOST_TEST_MESSAGE("--> START");

  vector<double> filt_flux {4.46988305945e-10, 7.55209775439e-09  , 8.10504409704e-08  , 5.37720817741e-07  , 2.51401509931e-06  , 6.99806298808e-06  , 1.85189046874e-05  , 4.62730582014e-05  , 0.000112264660037  , 0.000261196349244  , 0.000473327469799  , 0.000941541102988  , 0.0022360815699  , 0.00616068639278  , 0.0163716416381  , 0.0345833440769  , 0.0630512830469  , 0.0992973462051  , 0.137973383467  , 0.174139075218  , 0.198714202755  , 0.217756081148  , 0.235449018825  , 0.254551204551  , 0.275753334858  , 0.293922194239  , 0.310423652623  , 0.324055694349  , 0.33385505583 , 0.342623823556  , 0.352445759553  , 0.361494910148  , 0.367753898946  , 0.366801300375  , 0.36061192468  , 0.352385975285 , 0.348642688513  , 0.355816371765  , 0.376222528461  , 0.406474813703  , 0.44489055273  , 0.482107133548  , 0.510340033332 , 0.52688051393  , 0.533857812357  , 0.53936680191  , 0.548956621811  , 0.56530599455  , 0.585462201654  , 0.604957652414 , 0.606981267884  , 0.595474233508  , 0.565153282171  , 0.511546497581  , 0.436567688614  , 0.346083950193  , 0.253057191798  , 0.17026790731  , 0.106159452076  , 0.0629537930087  , 0.0367226901269  , 0.0219261381745  , 0.0137159476868  , 0.00897772886052  , 0.00617264762399  , 0.00445120642954  , 0.00330894550401  , 0.00260697975863  , 0.00212566526741  , 0.00177217934046  , 0.00153243182686  , 0.00133694615526  , 0.00117739405782  , 0.00101514908743  , 0.000870119931887  , 0.000718826977166  , 0.000576214450907  , 0.00046357219705  , 0.000370824021644  , 0.000330209874832  , 0.000289023073653  , 0.000279712664451  , 0.000280979816145  , 0.000282145835941  , 0.000283503946479  , 0.000295483983855  , 0.000318375736234  , 0.000341507009807  , 0.000375762094049  , 0.000410250501297  , 0.000444998017927  , 0.000513289116486  , 0.000615481378069  , 0.000785434958821  , 0.00110237828509  , 0.00160037747492  , 0.00245006092303  , 0.00367546429816  , 0.00537901679044  , 0.00739130838726  , 0.0094366448884  , 0.0111775890417  , 0.0121756005022  , 0.0121635772385  , 0.0112062696031  , 0.00957182249462  , 0.00763149229991  , 0.00575377687213  , 0.00413798770982  , 0.00286304901604  , 0.00196233585609  , 0.00139952036659  , 0.00109515471661  , 0.00100418134121  , 0.00102465922473  , 0.00113398249628  , 0.00125416217535  , 0.00134103538727  , 0.00137158926487  , 0.00133522199904  , 0.00125485141098  , 0.00120820842418  , 0.00118398450759};

  filt_flux.push_back(0.0);

  vector<double> filterWavelengths {};

  for (unsigned int i = 0; i< filt_flux.size(); i++) {
    filterWavelengths.push_back(3020.0 + i*20);
    filt_flux[i] = filt_flux[i]*c_light_ang/(filterWavelengths[i]*filterWavelengths[i]);
  }

  double yp1 = 0.0;
  double ypn = 0.0;
  CubicSplineInterpolation splineInterpolation(filterWavelengths, filt_flux, yp1, ypn);


  vector<double> x_test {3030.,  3330.,  3630.,  3930., 4230.,  4530.,  4830.,  5130., 5430.};
  vector<double> y_interpolated_python {-4.98533768e+03, 1.28622585e+10,   8.12565090e+10,
    1.05471575e+11,   4.72917758e+09,   9.41315946e+07,
    6.09864901e+07,   9.81365215e+08,   1.24647785e+08};
  vector<double> y_interpolated_test {};

    for (unsigned int i = 0; i < x_test.size(); i++)
    {
        cout << "Interpolated filter, Python: " << y_interpolated_python[i] << " NR : " << splineInterpolation.interpolate(x_test[i]) << endl;
     }
}

BOOST_FIXTURE_TEST_CASE( function_interpolation_Test, InterpolationFix ) {
  // Test done following the website:
  //            http://www.nr.com/forum/showthread.php?p=5143
  //

  BOOST_TEST_MESSAGE("--> Testing splineInterpolation function according to wed site");
  BOOST_TEST_MESSAGE("--> START");

  // Fill up a vectors xv & yv (abscissas and ordinates respectively)
  vector<double> xv {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  vector<double> yv;

  const int xvSize = xv.size();

   // fill up yv vector using the "exact" function
   for (int i = 0; i < xvSize; i++)
   {
       yv.push_back(exact(xv[i]));
   }

   // Value of first derivative for the first and last points
    double yp1 = exactd(xv[0]);
    double ypn = exactd(xv[xvSize-1]);

    CubicSplineInterpolation splineInterpolation(xv, yv, yp1, ypn);

    double xmin = *min_element(xv.begin(), xv.end());
    double xmax = *max_element(xv.begin(), xv.end());

    int    numValuesDesired = 20;
    double deltax           = (xmax-xmin)/(numValuesDesired-1.0);

    double xx;
    double result1, result2, result3;
    double expected_value1 = 25.;

    tolerence = 0.00001e+18;

    xx = xmin;
    result1 =  splineInterpolation.interpolate(xx);
    cout << " "<<endl;
    cout << " x value:            " << setw(10) << xx        << setw(10)<<
            " Exact value:        " << setw(10) << exact(xx) << setw(10)<<
            " Interpolated value: " << setw(10) << result1   << endl;

    BOOST_CHECK_CLOSE(expected_value1, result1, tolerence);

    double expected_value2 = 6.925208;

    xx = xmin + 5*deltax;
    result2 =  splineInterpolation.interpolate(xx);
    cout << " x value:            " << setw(10) << xx        << setw(10)<<
            " Exact value:        " << setw(10) << exact(xx) << setw(10)<<
            " Interpolated value: " << setw(10) << result2   << endl;

    BOOST_CHECK_CLOSE(expected_value2, result2, tolerence);

    double expected_value3 = 12.434903;
    xx = xmin + 18*deltax;
    result3 =  splineInterpolation.interpolate(xx);
    cout << " x value:            " << setw(10) << xx        << setw(10)<<
            " Exact value:        " << setw(10) << exact(xx) << setw(10)<<
            " Interpolated value: " << setw(10) << result3   << endl;

    BOOST_CHECK_CLOSE(expected_value3, result3, tolerence);

    BOOST_TEST_MESSAGE("--> END");

}


//____________________________________________________________________________//
BOOST_AUTO_TEST_SUITE_END ()



