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

#include "FilePool/FileManager.h"
#include "ElementsKernel/Temporary.h"
#include <boost/test/unit_test.hpp>

#include "TestFileTraits.h"

using namespace Euclid::FilePool;

/**
 * Dummy policy, since we are only interested on the methods implemented by the parent class
 */
class NoopFileManager : public FileManager {
public:
  NoopFileManager() = default;

protected:
  void notifyIntentToOpen(bool) final {}
  void notifyOpenedFile(FileId) final {}
  void notifyClosedFile(FileId) final {}
};

struct FileManagerFixture {
  std::shared_ptr<FileManager> manager;

  FileManagerFixture() : manager(std::make_shared<NoopFileManager>()) {}
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FileManagerTest)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(DifferentFilesTest, FileManagerFixture) {
  Elements::TempPath temp1, temp2;

  BOOST_CHECK(!manager->hasHandler(temp1.path()));
  BOOST_CHECK(!manager->hasHandler(temp2.path()));

  auto handler1 = manager->getFileHandler(temp1.path());

  BOOST_CHECK(manager->hasHandler(temp1.path()));
  BOOST_CHECK(!manager->hasHandler(temp2.path()));

  auto handler2 = manager->getFileHandler(temp2.path());

  BOOST_CHECK(manager->hasHandler(temp1.path()));
  BOOST_CHECK(manager->hasHandler(temp2.path()));

  BOOST_CHECK(handler1 != nullptr && handler2 != nullptr);
  BOOST_CHECK_NE(handler1, handler2);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SameHandlerTest, FileManagerFixture) {
  Elements::TempPath temp;

  BOOST_CHECK(!manager->hasHandler(temp.path()));

  auto handler1 = manager->getFileHandler(temp.path());
  auto handler2 = manager->getFileHandler(temp.path());

  BOOST_CHECK(handler1);
  BOOST_CHECK_EQUAL(handler1, handler2);
  BOOST_CHECK(manager->hasHandler(temp.path()));
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(RelativeSameHandlerTest, FileManagerFixture) {
  Elements::TempPath temp;
  auto               name   = temp.path().filename();
  auto               parent = temp.path().parent_path();

  // Build something like /tmp/../tmp/blah
  auto alternative = parent / ".." / parent.filename() / name;
  BOOST_REQUIRE_NE(temp.path(), alternative);
  BOOST_TEST_MESSAGE(alternative.native());

  auto handler1 = manager->getFileHandler(temp.path());

  BOOST_CHECK(manager->hasHandler(temp.path()));
  BOOST_CHECK(manager->hasHandler(alternative));

  auto handler2 = manager->getFileHandler(alternative);

  BOOST_CHECK(handler1);
  BOOST_CHECK_EQUAL(handler1, handler2);
}

//----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SymlinkSameHandlerTest, FileManagerFixture) {
  Elements::TempFile temp;
  Elements::TempPath symlink;

  BOOST_TEST_MESSAGE(temp.path() << " -> " << symlink.path());
  create_symlink(temp.path(), symlink.path());

  auto handler1 = manager->getFileHandler(temp.path());

  BOOST_CHECK(manager->hasHandler(temp.path()));
  BOOST_CHECK(manager->hasHandler(symlink.path()));

  auto handler2 = manager->getFileHandler(symlink.path());

  BOOST_CHECK(handler1);
  BOOST_CHECK_EQUAL(handler1, handler2);
}

//----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(NewHandlerTest, FileManagerFixture) {
  Elements::TempFile temp;

  BOOST_CHECK(!manager->hasHandler(temp.path()));
  {
    auto handler1 = manager->getFileHandler(temp.path());
    BOOST_CHECK(handler1);
    BOOST_CHECK(manager->hasHandler(temp.path()));
  }
  // handler1 was the only reference, so when it got destroyed it should have been de-registered
  BOOST_CHECK(!manager->hasHandler(temp.path()));
  auto handler2 = manager->getFileHandler(temp.path());
  BOOST_CHECK(handler2);
  BOOST_CHECK(manager->hasHandler(temp.path()));
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
