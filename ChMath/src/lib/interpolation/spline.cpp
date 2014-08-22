/** 
 * @file src/lib/interpolation/spline.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/ElementsException.h"
#include "ChMath/interpolation/interpolation.h"
#include "ChMath/function/Polynomial.h"
#include "ChMath/function/Piecewise.h"

namespace Euclid {
namespace ChMath {

std::unique_ptr<Function> splineInterpolation(const std::vector<double>& x, const std::vector<double>& y) {
  if (x.size() != y.size()) {
    throw ElementsException("Input X and Y vectors must have the same size");
  }
  for (auto iter=(x.begin()+1); iter!=x.end(); ++iter) {
    if (*iter <= *(iter-1)) {
      throw ElementsException("Only strictly increasing X values allowed");
    }
  }
  
  // Number of intervals
  int n = x.size() - 1;

  // Differences between knot points
  std::vector<double> h (n, 0.);
  for(int i=0; i<n; i++)
    h[i] = x[i+1] - x[i];

  std::vector<double> mu (n, 0.);
  std::vector<double> z (n+1, 0.);
  double g {0};
  for (int i=1; i<n; ++i) {
    g = 2.*(x[i+1]-x[i-1]) - h[i-1]*mu[i-1];
    mu[i] = h[i] / g;
    z[i] = (3.*(y[i+1]*h[i-1] - y[i]*(x[i+1]-x[i-1])+ y[i-1]*h[i]) / (h[i-1]*h[i]) - h[i-1] * z[i-1]) / g;
  }

  // cubic spline coefficients --  b is linear, c quadratic, d is cubic (original y's are constants)
  std::vector<double> a (n, 0.);
  std::vector<double> b (n, 0.);
  std::vector<double> c (n+1, 0.);
  std::vector<double> d (n, 0.);

  z[n] = 0.;
  c[n] = 0.;

  for (int j=n-1; j>=0; j--) {
    a[j] = y[j];
    c[j] = z[j] - mu[j] * c[j+1];
    b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2. * c[j]) / 3.;
    d[j] = (c[j+1] - c[j]) / (3. * h[j]);
  }

  // The above were taken from SplineInterpolator from Apache commons math. These
  // polynomials need to be shifted by -x[i] in our case.
  for (int i=0; i<n; i++) {
    double x_1 = -x[i];
    double x_2 = x_1 * x_1;
    double x_3 = x_1 * x_2;
    a[i] = a[i] + b[i]*x_1 + c[i]*x_2 + d[i]*x_3;
    b[i] = b[i] + 2.*c[i]*x_1 + 3.*d[i]*x_2;
    c[i] = c[i] + 3.*d[i]*x_1;
    // d[i] keeps the same value
  }

  std::vector<std::shared_ptr<Function>> functions {};
  for (int i=0; i<n; i++) {
    functions.push_back(std::shared_ptr<Function>(new Polynomial{{a[i],b[i],c[i],d[i]}}));
  }
  
  return std::unique_ptr<Function>(new Piecewise{x, std::move(functions)});
}

} // End of ChMath
} // end of namespace Euclid
