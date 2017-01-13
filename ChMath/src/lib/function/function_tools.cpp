/** 
 * @file function_tools.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/ElementsException.h"
#include "ChMath/function/Integrable.h"
#include "ChMath/function/function_tools.h"
#include "ChMath/function/multiplication.h"

namespace ChMath {

double integrate(const Function& function, const double min, const double max) {
  const Integrable* integrable = dynamic_cast<const Integrable*>(&function);
  if (integrable) {
    return integrable->integrate(min, max);
  }
  throw ElementsException() << "Numerical integration of non-Integrable Functions "
                            << "is not yet implemented";
}
    
class DefaultMultiplication : public Function {
public:
  DefaultMultiplication(const Function& f1, const Function& f2) : m_f1{f1.clone()}, m_f2{f2.clone()} {}
  double operator()(const double x) const override {
    return (*m_f1)(x) * (*m_f2)(x);
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> {new DefaultMultiplication{*m_f1, *m_f2}};
  }
private:
  std::unique_ptr<Function> m_f1;
  std::unique_ptr<Function> m_f2;
};

std::unique_ptr<Function> multiply(const Function& f1, const Function& f2) {
  // First we check if we have specific function for multiplying the two types with each other
  auto iter = multiplySpecificSpecificMap.find(std::pair<std::type_index,std::type_index>(typeid(f1),typeid(f2)));
  if (iter != multiplySpecificSpecificMap.end()) {
    return iter->second(f1,f2);
  }
  iter = multiplySpecificSpecificMap.find(std::pair<std::type_index,std::type_index>(typeid(f2),typeid(f1)));
  if (iter != multiplySpecificSpecificMap.end()) {
    return iter->second(f2,f1);
  }
  // Now we check if we have a specific function for multiplying one of the
  // parameters with a generic function
  auto iter2 = multiplySpecificGenericMap.find(typeid(f1));
  if (iter2 != multiplySpecificGenericMap.end()) {
    return iter2->second(f1,f2);
  }
  iter2 = multiplySpecificGenericMap.find(typeid(f2));
  if (iter2 != multiplySpecificGenericMap.end()) {
    return iter2->second(f2,f1);
  }
  // We couldn't find any specific function for handling the multiplication of
  // the f1 and f2, so return the default
  return std::unique_ptr<Function> {new DefaultMultiplication(f1, f2)};
}

} // End of ChMath