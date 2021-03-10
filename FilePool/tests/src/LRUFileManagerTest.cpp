/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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

#include "FilePool/LRUFileManager.h"
#include "ElementsKernel/Temporary.h"
#include <boost/test/unit_test.hpp>

#include "TestFileTraits.h"

using namespace Euclid::FilePool;

struct LRUFixture {
  static constexpr int            NFILES = 5;
  std::vector<Elements::TempPath> paths;

  LRUFixture() : paths(NFILES) {
    for (auto& path : paths) {
      std::ofstream stream(path.path().native());
      stream << "THIS IS FILE " << path.path().native();
    }
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(LRUFileManagerTest)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(TestLRU, LRUFixture) {
  constexpr int LIMIT = 3;

  LRUFileManager                     manager(LIMIT);
  std::map<FileManager::FileId, int> descriptors;
  std::vector<FileManager::FileId>   order_closed;

  auto close_callback = [&](FileManager::FileId id) mutable {
    order_closed.push_back(id);
    auto iter = descriptors.find(id);
    manager.close(iter->first, iter->second);
    descriptors.erase(iter);
    return true;
  };

  // Open all files
  std::vector<FileManager::FileId> order_opened;
  for (auto& path : paths) {
    auto pair = manager.open<int>(path.path(), false, close_callback);
    descriptors.emplace(pair);
    order_opened.push_back(pair.first);
  }

  // There are more files than the maximum, so the first opened should have been closed
  BOOST_REQUIRE_EQUAL(order_closed.size(), NFILES - LIMIT);
  for (int i = 0; i < NFILES - LIMIT; ++i) {
    BOOST_CHECK_EQUAL(order_opened[i], order_closed[i]);
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(TestLRUMultiple, LRUFixture) {
  constexpr int LIMIT = 3;

  LRUFileManager                     manager(LIMIT);
  std::map<FileManager::FileId, int> descriptors;
  std::vector<FileManager::FileId>   order_closed;

  auto close_callback = [&](FileManager::FileId id) mutable {
    order_closed.push_back(id);
    auto iter = descriptors.find(id);
    manager.close(iter->first, iter->second);
    descriptors.erase(iter);
    return true;
  };

  // Open first three
  std::vector<FileManager::FileId> order_opened;
  for (auto i = paths.begin(); i != paths.end() && order_opened.size() < 3; ++i) {
    auto pair = manager.open<int>(i->path(), false, close_callback);
    descriptors.emplace(pair);
    order_opened.push_back(pair.first);
  }
  BOOST_CHECK_EQUAL(order_closed.size(), 0);
  BOOST_CHECK_EQUAL(manager.getLimit(), 3);
  BOOST_CHECK_EQUAL(manager.getUsed(), 3);
  BOOST_CHECK_EQUAL(manager.getAvailable(), 0);

  // Re-use two and three
  manager.notifyUsed(order_opened[0]);
  manager.notifyUsed(order_opened[1]);

  // Open two more
  for (auto i = paths.begin(); i != paths.end() && order_opened.size() < 5; ++i) {
    auto pair = manager.open<int>(i->path(), false, close_callback);
    descriptors.emplace(pair);
    order_opened.push_back(pair.first);
  }

  BOOST_CHECK_EQUAL(order_closed.size(), 2);
  BOOST_CHECK_EQUAL(manager.getUsed(), 3);
  BOOST_CHECK_EQUAL(manager.getAvailable(), 0);

  // Since file 0 and 1 were re-used, the third opened should be gone first
  BOOST_CHECK_EQUAL(order_closed[0], order_opened[2]);
  BOOST_CHECK_EQUAL(order_closed[1], order_opened[0]);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(TestLruMixed, LRUFixture) {
  constexpr int LIMIT = 3;

  LRUFileManager                     manager(LIMIT);
  std::map<FileManager::FileId, int> descriptors;

  auto close_callback = [&](FileManager::FileId id) mutable {
    auto iter = descriptors.find(id);
    manager.close(iter->first, iter->second);
    return true;
  };

  manager.open<int>(paths[0].path(), false, close_callback);
  manager.open<CfitsioLike*>(paths[1].path(), false, close_callback);
#if !__GNUC__ || __GNUC__ > 4
  manager.open<std::fstream>(paths[2].path(), false, close_callback);

  BOOST_CHECK_EQUAL(manager.getLimit(), 3);
  BOOST_CHECK_EQUAL(manager.getUsed(), 3);
  BOOST_CHECK_EQUAL(manager.getAvailable(), 0);
#else
  BOOST_CHECK_EQUAL(manager.getLimit(), 3);
  BOOST_CHECK_EQUAL(manager.getUsed(), 2);
  BOOST_CHECK_EQUAL(manager.getAvailable(), 1);
#endif
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
