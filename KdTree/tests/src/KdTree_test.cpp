/**
 * @copyright (C) 2021 Euclid Science Ground Segment
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

#include "KdTree/KdTree.h"
#include <boost/test/unit_test.hpp>

//-----------------------------------------------------------------------------

struct DataNode {
  std::array<double, 3> m_coords;
  std::string           m_label;
};

//-----------------------------------------------------------------------------

namespace KdTree {
template <>
struct KdTreeTraits<DataNode> {
  static double getCoord(const DataNode& t, size_t index) {
    BOOST_ASSERT(index < 3);
    return t.m_coords[index];
  }
};
}  // namespace KdTree

//-----------------------------------------------------------------------------

struct KdTreeFixture {
  std::vector<DataNode> nodes;

  // nodes contain a 3x3x3 cube, each intersection contains the ascii character corresponding to
  // '0' + its position within the array
  KdTreeFixture() : nodes{3 * 3 * 3} {
    for (int x = 0; x < 3; ++x) {
      for (int y = 0; y < 3; ++y) {
        for (int z = 0; z < 3; ++z) {
          int i             = z + y * 3 + x * 9;
          nodes[i].m_coords = {double(x), double(y), double(z)};
          nodes[i].m_label  = std::string(1, '0' + i);
        }
      }
    }
  }

  static std::vector<char> getLabels(const std::vector<DataNode>& nodes) {
    std::vector<char> labels;
    for (auto& n : nodes) {
      labels.emplace_back(n.m_label[0]);
    }
    std::sort(labels.begin(), labels.end());
    return labels;
  }
};

//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(KdTree_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(KdTreeSingleMatch_test, KdTreeFixture) {
  KdTree::KdTree<DataNode, 3> tree(nodes);
  // There must be a single result
  auto closest = tree.findPointsWithinRadius({1., 1., 1.}, 0.5);
  BOOST_CHECK_EQUAL(closest.size(), 1);
  BOOST_CHECK_EQUAL(closest[0].m_label[0], '=');

  closest = tree.findPointsWithinRadius({2., 1., 2.}, 0.5);
  BOOST_CHECK_EQUAL(closest.size(), 1);
  BOOST_CHECK_EQUAL(closest[0].m_label[0], 'G');
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(KdTreeMultipleMatch_test, KdTreeFixture) {
  const std::vector<char> expected111{'4', ':', '<', '=', '>', '@', 'F'};
  const std::vector<char> expected222{'A', 'G', 'I', 'J'};

  KdTree::KdTree<DataNode, 3> tree(nodes);

  // Center
  auto closest = tree.findPointsWithinRadius({1., 1., 1.}, 1.1);
  BOOST_CHECK_EQUAL(closest.size(), 7);
  auto found_labels = getLabels(closest);
  BOOST_CHECK_EQUAL_COLLECTIONS(found_labels.begin(), found_labels.end(), expected111.begin(), expected111.end());

  // Corner
  closest = tree.findPointsWithinRadius({2., 2., 2.}, 1.1);
  BOOST_CHECK_EQUAL(closest.size(), 4);
  found_labels = getLabels(closest);
  BOOST_CHECK_EQUAL_COLLECTIONS(found_labels.begin(), found_labels.end(), expected222.begin(), expected222.end());
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(KdTreeNoMatch_test, KdTreeFixture) {
  KdTree::KdTree<DataNode, 3> tree(nodes);

  auto closest = tree.findPointsWithinRadius({10., 1., 1.}, 0.5);
  BOOST_CHECK(closest.empty());

  closest = tree.findPointsWithinRadius({1.5, 1., 1.}, 0.3);
  BOOST_CHECK(closest.empty());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(KdTreeEmpty_test) {
  KdTree::KdTree<DataNode> tree({});

  auto closest = tree.findPointsWithinRadius({1., 1.}, 0.5);
  BOOST_CHECK(closest.empty());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
