/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#include "KdTree/KdTree.h"
#include <array>
#include <boost/test/unit_test.hpp>
#include <cmath>

//-----------------------------------------------------------------------------

struct DataNode {
  std::array<double, 3> m_coords;
  uint32_t              m_label = 0;
};

//-----------------------------------------------------------------------------

namespace KdTree {
template <>
struct KdTreeTraits<DataNode> {
  static double getCoord(const DataNode& t, size_t index) {
    BOOST_ASSERT(index < 3);
    return t.m_coords[index];
  }

  static double distance(const DataNode& a, const DataNode& b) {
    double d = 0;
    for (std::size_t i = 0; i < a.m_coords.size(); ++i) {
      double delta = a.m_coords[i] - b.m_coords[i];
      d += delta * delta;
    }
    return std::sqrt(d);
  }

  static std::size_t getDimensions(const DataNode& n) {
    return n.m_coords.size();
  }
};
}  // namespace KdTree

//-----------------------------------------------------------------------------

struct KdTreeFixture {
  std::vector<DataNode> nodes;

  // nodes contain a 3x3x3 cube, each intersection contains the ascii character corresponding to
  // '0' + its position within the array
  KdTreeFixture() : nodes{9 * 9 * 9} {
    for (int x = 0; x < 9; ++x) {
      for (int y = 0; y < 9; ++y) {
        for (int z = 0; z < 9; ++z) {
          int i             = z + y * 9 + x * 81;
          nodes[i].m_coords = {static_cast<double>(x), static_cast<double>(y), static_cast<double>(z)};
          nodes[i].m_label  = z + y * 10 + x * 100;
        }
      }
    }
  }

  static std::vector<int32_t> getLabels(const std::vector<DataNode>& nodes) {
    std::vector<int32_t> labels;
    std::transform(nodes.begin(), nodes.end(), std::back_inserter(labels), [](const DataNode& n) { return n.m_label; });
    std::sort(labels.begin(), labels.end());
    return labels;
  }
};

//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(KdTree_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(KdTreeSingleMatch_test, KdTreeFixture) {
  KdTree::KdTree<DataNode> tree(nodes, 3);
  // There must be a single result
  auto closest = tree.findPointsWithinRadius({1., 1., 1.}, 0.5);
  BOOST_CHECK_EQUAL(closest.size(), 1);
  BOOST_CHECK_EQUAL(closest[0].m_label, 111);

  closest = tree.findPointsWithinRadius({2., 1., 2.}, 0.5);
  BOOST_CHECK_EQUAL(closest.size(), 1);
  BOOST_CHECK_EQUAL(closest[0].m_label, 212);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(KdTreeMultipleMatch_test, KdTreeFixture) {
  const std::vector<int32_t> expected111{11, 101, 110, 111, 112, 121, 211};
  const std::vector<int32_t> expected888{788, 878, 887, 888};
  const std::vector<int32_t> expected555{455, 545, 554, 555, 556, 565, 655};

  KdTree::KdTree<DataNode> tree(nodes, 3);

  // Center
  auto closest = tree.findPointsWithinRadius({1., 1., 1.}, 1.1);
  BOOST_CHECK_EQUAL(closest.size(), expected111.size());
  auto found_labels = getLabels(closest);
  BOOST_CHECK_EQUAL_COLLECTIONS(found_labels.begin(), found_labels.end(), expected111.begin(), expected111.end());

  // Corner
  closest = tree.findPointsWithinRadius({8., 8., 8.}, 1.1);
  BOOST_CHECK_EQUAL(closest.size(), expected888.size());
  found_labels = getLabels(closest);
  BOOST_CHECK_EQUAL_COLLECTIONS(found_labels.begin(), found_labels.end(), expected888.begin(), expected888.end());

  // Middle
  closest = tree.findPointsWithinRadius({5., 5., 5.}, 1.1);
  BOOST_CHECK_EQUAL(closest.size(), expected555.size());
  found_labels = getLabels(closest);
  BOOST_CHECK_EQUAL_COLLECTIONS(found_labels.begin(), found_labels.end(), expected555.begin(), expected555.end());
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(KdTreeNoMatch_test, KdTreeFixture) {
  KdTree::KdTree<DataNode> tree(nodes, 3);

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
