/*
 * Filter.cpp
 *
 * Created on: May 10, 2013
 *     Author: Pavel Binko
 */

#include "ChDataModel/Filter.h"

using namespace std;

namespace ChDataModel {

//-----------------------------------------------------------------------------
// Constructor with assignment of the filter name

Filter::Filter(std::vector<double> & waveLengths,
    std::vector<double> & filterValues, FilterTypes filterType,
    FilterNames filterName, bool check_sort_unique) :
    m_filter_curve(waveLengths, filterValues, check_sort_unique),
    m_type(filterType), m_name(filterName) {
}

//-----------------------------------------------------------------------------
// Constructor with assignment of the filter name

Filter::Filter(ChDataModel::VectorPair vectorPair, FilterTypes filterType,
    FilterNames filterName) :
    m_filter_curve(vectorPair), m_type(filterType),
    m_name(filterName) {
}

//-----------------------------------------------------------------------------
// Print method

void Filter::printFilter() {

  cout << "Filter Type = " << m_type << endl;
  cout << "Filter Name = " << m_name << endl;
  cout << "Wave length  |  Efficiency" << endl;

  m_filter_curve.printVectorPair();

  cout << endl;

} // Eof Filter::printFilter

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
