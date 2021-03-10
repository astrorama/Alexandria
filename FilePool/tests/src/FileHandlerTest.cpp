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

#include "FilePool/FileHandler.h"
#include "ElementsKernel/Temporary.h"
#include <boost/mpl/list.hpp>
#include <boost/test/unit_test.hpp>

#include "TestFileTraits.h"

using namespace Euclid::FilePool;

/**
 * Mock FileManager
 */
struct FileManagerMock : public FileManager {
protected:
  void notifyIntentToOpen(bool) override {
    BOOST_CHECK_EQUAL(n_notified, n_opened);
    ++n_notified;
  }

  void notifyOpenedFile(FileId file_id) override {
    BOOST_CHECK_EQUAL(n_notified, n_opened + 1);
    ++n_opened;
    auto iter = m_files.find(file_id);
    BOOST_REQUIRE(iter != m_files.end());
  }

  void notifyClosedFile(FileId file_id) override {
    BOOST_CHECK_LE(n_closed, n_opened);
    ++n_closed;
    auto iter = m_files.find(file_id);
    BOOST_REQUIRE(iter != m_files.end());
  }

  void notifyUsed(FileId) override {
    ++n_used;
  }

public:
  FileManagerMock() : n_opened(0), n_closed(0), n_notified(0), n_used(0) {}

  unsigned n_opened, n_closed, n_notified, n_used;
};

/**
 * Fixture
 */
struct FileHandlerFixture {
  std::shared_ptr<FileManagerMock> m_file_manager;
  Elements::TempPath               m_path;

  FileHandlerFixture() : m_file_manager(std::make_shared<FileManagerMock>()) {}
};

/**
 * Run the tests for this set of types
 */
