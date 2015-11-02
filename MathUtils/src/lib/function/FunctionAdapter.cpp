/*
 * FunctionAdapter.cpp
 *
 *  Created on: Nov 2, 2015
 *      Author: fdubath
 */


#include "MathUtils/function/FunctionAdapter.h"

namespace Euclid {
namespace MathUtils {

FunctionAdapter::FunctionAdapter(std::function<double(double)> function) :
    m_function { function } {
}

double FunctionAdapter::operator()(const double x) const  {
  return m_function(x);
}

std::unique_ptr<Function> FunctionAdapter::clone() const  {
  return std::unique_ptr<Function> { new FunctionAdapter(m_function) };
}

}
}

