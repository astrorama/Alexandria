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

#include <boost/test/unit_test.hpp>
#include <ElementsKernel/Temporary.h>
#include "NdArray/io/Npy.h"
#include "NdArray/io/NpyMmap.h"
#include "TestHelper.h"

using namespace Euclid::NdArray;

BOOST_AUTO_TEST_SUITE(NpyMmap_test)

BOOST_AUTO_TEST_CASE(MmapOpen_test) {
  Elements::TempFile file("npy_mmap_%%.npy");

  // Create npy
  NdArray<int32_t> ndarray({50, 10, 40});
  std::generate(ndarray.begin(), ndarray.end(), []() { return std::rand() % 1024; });
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
    mmapped.at(0, 1, 2) = 1024 + 42;
    mmapped.at(42, 5, 33) = 1024 + 108;
  }

  // Re-open as regular file
  // Changes should have persisted
  auto read = readNpy<int32_t>(file.path());
  BOOST_CHECK_EQUAL(read.at(0, 1, 2), 1024 + 42);
  BOOST_CHECK_EQUAL(read.at(42, 5, 33), 1024 + 108);
}

BOOST_AUTO_TEST_CASE(MmapOpenPrivate_test) {
  Elements::TempFile file("npy_mmap_%%.npy");

  // Create npy
  NdArray<int32_t> ndarray({50, 10, 40});
  std::generate(ndarray.begin(), ndarray.end(), []() { return std::rand() % 1024; });
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
    mmapped.at(0, 1, 2) = 1024 + 42;
    mmapped.at(42, 5, 33) = 1024 + 108;

    BOOST_CHECK_EQUAL(mmapped.at(0, 1, 2), 1024 + 42);
    BOOST_CHECK_EQUAL(mmapped.at(42, 5, 33), 1024 + 108);
  }

  // Re-open as regular file
  // Changes should have persisted
  auto read = readNpy<int32_t>(file.path());
  BOOST_CHECK_EQUAL_COLLECTIONS(ndarray.begin(), ndarray.end(), read.begin(), read.end());
}

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

BOOST_AUTO_TEST_CASE(MmapAppend_test) {
  Elements::TempFile file("npy_resize_mmap_%%.npy");

  auto ndarray = createMmapNpy<double>(file.path(), {100, 2});
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

BOOST_AUTO_TEST_SUITE_END()
