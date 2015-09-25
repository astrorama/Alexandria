/**
 * @file src/lib/XYDataset.cpp
 *
 * @date Apr 9, 2014
 * @author Nicolas Morisset
 */

#include <utility>
#include <algorithm>
#include <iostream>

#include "ElementsKernel/Exception.h"
#include "XYDataset/XYDataset.h"

using namespace std;

namespace Euclid {
namespace XYDataset {

XYDataset::const_iterator XYDataset::begin() const {
  return m_values.cbegin();
}

XYDataset::const_iterator XYDataset::end() const {
  return m_values.cend();
}

const std::pair<double, double>& XYDataset::front() const {
  return m_values.front();
}

const std::pair<double, double>& XYDataset::back() const {
  return m_values.back();
}

XYDataset XYDataset::factory(vector<pair<double, double>> vector_pair) {
  return (XYDataset(move(vector_pair)));
}

XYDataset XYDataset::factory(const vector<double>& x_vector, const vector<double>& y_vector) {
  size_t x_size = x_vector.size();
  size_t y_size = y_vector.size();
  // Vector must have the same size
  if ( x_size != y_size) {
    throw Elements::Exception() << " Vectors must have "
                              << "the same size! x size: %d" <<x_size
                              <<"  y_size : %d"<< y_size;
  }

  vector<pair<double, double>> vector_pair;
  vector_pair.reserve(x_size);

  // Make the pair vector
  transform(x_vector.begin(), x_vector.end(), y_vector.begin(), back_inserter(vector_pair),
                 [](double a, double b) { return std::make_pair(a, b); });

  return ( XYDataset(move(vector_pair)) );
}

} /* namespace XYDataset */
} // end of namespace Euclid
