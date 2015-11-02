/**
 * @file tests/src/function/FunctionAdapter_test_mock.cpp
 * @date November 2, 2015
 * @author FLorian Dubath
 */

#include <boost/test/unit_test.hpp>
#include <boost/test/test_tools.hpp>
#include "ElementsKernel/EnableGMock.h"

#include "MathUtils/function/FunctionAdapter.h"

using namespace testing;


class MockStdFunction {
public:
  virtual ~MockStdFunction() = default;
  MOCK_METHOD1(FunctorCall, double(double));
};


std::unique_ptr<MockStdFunction> mock_std_function_singleton {};

class TestFunction {
public:
  double operator()(double x) {
    if (mock_std_function_singleton == nullptr) {
      BOOST_FAIL("TestFunction was called when the MockStdFunction was not set");
    }
    return mock_std_function_singleton->FunctorCall(x);
  }
};


//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FunctionAdapter_test)

BOOST_AUTO_TEST_CASE(DirectCall) {
  mock_std_function_singleton.reset(new MockStdFunction{});
  EXPECT_CALL(*mock_std_function_singleton, FunctorCall(1.0)).Times(1).WillOnce(Return(3.14));

  Euclid::MathUtils::FunctionAdapter adapter{TestFunction()};

  BOOST_CHECK_EQUAL(adapter(1.0),3.14);

}

BOOST_AUTO_TEST_CASE(CloneCall) {
  mock_std_function_singleton.reset(new MockStdFunction{});
  EXPECT_CALL(*mock_std_function_singleton, FunctorCall(1.0)).Times(1).WillOnce(Return(3.14));

  Euclid::MathUtils::FunctionAdapter adapter{TestFunction()};
  auto cloned = adapter.clone();

  BOOST_CHECK_EQUAL((*cloned)(1.0),3.14);

}


//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
