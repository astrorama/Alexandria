/**
 * @file tests/src/CachedProvider_test.cpp
 * @date 08/14/18
 * @author aalvarez
 *
 * @copyright (C) 2012-2020 Euclid Science Ground Segment
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
 *
 */

#include <boost/test/unit_test.hpp>
#include <ElementsKernel/Exception.h>

#include "XYDataset/CachedProvider.h"

using namespace Euclid::XYDataset;


namespace boost::test_tools::tt_detail {
template<typename T, typename U>
struct print_log_value<std::pair<T,U>> {
  void operator()(std::ostream &os, const std::pair<T, U> &pair) {
    os << "<" << pair.first << "," << pair.second << ">";
  }
};
}


struct MockProvider: public XYDatasetProvider {
  int m_list_calls = 0;
  int m_data_calls = 0;

  std::map<std::string, std::vector<QualifiedName>> m_listing;
  std::map<QualifiedName, XYDataset> m_dataset;
  std::vector<double> m_x = {1., 2., 3.};
  std::vector<double> m_y = {0., 0.5, 0.6};

  virtual ~MockProvider() = default;

  MockProvider() {
    m_listing["A"] = {};
    m_listing["B"] = {{"1"}, {"2"}, {"3"}};
    m_listing["C"] = {{"x"}, {"y"}};

    m_dataset.emplace(QualifiedName{"1"}, std::move(XYDataset::factory(m_x, m_y)));
    m_dataset.emplace(QualifiedName{"2"}, std::move(XYDataset::factory(m_y, m_x)));
  }

  std::vector<QualifiedName> listContents(const std::string& group) override {
    ++m_list_calls;
    auto i = m_listing.find(group);
    if (i == m_listing.end()) {
      return {};
    }
    return i->second;
  }

  std::unique_ptr<XYDataset> getDataset(const QualifiedName& qualified_name) override {
    ++m_data_calls;
    auto i = m_dataset.find(qualified_name);
    if (i == m_dataset.end()) {
      return nullptr;
    }
    return std::unique_ptr<XYDataset>{new XYDataset{i->second}};
  }
};

struct CachedProvider_fixture {
  std::shared_ptr<MockProvider> mock_provider{new MockProvider{}};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (CachedProvider_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(listContents_missing_test, CachedProvider_fixture) {
  CachedProvider cache{mock_provider};

  BOOST_CHECK_EQUAL(cache.listContents("V").size(), 0);
  BOOST_CHECK_EQUAL(mock_provider->m_list_calls, 1);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(listContents_test, CachedProvider_fixture) {
  CachedProvider cache{mock_provider};

  auto list_return = cache.listContents("A");
  BOOST_CHECK_EQUAL_COLLECTIONS(
    list_return.begin(), list_return.end(), mock_provider->m_listing["A"].begin(), mock_provider->m_listing["A"].end()
  );

  list_return = cache.listContents("B");
  BOOST_CHECK_EQUAL_COLLECTIONS(
    list_return.begin(), list_return.end(), mock_provider->m_listing["B"].begin(), mock_provider->m_listing["B"].end()
  );

  list_return = cache.listContents("C");
  BOOST_CHECK_EQUAL_COLLECTIONS(
    list_return.begin(), list_return.end(), mock_provider->m_listing["C"].begin(), mock_provider->m_listing["C"].end()
  );

  BOOST_CHECK_EQUAL(mock_provider->m_list_calls, 3);

  // Repeat
  list_return = cache.listContents("A");
  BOOST_CHECK_EQUAL_COLLECTIONS(
    list_return.begin(), list_return.end(), mock_provider->m_listing["A"].begin(), mock_provider->m_listing["A"].end()
  );

  list_return = cache.listContents("B");
  BOOST_CHECK_EQUAL_COLLECTIONS(
    list_return.begin(), list_return.end(), mock_provider->m_listing["B"].begin(), mock_provider->m_listing["B"].end()
  );

  list_return = cache.listContents("C");
  BOOST_CHECK_EQUAL_COLLECTIONS(
    list_return.begin(), list_return.end(), mock_provider->m_listing["C"].begin(), mock_provider->m_listing["C"].end()
  );

  BOOST_CHECK_EQUAL(mock_provider->m_list_calls, 3);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getDataset_missing_test, CachedProvider_fixture) {
  CachedProvider cache{mock_provider};

  BOOST_CHECK(cache.getDataset(QualifiedName{"V"}) == nullptr);
  BOOST_CHECK_EQUAL(mock_provider->m_data_calls, 1);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getDataSet_test, CachedProvider_fixture) {
  CachedProvider cache{mock_provider};

  auto dataset_ptr = cache.getDataset(QualifiedName{"1"});
  BOOST_CHECK_EQUAL_COLLECTIONS(
    dataset_ptr->begin(), dataset_ptr->end(),
    mock_provider->m_dataset.at({"1"}).begin(), mock_provider->m_dataset.at({"1"}).end()
  );

  dataset_ptr = cache.getDataset(QualifiedName{"2"});
  BOOST_CHECK_EQUAL_COLLECTIONS(
    dataset_ptr->begin(), dataset_ptr->end(),
    mock_provider->m_dataset.at({"2"}).begin(), mock_provider->m_dataset.at({"2"}).end()
  );

  BOOST_CHECK_EQUAL(mock_provider->m_data_calls, 2);

  dataset_ptr = cache.getDataset(QualifiedName{"1"});
  BOOST_CHECK_EQUAL_COLLECTIONS(
    dataset_ptr->begin(), dataset_ptr->end(),
    mock_provider->m_dataset.at({"1"}).begin(), mock_provider->m_dataset.at({"1"}).end()
  );

  dataset_ptr = cache.getDataset(QualifiedName{"2"});
  BOOST_CHECK_EQUAL_COLLECTIONS(
    dataset_ptr->begin(), dataset_ptr->end(),
    mock_provider->m_dataset.at({"2"}).begin(), mock_provider->m_dataset.at({"2"}).end()
  );

  BOOST_CHECK_EQUAL(mock_provider->m_data_calls, 2);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


