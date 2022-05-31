/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/**
 * @file tests/src/Matrix_test.cpp
 * @date November 21, 2018
 * @author Alejandro Alvarez Ayllon
 */

#include "NdArray/NdArray.h"
#include <boost/test/unit_test.hpp>
#include <sstream>

using namespace Euclid::NdArray;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Matrix_test)

static_assert(sizeof(NdArray<int>) == 8, "Expected NdArray<int> to have size 8");

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(OneDimension_test) {
  NdArray<int> m{5};
  m.at(0) = 10;

  BOOST_CHECK_EQUAL(m.shape().size(), 1);
  BOOST_CHECK_EQUAL(m.shape()[0], 5);
  BOOST_CHECK_EQUAL(m.at(0), 10);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(TwoDimension_test) {
  NdArray<int> m{2, 3};
  m.at(0, 0) = 10;
  m.at(1, 0) = 15;
  m.at(0, 1) = 50;
  m.at(1, 1) = 20;

  BOOST_CHECK_EQUAL(m.shape().size(), 2);
  BOOST_CHECK_EQUAL(m.shape()[0], 2);
  BOOST_CHECK_EQUAL(m.shape()[1], 3);
  BOOST_CHECK_EQUAL((m.at(0, 0)), 10);
  BOOST_CHECK_EQUAL((m.at(std::vector<size_t>{0, 0})), 10);
  BOOST_CHECK_EQUAL((m.at(1, 1)), 20);

  const NdArray<int>& cm = m;
  BOOST_CHECK_EQUAL((cm.at(1, 1)), 20);

  std::vector<int> expected{10, 50, 0, 15, 20, 0};
  BOOST_CHECK_EQUAL_COLLECTIONS(cm.begin(), cm.end(), expected.begin(), expected.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(InitFromVector_test) {
  NdArray<int> m{std::vector<size_t>{2, 3}, {10, 50, 0, 15, 20, 0}};

  BOOST_CHECK_EQUAL(m.shape()[0], 2);
  BOOST_CHECK_EQUAL(m.shape()[1], 3);
  BOOST_CHECK_EQUAL((m.at(0, 0)), 10);
  BOOST_CHECK_EQUAL((m.at(1, 1)), 20);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(BadInitFromVector_test) {
  try {
    const std::vector<int> v{10, 20, 30, 40};
    NdArray<int>           m(std::vector<size_t>{2, 3}, v);
    BOOST_ERROR("The construction should have failed");
  } catch (...) {
  }
  try {
    NdArray<int> m(std::vector<size_t>{2, 3}, {10, 50, 0, 15});
    BOOST_ERROR("The construction should have failed");
  } catch (...) {
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(BadInitFromIterators_test) {
  const std::vector<int> v{10, 20, 30, 40};
  try {
    NdArray<int> m(std::vector<size_t>{2, 3}, v.begin(), v.end());
    BOOST_ERROR("The construction should have failed");
  } catch (...) {
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Fill_test) {
  NdArray<int> m{2, 3};
  std::fill(m.begin(), m.end(), 42);

  std::vector<int> expected{42, 42, 42, 42, 42, 42};
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), expected.begin(), expected.end());
  BOOST_CHECK_EQUAL(m.at(1, 1), 42);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(VectorCopy_test) {
  std::vector<int> original{1, 1, 2, 3, 5, 8};
  std::vector<int> expected(original.begin(), original.end());
  NdArray<int>     m(std::vector<size_t>{2, 3}, original);

  BOOST_CHECK_EQUAL(original.size(), 6);
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), expected.begin(), expected.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(VectorMove_test) {
  std::vector<int> original{1, 1, 2, 3, 5, 8};
  std::vector<int> expected(original.begin(), original.end());
  NdArray<int>     m(std::vector<size_t>{2, 3}, std::move(original));

  BOOST_CHECK_EQUAL(original.size(), 0);
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), expected.begin(), expected.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Ostream_test) {
  std::vector<int> original{1, 1, 2, 3, 5, 8};
  NdArray<int>     m(std::vector<size_t>{2, 3}, std::move(original));

  std::stringstream stream;
  stream << m;

  BOOST_CHECK_EQUAL(stream.str(), std::string("<2,3>1,1,2,3,5,8"));
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(FromIterator_test) {
  std::list<int> original{1, 7, 6, 9, 5, 3};
  NdArray<int>   m(std::vector<size_t>{2, 3}, std::begin(original), std::end(original));
  BOOST_CHECK_EQUAL(original.size(), 6);
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), original.begin(), original.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Reshape_test) {
  std::vector<int> values{10, 50, 0, 15, 20, 0};
  NdArray<int>     m{std::vector<size_t>{2, 3}, values};

  m.reshape(6);

  BOOST_CHECK_EQUAL(m.size(), 6);
  BOOST_CHECK_EQUAL(m.shape().size(), 1);
  BOOST_CHECK_EQUAL(m.shape()[0], 6);

  for (size_t i = 0; i < values.size(); ++i) {
    BOOST_CHECK_EQUAL(m.at(i), values[i]);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(BadReshape_test) {
  std::vector<int> values{10, 50, 0, 15, 20, 0};
  NdArray<int>     m{std::vector<size_t>{2, 3}, values};

  BOOST_CHECK_THROW(m.reshape(3), std::range_error);
  BOOST_CHECK_THROW(m.reshape(10), std::range_error);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Copy_test) {
  std::vector<int> values{10, 50, 0, 15, 20, 0};
  NdArray<int>     m{std::vector<size_t>{2, 3}, values};

  auto copy = m.copy();
  BOOST_CHECK_EQUAL_COLLECTIONS(values.begin(), values.end(), copy.begin(), copy.end());
  copy.at(0, 0) = 1;
  copy.at(0, 1) = 0;

  BOOST_CHECK_EQUAL(m.at(0, 0), values[0]);
  BOOST_CHECK_EQUAL(m.at(0, 1), values[1]);
  BOOST_CHECK_EQUAL(copy.at(0, 0), 1);
  BOOST_CHECK_EQUAL(copy.at(0, 1), 0);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Concatenate_test) {
  std::vector<int> values1{1, 2, 3, 4, 5, 6};
  std::vector<int> values2{50, 60, 70, 80, 90, 100};
  NdArray<int>     m{std::vector<size_t>{2, 3}, values1};
  NdArray<int>     add{std::vector<size_t>{2, 3}, values2};

  m.concatenate(add);

  BOOST_CHECK_EQUAL(m.shape()[0], 4);
  BOOST_CHECK_EQUAL(m.shape()[1], 3);
  BOOST_CHECK_EQUAL(m.size(), 12);

  std::vector<int> expected = values1;
  std::copy(values2.begin(), values2.end(), std::back_inserter(expected));

  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), m.begin(), m.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConcatenateNamed_test) {
  std::vector<int>               values1{1, 2, 3, 4, 5, 6};
  std::vector<int>               values2{50, 60, 70, 80, 90, 100};
  const std::vector<std::string> attr_names{"ID", "SED", "PDZ"};
  NdArray<int>                   m(std::vector<size_t>{2}, attr_names, values1);
  NdArray<int>                   add(std::vector<size_t>{2}, attr_names, values2);

  m.concatenate(add);

  BOOST_CHECK_EQUAL(m.shape()[0], 4);
  BOOST_CHECK_EQUAL(m.shape()[1], 3);

  std::vector<int> expected = values1;
  std::copy(values2.begin(), values2.end(), std::back_inserter(expected));

  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), m.begin(), m.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(BadConcatenate_test) {
  NdArray<int> m{std::vector<size_t>{2, 3}};
  NdArray<int> add1{std::vector<size_t>{2, 4}};
  NdArray<int> add2{std::vector<size_t>{2, 3, 4}};

  BOOST_CHECK_THROW(m.concatenate(add1), std::length_error);
  BOOST_CHECK_THROW(m.concatenate(add2), std::length_error);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(AttrNames_test) {
  const std::vector<std::string> attr_names{"ID", "SED", "PDZ"};
  NdArray<int>                   named{{20}, attr_names};

  BOOST_CHECK_EQUAL(named.shape().size(), 2);
  BOOST_CHECK_EQUAL(named.shape()[0], 20);
  BOOST_CHECK_EQUAL(named.shape()[1], 3);
  BOOST_CHECK_EQUAL(named.size(), 60);

  for (size_t i = 0; i < named.shape()[0]; ++i) {
    named.at(i, "ID")  = i;
    named.at(i, "SED") = i * 2;
    named.at(i, "PDZ") = i * 10 + 5;
  }

  auto attrs = named.attributes();
  BOOST_CHECK_EQUAL_COLLECTIONS(attrs.begin(), attrs.end(), attr_names.begin(), attr_names.end());
  BOOST_CHECK_THROW(named.at(0, "XXX"), std::out_of_range);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ReshapeWithAttr_test) {
  const std::vector<std::string> attr_names{"ID", "SED", "PDZ"};
  NdArray<int>                   named{{20}, attr_names};
  BOOST_CHECK_THROW(named.reshape(10, 2), std::invalid_argument);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Slice_test) {
  NdArray<int> m({2, 3, 3}, {1, 1, 1, 2, 2, 2, 3, 3, 3, 11, 11, 11, 22, 22, 22, 33, 33, 33});
  BOOST_CHECK_EQUAL(m.size(), 18);

  auto first  = m.slice(0);
  auto second = m.slice(1);
  BOOST_CHECK_THROW(m.slice(2), std::out_of_range);

  BOOST_CHECK_EQUAL(first.size(), 9);
  BOOST_CHECK_EQUAL(first.shape().size(), 2);
  BOOST_CHECK_EQUAL(first.shape()[0], 3);
  BOOST_CHECK_EQUAL(first.shape()[1], 3);

  BOOST_CHECK_EQUAL(first.at(0, 0), 1);
  BOOST_CHECK_EQUAL(first.at(1, 0), 2);
  BOOST_CHECK_EQUAL(first.at(2, 1), 3);

  std::vector<int> expected_first{1, 1, 1, 2, 2, 2, 3, 3, 3};
  BOOST_CHECK_EQUAL_COLLECTIONS(first.begin(), first.end(), expected_first.begin(), expected_first.end());

  BOOST_CHECK_EQUAL(second.size(), 9);
  BOOST_CHECK_EQUAL(second.shape().size(), 2);
  BOOST_CHECK_EQUAL(second.shape()[0], 3);
  BOOST_CHECK_EQUAL(second.shape()[1], 3);

  BOOST_CHECK_EQUAL(second.at({0, 0}), 11);
  BOOST_CHECK_EQUAL(second.at(0, 0), 11);
  BOOST_CHECK_EQUAL(second.at({1, 0}), 22);
  BOOST_CHECK_EQUAL(second.at(1, 0), 22);
  BOOST_CHECK_EQUAL(second.at({2, 1}), 33);
  BOOST_CHECK_EQUAL(second.at(2, 1), 33);

  std::vector<int> expected_second{11, 11, 11, 22, 22, 22, 33, 33, 33};
  BOOST_CHECK_EQUAL_COLLECTIONS(second.begin(), second.end(), expected_second.begin(), expected_second.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NextSlice_test) {
  NdArray<int> m({2, 3, 3}, {1, 1, 1, 2, 2, 2, 3, 3, 3, 11, 11, 11, 22, 22, 22, 33, 33, 33});
  BOOST_CHECK_EQUAL(m.size(), 18);

  auto             first = m.slice(0);
  std::vector<int> expected_first{1, 1, 1, 2, 2, 2, 3, 3, 3};
  BOOST_CHECK_EQUAL_COLLECTIONS(first.begin(), first.end(), expected_first.begin(), expected_first.end());

  first.next_slice();
  std::vector<int> expected_second{11, 11, 11, 22, 22, 22, 33, 33, 33};
  BOOST_CHECK_EQUAL_COLLECTIONS(first.begin(), first.end(), expected_second.begin(), expected_second.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(SliceTwice_test) {
  NdArray<int> m({2, 3, 3}, {1, 1, 1, 2, 2, 2, 3, 3, 3, 11, 11, 11, 22, 22, 22, 33, 33, 33});
  BOOST_CHECK_EQUAL(m.size(), 18);

  auto first  = m.slice(0);
  auto second = first.slice(2);

  BOOST_CHECK_EQUAL(second.size(), 3);
  BOOST_CHECK_EQUAL(second.shape().size(), 1);
  BOOST_CHECK_EQUAL(second.shape()[0], 3);

  BOOST_CHECK_EQUAL(second.at(0), 3);
  BOOST_CHECK_EQUAL(second.at(1), 3);
  BOOST_CHECK_EQUAL(second.at(2), 3);

  std::vector<int> expected_second{3, 3, 3};
  BOOST_CHECK_EQUAL_COLLECTIONS(second.begin(), second.end(), expected_second.begin(), expected_second.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(SliceConst_test) {
  const NdArray<int> m({2, 3, 3}, {1, 1, 1, 2, 2, 2, 3, 3, 3, 11, 11, 11, 22, 22, 22, 33, 33, 33});

  auto first  = m.slice(0);
  auto second = first.slice(2);

  BOOST_CHECK_EQUAL(second.at(0), 3);
  BOOST_CHECK_EQUAL(second.at(1), 3);
  BOOST_CHECK_EQUAL(second.at(2), 3);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(RSlice_test) {
  NdArray<int> m({2, 3, 3}, {1, 1, 1, 2, 2, 2, 3, 3, 3, 11, 11, 11, 22, 22, 22, 33, 33, 33});
  BOOST_CHECK_EQUAL(m.size(), 18);

  auto first  = m.rslice(0);
  auto second = m.rslice(1);
  auto third  = m.rslice(2);
  BOOST_CHECK_THROW(m.slice(3), std::out_of_range);

  BOOST_CHECK_EQUAL(first.size(), 6);
  BOOST_CHECK_EQUAL(first.shape().size(), 2);
  BOOST_CHECK_EQUAL(first.shape()[0], 2);
  BOOST_CHECK_EQUAL(first.shape()[1], 3);

  BOOST_CHECK_EQUAL(first.at(0, 0), 1);
  BOOST_CHECK_EQUAL(first.at(1, 0), 11);
  BOOST_CHECK_EQUAL(first.at(0, 1), 2);
  BOOST_CHECK_EQUAL(first.at(1, 1), 22);
  BOOST_CHECK_EQUAL(first.at(0, 2), 3);
  BOOST_CHECK_EQUAL(first.at(1, 2), 33);

  std::vector<int> expected_first{1, 2, 3, 11, 22, 33};
  BOOST_CHECK_EQUAL_COLLECTIONS(first.begin(), first.end(), expected_first.begin(), expected_first.end());

  BOOST_CHECK_EQUAL(second.size(), 6);
  BOOST_CHECK_EQUAL(second.shape().size(), 2);
  BOOST_CHECK_EQUAL(second.shape()[0], 2);
  BOOST_CHECK_EQUAL(second.shape()[1], 3);

  BOOST_CHECK_EQUAL(second.at(0, 0), 1);
  BOOST_CHECK_EQUAL(second.at(1, 0), 11);
  BOOST_CHECK_EQUAL(second.at(0, 1), 2);
  BOOST_CHECK_EQUAL(second.at(1, 1), 22);
  BOOST_CHECK_EQUAL(second.at(0, 2), 3);
  BOOST_CHECK_EQUAL(second.at(1, 2), 33);

  BOOST_CHECK_EQUAL_COLLECTIONS(second.begin(), second.end(), expected_first.begin(), expected_first.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(RSliceTwice_test) {
  NdArray<int> m({2, 3, 3}, {1, 1, 1, 2, 2, 2, 3, 3, 3, 11, 11, 11, 22, 22, 22, 33, 33, 33});
  BOOST_CHECK_EQUAL(m.size(), 18);

  auto first  = m.rslice(0);
  auto second = first.rslice(2);

  BOOST_CHECK_EQUAL(second.size(), 2);
  BOOST_CHECK_EQUAL(second.shape().size(), 1);
  BOOST_CHECK_EQUAL(second.shape()[0], 2);

  BOOST_CHECK_EQUAL(second.at(0), 3);
  BOOST_CHECK_EQUAL(second.at(1), 33);

  std::vector<int> expected_second{3, 33};
  BOOST_CHECK_EQUAL_COLLECTIONS(second.begin(), second.end(), expected_second.begin(), expected_second.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(SliceOneAxis) {
  NdArray<int> array({20});

  BOOST_CHECK_THROW(array.slice(0), std::out_of_range);
  BOOST_CHECK_THROW(array.rslice(0), std::out_of_range);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(SliceWithAttrNames_test) {
  const std::vector<std::string> attr_names{"ID", "SED", "PDZ"};
  NdArray<int>                   named{{20, 10}, attr_names};

  for (size_t i = 0; i < named.shape()[0]; ++i) {
    for (size_t j = 0; j < named.shape()[1]; ++j) {
      named.at(i, j, "ID")  = i + j;
      named.at(i, j, "SED") = i * 2 + j * 3;
      named.at(i, j, "PDZ") = i * 10 + j * 4;
    }
  }

  auto first = named.slice(2);
  BOOST_CHECK_EQUAL(first.size(), 30);
  for (size_t j = 0; j < first.shape()[0]; ++j) {
    BOOST_CHECK_EQUAL(first.at(j, "ID"), 2 + j);
    BOOST_CHECK_EQUAL(first.at(j, "SED"), 4 + j * 3);
    BOOST_CHECK_EQUAL(first.at(j, "PDZ"), 20 + j * 4);
  }

  BOOST_CHECK_THROW(named.rslice(9), std::invalid_argument);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(BadSlicing_test) {
  NdArray<int> array({20, 10});
  BOOST_CHECK_THROW(array.slice(-1), std::out_of_range);
  BOOST_CHECK_THROW(array.rslice(11), std::out_of_range);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(FillWithIterator_test) {
  NdArray<int> array({10, 10});
  std::fill(array.begin(), array.end(), -1);
  for (size_t y = 0; y < 10; ++y) {
    for (size_t x = 0; x < 10; ++x) {
      BOOST_CHECK_EQUAL(array.at(x, y), -1);
    }
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(FillWithIteratorNamed_test) {
  const std::vector<std::string> attr_names{"ID", "SED", "PDZ"};
  NdArray<int>                   named{{20}, attr_names};
  std::fill(named.begin(), named.end(), -1);

  for (size_t i = 0; i < 10; ++i) {
    BOOST_CHECK_EQUAL(named.at(i, "ID"), -1);
    BOOST_CHECK_EQUAL(named.at(i, "SED"), -1);
    BOOST_CHECK_EQUAL(named.at(i, "PDZ"), -1);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
