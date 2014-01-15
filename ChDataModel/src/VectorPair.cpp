/*
 * VectorPair.cpp
 *
 * Created on: May 10, 2013
 *     Author: Pavel Binko
 */

#include <stdexcept>
#include <iostream>
#include <algorithm>

#include "ChDataModel/VectorPair.h"
#include "ElementsKernel/ElementsException.h"

using namespace std;

namespace ChDataModel {

//------------------------------------------------------------------------------

VectorPair::VectorPair(const std::vector<double> & x,
    const std::vector<double> & y, bool check_sort_unique) {

  // Check the size always
  if (x.size() == y.size()) {
    m_x = x;
    m_y = y;
  } else {
    throw ElementsException(
        "DataModel::VectorPair : The vectors provided in the constructor do not have the same length.");
  }

  // Check if sorted and unique only on request
  if (true == check_sort_unique) {

    vector<double> tempVector = m_x;

    std::sort (tempVector.begin(), tempVector.end());
    if (tempVector != m_x) {
      throw ElementsException(
          "DataModel::VectorPair : The values of the vector X are not sorted.");
    }

    std::unique (tempVector.begin(), tempVector.end());
    if (tempVector != m_x) {
      throw ElementsException(
          "DataModel::VectorPair : The values of the vector X are not unique.");
    }

  }

} // Eof VectorPair::VectorPair

//------------------------------------------------------------------------------

// Get i-th value on the X axis
double VectorPair::getX(const int i) const {
  try {
    return m_x.at(i);
  } catch (const std::out_of_range& oor) {
    throw ElementsException(
        "DataModel::VectorPair::getX : Index is out of range.");
  }
}

//------------------------------------------------------------------------------

// Get i-th value on the Y axis
double VectorPair::getY(const int i) const {
  try {
    return m_y.at(i);
  } catch (const std::out_of_range& oor) {
    throw ElementsException(
        "DataModel::VectorPair::getY : Index is out of range.");
  }
}

//-----------------------------------------------------------------------------
// Print method

void VectorPair::printVectorPair() {

  for (size_t i=0; i < m_x.size(); ++i) {
    cout << "X = " << m_x[i] << " Y = " << m_y[i] << endl;
  }

} // Eof Filter::printVectorPair

//------------------------------------------------------------------------------

} /* namespace ChDataModel */
