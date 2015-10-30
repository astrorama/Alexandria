/**
 * @file src/lib/CosmologicalDistances.h
 * @date November 29, 2015
 * @author Florian Dubath
 */
#include <cmath>

#include "ElementsKernel/PhysConstants.h"
#include "ElementsKernel/Real.h"

#include "MathUtils/function/function_tools.h"
#include "MathUtils/numericalIntegration/AdaptativeIntegration.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"

#include "PhysicsUtils/CosmologicalDistances.h"

namespace Euclid {
namespace PhysicsUtils {

double CosmologicalDistances::hubbleDistance(const CosmologicalParameters& parameters) const {
  return Elements::Units::c_light * 1.0E3 / parameters.getHubbleConstant(); // in [pc]
}

double CosmologicalDistances::hubbleParameter(double z,
    const CosmologicalParameters& parameters) const {
  double square = (1. + z) * (1. + z);
  double cube = square * (1. + z);
  return std::sqrt(
      parameters.getOmegaM() * cube + parameters.getOmegaK() * square
          + parameters.getOmegaLambda());
}

class FunctionWrapper: public MathUtils::Function {
public:
  FunctionWrapper(std::function<double(double)> function) :
      m_function { function } {
  }
  ;

  double operator()(const double x) const override {
    return m_function(x);
  }

  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> { new FunctionWrapper(m_function) };
  }
private:
  std::function<double(double)> m_function;
};

double CosmologicalDistances::comovingDistance(double z,
    const CosmologicalParameters& parameters, double relative_precision) const {
  if (Elements::isEqual(0., z)) {
    return 0.;
  }

  std::unique_ptr<MathUtils::NumericalIntegrationScheme> integrationScheme {
      new MathUtils::AdaptativeIntegration<MathUtils::SimpsonsRule>(
          relative_precision, MathUtils::SimpsonsRule::minimal_order) };

  FunctionWrapper wrapper(
      [&parameters,this](double x) {return 1./hubbleParameter(x,parameters);});

  return hubbleDistance(parameters)
      * integrate(wrapper, 0., z, std::move(integrationScheme));

}

double CosmologicalDistances::transverseComovingDistance(double z,
    const CosmologicalParameters& parameters) const {
  double comoving = comovingDistance(z, parameters);
  if (Elements::isEqual(0., parameters.getOmegaK())) {
    return comoving;
  }

  double dHOverSqrtOmegaK = hubbleDistance(parameters)
      / std::sqrt(std::abs(parameters.getOmegaK()));

  if (parameters.getOmegaK() > 0) {
    return dHOverSqrtOmegaK * std::sinh(comoving / dHOverSqrtOmegaK);
  } else {
    return dHOverSqrtOmegaK * std::sin(comoving / dHOverSqrtOmegaK);
  }
}

double CosmologicalDistances::luminousDistance(double z,
    const CosmologicalParameters& parameters) const {
  double ld;
  if (Elements::isEqual(0., z)) {
    return 10.;
  } else {
    return (1. + z) * transverseComovingDistance(z, parameters);
  }
}

double CosmologicalDistances::distanceModulus(double z,
    const CosmologicalParameters& parameters) const {
  return 5. * std::log10(luminousDistance(z, parameters) / 10.);
}

}
}
