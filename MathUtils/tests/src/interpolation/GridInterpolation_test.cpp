#include "MathUtils/interpolation/GridInterpolation.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::MathUtils;
using namespace Euclid::NdArray;

enum class EnumType { A, B, C, D, E };

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridInterpolation_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(DiscreteAxis1) {
  std::vector<EnumType> knots{EnumType::A, EnumType::B, EnumType::C, EnumType::E};
  NdArray<double>       values{{4}, {1, 10, 20, 3}};

  InterpN<EnumType> interp1({knots}, values, false);
  BOOST_CHECK_EQUAL(interp1(EnumType::A), 1);
  BOOST_CHECK_EQUAL(interp1(EnumType::B), 10);
  BOOST_CHECK_EQUAL(interp1(EnumType::C), 20);
  BOOST_CHECK_EQUAL(interp1(EnumType::D), 0);
  BOOST_CHECK_EQUAL(interp1(EnumType::E), 3);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(CombinedAxes2) {
  std::vector<EnumType> knots0{EnumType::A, EnumType::B, EnumType::C, EnumType::E};
  std::vector<double>   knots1{0., 1., 2., 3., 4.};
  NdArray<double>       values{{4, 5}, {                     //
                                  1,  2,  4,  3,  5,   //
                                  6,  8,  9,  10, 11,  //
                                  90, 80, 70, 60, 65,  //
                                  1,  1,  1,  1,  1}};

  InterpN<EnumType, double> interp2({knots0, knots1}, values, true);

  BOOST_CHECK_EQUAL(interp2(EnumType::A, 1.), 2);
  BOOST_CHECK_CLOSE(interp2(EnumType::B, 2.5), 9.5, 1e-8);
  BOOST_CHECK_CLOSE(interp2(EnumType::C, 5.), 70, 1e-8);  // Extrapolated
  BOOST_CHECK_EQUAL(interp2(EnumType::D, 4.), 0.);        // d is not defined
  BOOST_CHECK_CLOSE(interp2(EnumType::E, 1.328), 1., 1e-8);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(CombinedAxesReversed2) {
  std::vector<double>   knots0{0., 1., 2., 3., 4.};
  std::vector<EnumType> knots1{EnumType::A, EnumType::B, EnumType::C, EnumType::E};

  NdArray<double> values{{5, 4}, {                 //
                                  1,  4,  3,  5,   //
                                  6,  9,  10, 11,  //
                                  90, 70, 60, 65,  //
                                  1,  1,  1,  1,   //
                                  0,  3,  0,  0}};

  InterpN<double, EnumType> interp2({knots0, knots1}, values, true);

  BOOST_CHECK_EQUAL(interp2(1., EnumType::A), 6);
  BOOST_CHECK_CLOSE(interp2(2.5, EnumType::B), 35.5, 1e-8);
  BOOST_CHECK_CLOSE(interp2(5., EnumType::C), -1, 1e-8);  // Extrapolated
  BOOST_CHECK_EQUAL(interp2(4., EnumType::D), 0.);        // d is not defined
  BOOST_CHECK_CLOSE(interp2(0.5, EnumType::E), 8., 1e-8);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
