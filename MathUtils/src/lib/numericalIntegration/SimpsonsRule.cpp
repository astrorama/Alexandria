#include  <cmath>
#include "MathUtils/numericalIntegration/SimpsonsRule.h"
#include "ElementsKernel/Exception.h"


namespace Euclid {
namespace MathUtils {

double SimpsonsRule::operator()(const std::function<double(double)>& f,double x_min, double x_max, int order){
  if (order<3){
    throw Elements::Exception() << "Simpson's Rule integration is define only for order bigger than 2";
  }

  int N= pow(2,order);
  double h=(x_max-x_min)/N;

  double partial_sum=0;
  for (int i=3;i<N-2;i++){
    partial_sum += f(x_min+i*h);
  }

  partial_sum += 0.375*(f(x_min) + f(x_max));
  partial_sum += 7.*(f(x_min+h) + f(x_max-h))/6.;
  partial_sum += 23.*(f(x_min+2.*h) + f(x_max-2*h))/24.;

  return partial_sum*h;

}

double SimpsonsRule::operator()(const std::function<double(double)>& f,double x_min, double x_max, double previous_value, int order){
  if (order<4){
    throw Elements::Exception() << "Simpson's Rule integration with recursion is define only for order bigger than 3";
  }

  int N = pow(2,order);
  double h=(x_max-x_min)/N;

  double partial_sum=0;

  for (int j=1;j<N/2-1;j++){
    int i=2*j+1;
     partial_sum += f(x_min+i*h);
  }

  partial_sum += 7.*(f(x_min+h) + f(x_max-h))/6.;
  partial_sum -= 5.*(f(x_min+2.*h) + f(x_max-2.*h))/24.;
  partial_sum += (f(x_min+4.*h) + f(x_max-4.*h))/24.;
  return partial_sum*h+previous_value/2.;
}

} // End of MathUtils
} // end of namespace Euclid
