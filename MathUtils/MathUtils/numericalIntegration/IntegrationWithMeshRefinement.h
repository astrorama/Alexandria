/*
 * IntegrationWithMeshRefinement.h
 *
 *  Created on: Jul 2, 2015
 *      Author: fdubath
 */

#ifndef MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_INTEGRATIONWITHMESHREFINEMENT_H_
#define MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_INTEGRATIONWITHMESHREFINEMENT_H_
#include <cmath>
#include "ElementsKernel/Real.h"
#include <functional>


namespace Euclid {
namespace MathUtils {

template<typename integration_functor>
class IntegrationWithMeshRefinement {

public:
  IntegrationWithMeshRefinement(double relative_precion, int initial_order):
    m_relative_precion{relative_precion},
    m_initial_order{initial_order}{}

  double operator()(const std::function<double(double)>& f,double x_min, double x_max){
    int m = m_initial_order;
    double value_order_m=0.;
    double value_order_m_1 = m_integration_functor(f,x_min,x_max,m);
    double diff=0.;
    do{
      ++m;
      value_order_m=value_order_m_1;
      value_order_m_1 = m_integration_functor(f,x_min,x_max,value_order_m,m);
      diff=value_order_m_1-value_order_m;
    } while ( std::abs(diff/value_order_m)>m_relative_precion);

    return value_order_m_1;
  }

private:
  integration_functor m_integration_functor{};
  double m_relative_precion;
  int m_initial_order;
};

}
}


#endif /* MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_INTEGRATIONWITHMESHREFINEMENT_H_ */
