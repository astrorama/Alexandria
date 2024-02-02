/**
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

#include "NdArray/io/Npy.h"
#include "NdArray/io/NpyMmap.h"
#include "TestHelper.h"
#include <ElementsKernel/Temporary.h>
#include <boost/test/unit_test.hpp>
#include <random>

struct RandomGeneratorFixture {
  std::mt19937 rng{std::random_device()()};

  template <typename T>
  std::function<T()> generator() {
    std::uniform_int_distribution<int> dist;
    return [dist, this]() mutable { return static_cast<T>(dist(this->rng) % 100); };
  }
};

using namespace Euclid::NdArray;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(NpyMmap_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(MmapOpen_test, RandomGeneratorFixture) {
  Elements::TempFile file("npy_mmap_%%.npy");

  // Create npy
  NdArray<int32_t> ndarray({50, 10, 40});
  std::generate(ndarray.begin(), ndarray.end(), generator<int32_t>());
  writeNpy(file.path(), ndarray);

  // Open with mmap
  {
    auto mmapped = mmapNpy<int32_t>(file.path());
    BOOST_CHECK_EQUAL(mmapped.shape().size(), 3);
    BOOST_CHECK_EQUAL(mmapped.shape()[0], 50);
    BOOST_CHECK_EQUAL(mmapped.shape()[1], 10);
    BOOST_CHECK_EQUAL(mmapped.shape()[2], 40);
    BOOST_CHECK_EQUAL_COLLECTIONS(ndarray.begin(), ndarray.end(), mmapped.begin(), mmapped.end());
    // Modify a couple of elements
    // Note we start at 1024 so there is no chance they have been generated randomly
    mmapped.at(0, 1, 2)   = 1024 + 42;
    mmapped.at(42, 5, 33) = 1024 + 108;
  }

  // Re-open as regular file
  // Changes should have persisted
  auto read = readNpy<int32_t>(file.path());
  BOOST_CHECK_EQUAL(read.at(0, 1, 2), 1024 + 42);
  BOOST_CHECK_EQUAL(read.at(42, 5, 33), 1024 + 108);
  BOOST_CHECK_EQUAL(read.front(), ndarray.front());
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(MmapOpenPrivate_test, RandomGeneratorFixture) {
  Elements::TempFile file("npy_mmap_%%.npy");

  // Create npy
  NdArray<int32_t> ndarray({50, 10, 40});
  std::generate(ndarray.begin(), ndarray.end(), generator<int32_t>());
  writeNpy(file.path(), ndarray);

  // Open with mmap
  {
    auto mmapped = mmapNpy<int32_t>(file.path(), boost::iostreams::mapped_file_base::priv);
    BOOST_CHECK_EQUAL(mmapped.shape().size(), 3);
    BOOST_CHECK_EQUAL(mmapped.shape()[0], 50);
    BOOST_CHECK_EQUAL(mmapped.shape()[1], 10);
    BOOST_CHECK_EQUAL(mmapped.shape()[2], 40);
    BOOST_CHECK_EQUAL_COLLECTIONS(ndarray.begin(), ndarray.end(), mmapped.begin(), mmapped.end());
    // Modify a couple of elements
    // Note we start at 1024 so there is no chance they have been generated randomly
    mmapped.at(0, 1, 2)   = 1024 + 42;
    mmapped.at(42, 5, 33) = 1024 + 108;

    BOOST_CHECK_EQUAL(mmapped.at(0, 1, 2), 1024 + 42);
    BOOST_CHECK_EQUAL(mmapped.at(42, 5, 33), 1024 + 108);
  }

  // Re-open as regular file
  // Changes should have persisted
  auto read = readNpy<int32_t>(file.path());
  BOOST_CHECK_EQUAL_COLLECTIONS(ndarray.begin(), ndarray.end(), read.begin(), read.end());
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(MmapOpenReadOnly_test, RandomGeneratorFixture) {
  Elements::TempFile file("npy_mmap_%%.npy");

  // Create npy
  NdArray<int32_t> ndarray({50, 10, 40});
  std::generate(ndarray.begin(), ndarray.end(), generator<int32_t>());
  writeNpy(file.path(), ndarray);

  // Open with mmap
  auto mmapped = mmapNpy<int32_t>(file.path(), boost::iostreams::mapped_file_base::readonly);
  BOOST_CHECK_EQUAL(mmapped.shape().size(), 3);
  BOOST_CHECK_EQUAL(mmapped.shape()[0], 50);
  BOOST_CHECK_EQUAL(mmapped.shape()[1], 10);
  BOOST_CHECK_EQUAL(mmapped.shape()[2], 40);
  BOOST_CHECK_EQUAL_COLLECTIONS(ndarray.begin(), ndarray.end(), mmapped.begin(), mmapped.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(MmapCreate_test) {
  Elements::TempFile file("npy_create_mmap_%%.npy");

  {
    auto ndarray = createMmapNpy<double>(file.path(), {100, 2});
    for (size_t i = 0; i < 100; ++i) {
      ndarray.at(i, 0) = i;
      ndarray.at(i, 1) = 2 * i;
    }
  }

  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.load(sys.argv[1])
assert a.dtype == np.float64
assert a.shape == (100, 2)
assert np.isclose(np.average(a[:,0], weights=a[:,1]),66.33333, 1e-3)
)EDOCYP";
  runPython(PYCODE, file.path());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(MmapAppend_test) {
  Elements::TempFile file("npy_resize_mmap_%%.npy");

  auto ndarray = createMmapNpy<double>(file.path(), {100, 2}, {}, 10240);
  for (size_t i = 0; i < 100; ++i) {
    ndarray.at(i, 0) = i;
    ndarray.at(i, 1) = 2 * i;
  }

  NdArray<double> another({50, 2});
  std::fill(another.begin(), another.end(), 4.2);

  ndarray.concatenate(another);

  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.load(sys.argv[1])
assert a.dtype == np.float64
assert a.shape == (150, 2), a.shape
assert np.isclose(np.average(a[0:100,0], weights=a[0:100,1]), 66.33333, 1e-3)
assert np.allclose(a[100:,:], 4.2)
)EDOCYP";
  runPython(PYCODE, file.path());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(MmapAppend_NotEnough_test) {
  Elements::TempFile file("npy_resize_mmap_%%.npy");

  // This allocates only enough for the 100x2 doubles
  auto ndarray = createMmapNpy<double>(file.path(), {100, 2});
  for (size_t i = 0; i < 100; ++i) {
    ndarray.at(i, 0) = i;
    ndarray.at(i, 1) = 2 * i;
  }

  NdArray<double> another({50, 2});
  std::fill(another.begin(), another.end(), 4.2);

  BOOST_CHECK_THROW(ndarray.concatenate(another), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(MmapNamed_test) {
  Elements::TempFile             file("npy_named_mmap_%%.npy");
  const std::vector<std::string> attr_names{"ID", "SED", "PDZ"};

  // Create mmap
  auto ndarray = createMmapNpy<uint64_t>(file.path(), {100}, attr_names);
  BOOST_CHECK_EQUAL(ndarray.shape().size(), 2);
  BOOST_CHECK_EQUAL(ndarray.shape()[0], 100);
  BOOST_CHECK_EQUAL(ndarray.shape()[1], 3);
  auto attrs = ndarray.attributes();
  BOOST_CHECK_EQUAL_COLLECTIONS(attrs.begin(), attrs.end(), attr_names.begin(), attr_names.end());

  // Fill
  for (size_t i = 0; i < ndarray.shape()[0]; ++i) {
    ndarray.at(i, "ID")  = i;
    ndarray.at(i, "SED") = i * 2;
    ndarray.at(i, "PDZ") = i * 10 + 5;
  }

  // Read from Python
  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.load(sys.argv[1])
assert a.shape == (100,)
assert len(a.dtype) == 3
assert set(a.dtype.names) == {'ID', 'SED', 'PDZ'}

for i in range(100):
  assert a[i]['ID'] == i
  assert a[i]['SED'] == i * 2
  assert a[i]['PDZ'] == i * 10 + 5
)EDOCYP";

  runPython(PYCODE, file.path());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ReadAttrNames_test) {
  Elements::TempFile file(std::string("npy_named_mmap_%%.npy"));

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
  auto array = mmapNpy<int16_t>(file.path());
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

  // Modify on the fly
  array.at(0, "a") = 42;
  array.at(0, "b") = 88;
  array.at(3, "a") = 78;

  // The changes must be visible to another process
  constexpr const char* PYCODE2 = R"EDOCYP(
import sys
import numpy as np

a = np.load(sys.argv[1])
assert a.shape == (4,)
assert set(a.dtype.names) == {"a", "b"}
expected = np.array([(42, 88), (3, 4), (5, 6), (78, 8)], dtype=[('a', np.int16), ('b', np.int16)])
assert np.array_equal(expected, a), a
)EDOCYP";

  runPython(PYCODE2, file.path());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NamedAppend_test) {
  Elements::TempFile             file("npy_named_resize_mmap_%%.npy");
  const std::vector<std::string> attr_names{"X", "Y"};

  auto ndarray = createMmapNpy<double>(file.path(), {100}, attr_names, 10240);
  for (size_t i = 0; i < 100; ++i) {
    ndarray.at(i, "X") = i;
    ndarray.at(i, "Y") = 2 * i;
  }

  NdArray<double> another({50}, attr_names);
  std::fill(another.begin(), another.end(), 4.2);

  ndarray.concatenate(another);

  constexpr const char* PYCODE = R"EDOCYP(
import sys
import numpy as np
a = np.load(sys.argv[1])
assert a.shape == (150,), a.shape
assert np.isclose(np.average(a[0:100]['X'], weights=a[0:100]['Y']), 66.33333, 1e-3)
assert np.allclose(a[100:]['X'], 4.2)
assert np.allclose(a[100:]['Y'], 4.2)
)EDOCYP";
  runPython(PYCODE, file.path());
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(BadDtype_test, RandomGeneratorFixture) {
  Elements::TempFile file("npy_mmap_%%.npy");

  // Create npy
  NdArray<int32_t> ndarray({50, 10, 40});
  std::generate(ndarray.begin(), ndarray.end(), generator<int32_t>());
  writeNpy(file.path(), ndarray);

  // Open with mmap
  BOOST_CHECK_THROW(mmapNpy<float>(file.path()), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
