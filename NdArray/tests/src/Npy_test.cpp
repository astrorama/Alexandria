/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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

#include "NdArray/io/Npy.h"
#include "TestHelper.h"
#include <ElementsKernel/Temporary.h>
#include <boost/mpl/list.hpp>
#include <boost/test/unit_test.hpp>

using namespace Euclid::NdArray;

BOOST_AUTO_TEST_SUITE(Npy_test)

typedef boost::mpl::list<int32_t, int64_t, float, double> array_type;

BOOST_AUTO_TEST_CASE_TEMPLATE(Npy1d_readwrite_test, T, array_type) {
  std::stringstream stream;

  // Construct NdArray
  NdArray<T> ndarray({100});
  std::generate(ndarray.begin(), ndarray.end(), []() { return std::rand() % 100; });

  // Write NPY
  writeNpy(stream, ndarray);

  // Read NPY
  auto rend = readNpy<T>(stream);

  BOOST_CHECK_EQUAL(rend.shape().size(), 1);
  BOOST_CHECK_EQUAL(rend.shape()[0], 100);
  BOOST_CHECK_EQUAL(rend.size(), ndarray.size());
  BOOST_CHECK_EQUAL_COLLECTIONS(ndarray.begin(), ndarray.end(), rend.begin(), rend.end());
}

BOOST_AUTO_TEST_CASE_TEMPLATE(Npy2d_readwrite_test, T, array_type) {
  std::stringstream stream;

  // Construct NdArray
  NdArray<T> ndarray({50, 2});
  std::generate(ndarray.begin(), ndarray.end(), []() { return std::rand() % 100; });

  // Write NPY
  writeNpy(stream, ndarray);

  // Read NPY
  auto rend = readNpy<T>(stream);

  BOOST_CHECK_EQUAL(rend.shape().size(), 2);
  BOOST_CHECK_EQUAL(rend.shape()[0], 50);
  BOOST_CHECK_EQUAL(rend.shape()[1], 2);
  BOOST_CHECK_EQUAL(rend.size(), ndarray.size());
  BOOST_CHECK_EQUAL_COLLECTIONS(ndarray.begin(), ndarray.end(), rend.begin(), rend.end());
}

BOOST_AUTO_TEST_CASE_TEMPLATE(Npy1d_python_test, T, array_type) {
  Elements::TempFile file(std::string("npy_1d_test_") + typeid(T).name() + "_%%.npy");

  // Construct NdArray
  NdArray<T> ndarray({100});
  std::generate(ndarray.begin(), ndarray.end(), []() { return std::rand() % 100; });

  // Write NPY
  writeNpy(file.path(), ndarray);

  // Read NPY
  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.load(sys.argv[1])
assert a.shape == (100,)
print(a.sum())
)EDOCYP";
  auto                  output = runPython(PYCODE, file.path());

  T sum;
  output >> sum;
  BOOST_CHECK_EQUAL(std::accumulate(ndarray.begin(), ndarray.end(), 0), sum);
}

BOOST_AUTO_TEST_CASE_TEMPLATE(Npy2d_python_test, T, array_type) {
  Elements::TempFile file(std::string("npy_testpy_") + typeid(T).name() + "_%%.npy");

  // Construct NdArray
  NdArray<T> ndarray({50, 2});
  std::generate(ndarray.begin(), ndarray.end(), []() { return std::rand() % 100; });

  // Write NPY
  writeNpy(file.path(), ndarray);

  // Read NPY
  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.load(sys.argv[1])
assert a.shape == (50, 2)
print((a[:,0] * a[:,1]).sum())
)EDOCYP";
  auto                  output = runPython(PYCODE, file.path());

  // Must match
  T expected = 0;
  for (size_t i = 0; i < ndarray.shape()[0]; ++i) {
    expected += ndarray.at(i, 0) * ndarray.at(i, 1);
  }

  T weighted_sum;
  output >> weighted_sum;
  BOOST_CHECK_EQUAL(expected, weighted_sum);
}

