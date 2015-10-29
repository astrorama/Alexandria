/**
 * @file tests/src/numericalIntegration/SimpsonRule_test.cpp
 * @date 29 oct. 2015
 * @author Florian Dubath
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "MathUtils/function/Function.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"

struct simpsonsRule_Fixture {
  Euclid::MathUtils::SimpsonsRule quadrature{};

  /**
   * function f(x)->a
   */
  class ConstFunction : public Euclid::MathUtils::Function{
  public:
    ConstFunction(double a):m_a{a}{};

    double operator()(const double) const{
      return m_a;
    }

    std::unique_ptr<Function> clone() const{
      return  std::unique_ptr<Function>{new ConstFunction(m_a)};
    }
  private:
    double m_a;
  };

  /**
   * function f(x)->ax+b
   */
  class AffineFunction: public Euclid::MathUtils::Function {
  public:
    AffineFunction(double a, double b) :
        m_a { a }, m_b { b } {};

    double operator()(const double x) const {
      return m_a * x + m_b;
    }

    std::unique_ptr<Function> clone() const {
      return std::unique_ptr<Function> { new AffineFunction(m_a, m_b) };
    }
  private:
    double m_a;
    double m_b;
  };

  /**
   * function f(x)->ax^2+bx+c
   */
  class QuadraticFunction: public Euclid::MathUtils::Function {
  public:
    QuadraticFunction(double a, double b, double c) :
        m_a { a }, m_b { b }, m_c { c } {};

    double operator()(const double x) const {
      return m_a * x * x + m_b * x + m_c;
    }

    std::unique_ptr<Function> clone() const {
      return std::unique_ptr<Function> { new QuadraticFunction(m_a, m_b, m_c) };
    }
  private:
    double m_a;
    double m_b;
    double m_c;
  };

  /**
   * function f(x)->ax^3+bx^2+cx+d
   */
  class CubicFunction: public Euclid::MathUtils::Function {
  public:
    CubicFunction(double a, double b, double c, double d) :
        m_a { a }, m_b { b }, m_c { c }, m_d { d } {};

    double operator()(const double x) const {
      return m_a * x * x * x + m_b * x * x + m_c * x + m_d;
    }

    std::unique_ptr<Function> clone() const {
      return std::unique_ptr<Function> { new CubicFunction(m_a, m_b, m_c, m_d) };
    }
  private:
    double m_a;
    double m_b;
    double m_c;
    double m_d;
  };

  /**
   * function f(x)->a exp(bx)
   */
  class ExpFunction: public Euclid::MathUtils::Function {
  public:
    ExpFunction(double a, double b) :
        m_a { a }, m_b { b } {};

    double operator()(const double x) const {
      return m_a * std::exp(x*m_b);
    }

    std::unique_ptr<Function> clone() const {
      return std::unique_ptr<Function> { new ExpFunction(m_a, m_b) };
    }
  private:
    double m_a;
    double m_b;
  };

  /**
   * function f(x)->1/ sqrt(x*x*x)
   */
  class TestFunction: public Euclid::MathUtils::Function {
  public:

    double operator()(const double x) const {
      return 1./std::sqrt(x*x*x);
    }

    std::unique_ptr<Function> clone() const {
      return std::unique_ptr<Function> { new TestFunction() };
    }
  };

};



//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (simpsonsRule_test)

// check that when called with order bellow the minimal order an exception is thrown.
BOOST_FIXTURE_TEST_CASE(error_test, simpsonsRule_Fixture) {
  ConstFunction constant_function{1.0};

  BOOST_CHECK_THROW(quadrature(constant_function,0.,1.,0), Elements::Exception );
  BOOST_CHECK_THROW(quadrature(constant_function,0.,1.,1), Elements::Exception );
  BOOST_CHECK_THROW(quadrature(constant_function,0.,1.,2), Elements::Exception );
  BOOST_CHECK_NO_THROW(quadrature(constant_function,0.,1.,3));
  BOOST_CHECK_NO_THROW(quadrature(constant_function,0.,1.,4));


  BOOST_CHECK_THROW(quadrature(constant_function,0.,1.,1.,2), Elements::Exception );
  BOOST_CHECK_THROW(quadrature(constant_function,0.,1.,1.,3), Elements::Exception );
  BOOST_CHECK_NO_THROW(quadrature(constant_function,0.,1.,1.,4));
  BOOST_CHECK_NO_THROW(quadrature(constant_function,0.,1.,1.,5));
}


BOOST_FIXTURE_TEST_CASE(Linear, simpsonsRule_Fixture) {
  ConstFunction constant_function{1.0};
  AffineFunction affine_function{1.0,0.0};
  double result = quadrature(constant_function,0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,1.));

  result = quadrature(affine_function,0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,0.5));

  result = quadrature(affine_function,-1.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,0.));
}

BOOST_FIXTURE_TEST_CASE(quadratic, simpsonsRule_Fixture) {
  QuadraticFunction quadratic{1.0,0.,0,};
  double result = quadrature(quadratic,0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,1./3.));
}

BOOST_FIXTURE_TEST_CASE(cubic, simpsonsRule_Fixture) {
  CubicFunction cubic{1.,0.,0.,0.};
  double result = quadrature(cubic,0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,1./4.));
}

BOOST_FIXTURE_TEST_CASE(recursion, simpsonsRule_Fixture) {
  CubicFunction cubic{1.,0.,0.,0.};
  for(int order=3; order<10;order++){
    double result_o = quadrature(cubic, 0., 1., order);
    double result_o1 = quadrature(cubic, 0., 1., order+1);
    double result_rec = quadrature(cubic, 0.,1.,result_o, order+1);
    BOOST_CHECK(Elements::isEqual(result_rec,result_o1));
  }

  TestFunction test_function {};
  for (int order = 3; order < 10; order++) {
    double result_o = quadrature(test_function, 0., 1., order);
    double result_o1 = quadrature(test_function, 0., 1., order + 1);
    double result_rec = quadrature(test_function, 0., 1., result_o, order + 1);
    BOOST_CHECK(Elements::isEqual(result_rec, result_o1));
  }
}

BOOST_FIXTURE_TEST_CASE(exp_decr, simpsonsRule_Fixture) {
  ExpFunction exp_function{1.0,-1.0};
  double result = quadrature(exp_function,0.,1.,3);

  double expected = (1.-exp(-1.));
  BOOST_CHECK((result-expected)/expected<0.00001);

  result = quadrature(exp_function,0.,1.,4);
  BOOST_CHECK((result-expected)/expected<0.000001);

  TestFunction test_function{};
  expected = 2.*(1.-1./std::sqrt(2.));
  std::vector<double> precisions{0.0001,0.00001,0.000001,0.0000001};
  std::vector<int> orders{3,4,5,6};
  for (int step=0; step<orders.size(); step++){
    result = quadrature(test_function, 1., 2., orders[step]);
    BOOST_CHECK_MESSAGE((result - expected) / expected < precisions[step],
        "Expected:"+std::to_string(expected)+
        " Actual :"+std::to_string(result) +
        " Diff:"+std::to_string(100.*(result - expected) / expected) +"%");
  }
}


//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