#if !__GNUC__ || __GNUC__ > 4
typedef boost::mpl::list<int, CfitsioLike*, std::fstream> file_descriptor_types;
#else
typedef boost::mpl::list<int, CfitsioLike*> file_descriptor_types;
#endif

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FileHandlerTest)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE_TEMPLATE(OpenWriteReadTest, T, file_descriptor_types, FileHandlerFixture) {
  auto        handler = m_file_manager->getFileHandler(m_path.path());
  std::string write_buffer("this is a string to be written to the nice file");
  std::string write_buffer2(" and another string to go there");

  // Write once
  {
    auto write_accessor = handler->template getAccessor<T>(FileHandler::kWrite);
    BOOST_REQUIRE(write_accessor);
    BOOST_CHECK(!handler->isReadOnly());
    BOOST_CHECK(!write_accessor->isReadOnly());
    OpenCloseTrait<T>::write(write_accessor->m_fd, write_buffer);
  }

  BOOST_CHECK_EQUAL(m_file_manager->n_closed, 0);
  BOOST_CHECK_EQUAL(m_file_manager->n_notified, 1);
  BOOST_CHECK_EQUAL(m_file_manager->n_opened, 1);
  BOOST_CHECK_EQUAL(m_file_manager->n_used, 1);

  // Write twice
  // The handler should be reused
  {
    auto write_accessor = handler->template getAccessor<T>(FileHandler::kWrite);
    BOOST_REQUIRE(write_accessor);
    BOOST_CHECK(!handler->isReadOnly());
    BOOST_CHECK(!write_accessor->isReadOnly());
    OpenCloseTrait<T>::write(write_accessor->m_fd, write_buffer2);
  }

  BOOST_CHECK_EQUAL(m_file_manager->n_closed, 0);
  BOOST_CHECK_EQUAL(m_file_manager->n_notified, 1);
  BOOST_CHECK_EQUAL(m_file_manager->n_opened, 1);
  BOOST_CHECK_EQUAL(m_file_manager->n_used, 2);

  // We open for read, so the write handler should be closed and a new handler open
  auto read_accessor = handler->template getAccessor<T>(FileHandler::kRead);

  BOOST_CHECK_EQUAL(m_file_manager->n_closed, 1);
  BOOST_CHECK_EQUAL(m_file_manager->n_notified, 2);
  BOOST_CHECK_EQUAL(m_file_manager->n_opened, 2);
  BOOST_CHECK_EQUAL(m_file_manager->n_used, 3);

  BOOST_REQUIRE(read_accessor);
  BOOST_CHECK(handler->isReadOnly());
  BOOST_CHECK(read_accessor->isReadOnly());
  auto content = OpenCloseTrait<T>::read(read_accessor->m_fd);

  BOOST_CHECK_EQUAL(content, write_buffer + write_buffer2);

  // We open another reader, so a new file descriptor is expected
  handler->template getAccessor<T>(FileHandler::kRead);

  BOOST_CHECK_EQUAL(m_file_manager->n_closed, 1);
  BOOST_CHECK_EQUAL(m_file_manager->n_notified, 3);
  BOOST_CHECK_EQUAL(m_file_manager->n_opened, 3);
  BOOST_CHECK_EQUAL(m_file_manager->n_used, 4);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE_TEMPLATE(OpenWriteBlock, T, file_descriptor_types, FileHandlerFixture) {
  auto        handler = m_file_manager->getFileHandler(m_path.path());
  std::string write_buffer("this is a string to be written to the nice file");
  std::string write_buffer2(" and another string to go there");

  // Can write once
  {
    auto write_accessor = handler->template getAccessor<T>(FileHandler::kWrite);
    BOOST_REQUIRE(write_accessor);
    BOOST_CHECK(!handler->isReadOnly());
    BOOST_CHECK(!write_accessor->isReadOnly());
    OpenCloseTrait<T>::write(write_accessor->m_fd, write_buffer);
  }

  // Open to read
  auto read_accessor = handler->template getAccessor<T>(FileHandler::kRead);
  BOOST_CHECK(read_accessor);

  BOOST_CHECK_EQUAL(m_file_manager->n_closed, 1);
  BOOST_CHECK_EQUAL(m_file_manager->n_notified, 2);
  BOOST_CHECK_EQUAL(m_file_manager->n_opened, 2);
  BOOST_CHECK_EQUAL(m_file_manager->n_used, 2);

  // Should not be able to open to write because the file is kept by read_accessor
  auto write_accessor = handler->template getAccessor<T>(FileHandler::kTryWrite);
  BOOST_CHECK(write_accessor == nullptr);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadDifferentType2, FileHandlerFixture) {
  auto        handler = m_file_manager->getFileHandler(m_path.path());
  std::string content("Genève est à nouveau la capitale suisse du bouchon");

  // Can write once
  {
    auto write_accessor = handler->getAccessor<int>(FileHandler::kWrite);
    BOOST_REQUIRE(write_accessor);
    BOOST_CHECK(!handler->isReadOnly());
    BOOST_CHECK(!write_accessor->isReadOnly());
    OpenCloseTrait<int>::write(write_accessor->m_fd, content);
  }

  // Open as different types
  auto read_stream = handler->getAccessor<CfitsioLike*>(FileHandler::kRead);
  auto read_int    = handler->getAccessor<int>(FileHandler::kRead);

  BOOST_REQUIRE(read_stream && read_int);
  BOOST_REQUIRE_NE(static_cast<void*>(read_stream.get()), static_cast<void*>(read_int.get()));

  // Read with both
  auto stream_content = OpenCloseTrait<CfitsioLike*>::read(read_stream->m_fd);
  auto int_content    = OpenCloseTrait<int>::read(read_int->m_fd);

  BOOST_CHECK_EQUAL(stream_content, content);
  BOOST_CHECK_EQUAL(int_content, content);
}

//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadDifferentTypes2, FileHandlerFixture) {
  auto        handler = m_file_manager->getFileHandler(m_path.path());
  std::string content("Genève est à nouveau la capitale suisse du bouchon");

  // Can write once
  {
    auto write_accessor = handler->getAccessor<int>(FileHandler::kWrite);
    BOOST_REQUIRE(write_accessor);
    BOOST_CHECK(!handler->isReadOnly());
    BOOST_CHECK(!write_accessor->isReadOnly());
    OpenCloseTrait<int>::write(write_accessor->m_fd, content);
  }

  // Open as different types, but letting the first one go out of scope
  {
    auto read_stream    = handler->getAccessor<CfitsioLike*>(FileHandler::kRead);
    auto stream_content = OpenCloseTrait<CfitsioLike*>::read(read_stream->m_fd);
    BOOST_CHECK_EQUAL(stream_content, content);
  }
  // Only the write descriptor!
  BOOST_CHECK_EQUAL(m_file_manager->n_closed, 1);
  {
    auto read_int    = handler->getAccessor<int>(FileHandler::kRead);
    auto int_content = OpenCloseTrait<int>::read(read_int->m_fd);
    BOOST_CHECK_EQUAL(int_content, content);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