BOOST_AUTO_TEST_CASE(Npy2d_frompython_test) {
  Elements::TempFile file("npy_test_frompython_%%.npy");

  // Write NPY from Python
  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.save(sys.argv[1], np.arange(0, 100, dtype='=u4').reshape(2, 5, 10))
)EDOCYP";
  runPython(PYCODE, file.path());

  // Read
  auto ndarray = readNpy<uint32_t>(file.path());

  BOOST_CHECK_EQUAL(ndarray.shape().size(), 3);
  BOOST_CHECK_EQUAL(ndarray.shape()[0], 2);
  BOOST_CHECK_EQUAL(ndarray.shape()[1], 5);
  BOOST_CHECK_EQUAL(ndarray.shape()[2], 10);
}

BOOST_AUTO_TEST_CASE(Npy_badtype_test) {
  std::stringstream stream;

  // Construct NdArray
  NdArray<double> ndarray({50, 2});
  std::generate(ndarray.begin(), ndarray.end(), []() { return std::rand() % 100; });

  // Write NPY
  writeNpy(stream, ndarray);

  // Read NPY
  BOOST_CHECK_THROW(readNpy<int64_t>(stream), Elements::Exception);
}

BOOST_AUTO_TEST_CASE(Npy_badendian_test) {
  Elements::TempFile file(std::string("npy_testpy_endian_%%.npy"));

  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
np.save(sys.argv[1], np.arange(100, 400, dtype='>i8'))
)EDOCYP";

  runPython(PYCODE, file.path());

  BOOST_CHECK_THROW(readNpy<int64_t>(file.path()), Elements::Exception);
}

BOOST_AUTO_TEST_CASE(AttrNames_test) {
  Elements::TempFile file(std::string("npy_testpy_attrs_%%.npy"));

  // Construct NdArray
  const std::vector<std::string> attr_names{"ID", "SED", "PDZ"};
  NdArray<int>                   named{{20}, attr_names};

  for (size_t i = 0; i < named.shape()[0]; ++i) {
    named.at(i, "ID")  = i;
    named.at(i, "SED") = i * 2;
    named.at(i, "PDZ") = i * 10 + 5;
  }

  // Write
  writeNpy(file.path(), named);

  // Read from Python
  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.load(sys.argv[1])
assert a.shape == (20,)
assert len(a.dtype) == 3
assert set(a.dtype.names) == {'ID', 'SED', 'PDZ'}

for i in range(20):
  assert a[i]['ID'] == i
  assert a[i]['SED'] == i * 2
  assert a[i]['PDZ'] == i * 10 + 5
)EDOCYP";

  runPython(PYCODE, file.path());
}

BOOST_AUTO_TEST_CASE(ReadAttrNames_test) {
  Elements::TempFile file(std::string("npy_testpy_read_attrs_%%.npy"));

  std::vector<std::string> expected_attrs{"a", "b"};

  // Write from Python
  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np

a = np.array([(1, 2), (3, 4), (5, 6), (7, 8)], dtype=[('a', np.int16), ('b', np.int16)])
np.save(sys.argv[1], a)
)EDOCYP";

  runPython(PYCODE, file.path());

  // Read
  auto array = readNpy<int16_t>(file.path());
  BOOST_CHECK_EQUAL(array.shape().size(), 2);
  BOOST_CHECK_EQUAL(array.shape()[0], 4);
  BOOST_CHECK_EQUAL(array.shape()[1], 2);

  auto attrs = array.attributes();
  BOOST_CHECK_EQUAL_COLLECTIONS(attrs.begin(), attrs.end(), expected_attrs.begin(), expected_attrs.end());

  // Check values
  for (size_t i = 0; i < 4; ++i) {
    BOOST_CHECK_EQUAL(array.at(i, "a"), i * 2 + 1);
    BOOST_CHECK_EQUAL(array.at(i, "b"), i * 2 + 2);
  }
}

BOOST_AUTO_TEST_CASE(AttrNames_mixed_test) {
  Elements::TempFile file(std::string("npy_testpy_read_attrs_%%.npy"));

  // Write from Python
  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np

a = np.array([(1, 2), (3, 4), (5, 6), (7, 8)], dtype=[('a', np.int16), ('b', np.int64)])
np.save(sys.argv[1], a)
)EDOCYP";

  runPython(PYCODE, file.path());

  // Read
  BOOST_CHECK_THROW(readNpy<int16_t>(file.path()), std::invalid_argument);
}

BOOST_AUTO_TEST_SUITE_END()
