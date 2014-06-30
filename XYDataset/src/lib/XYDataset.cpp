/**
 * @file src/lib/XYDataset.cpp
 *
 * @date Apr 9, 2014
 * @author Nicolas Morisset
 */

#include <utility>
#include <algorithm>
#include <iostream>

#include "ElementsKernel/ElementsException.h"
#include "XYDataset/XYDataset.h"

using namespace std;

namespace XYDataset {

XYDataset::const_iterator XYDataset::begin() const {
  return m_values.cbegin();
}

XYDataset::const_iterator XYDataset::end() const {
  return m_values.cend();
}

unique_ptr<XYDataset> XYDataset::factory(vector<pair<double, double>> vector_pair) {
  return (unique_ptr<XYDataset> (new XYDataset(vector_pair)));
}

unique_ptr<XYDataset> XYDataset::factory(vector<double> x_vector, vector<double> y_vector) {
  size_t x_size = x_vector.size();
  size_t y_size = y_vector.size();
  // Vector must have the same size
  if ( x_size != y_size) {
    throw ElementsException() << " Vectors must have "
                              << "the same size! x size: %d" <<x_size
                              <<"  y_size : %d"<< y_size;
  }

  vector<pair<double, double>> vector_pair;
  vector_pair.reserve(x_size);

  // Make the pair vector
  transform(x_vector.begin(), x_vector.end(), y_vector.begin(), back_inserter(vector_pair),
                 [](double a, double b) { return std::make_pair(a, b); });

  return ( unique_ptr<XYDataset> (new XYDataset(vector_pair)) );
}

} /* namespace XYDataset */
