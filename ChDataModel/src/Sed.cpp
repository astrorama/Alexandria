/*
 * Sed.cpp
 *
 * Created on: May 10, 2013
 *     Author: Pavel Binko
 */

#include "ChDataModel/Sed.h"

using namespace std;

namespace ChDataModel {

//-----------------------------------------------------------------------------
// Constructor with assignment of the sed name

Sed::Sed(vector<double> & waveLengths, vector<double> & intensities,
    SedNames sedName, bool check_sort_unique) :
    m_sed_curve(waveLengths, intensities, check_sort_unique), m_name(sedName) {
}

//-----------------------------------------------------------------------------
// Constructor with assignment of the sed name

Sed::Sed(ChDataModel::VectorPair vectorPair, SedNames sedName) :
    m_sed_curve(vectorPair), m_name(sedName) {
}

//-----------------------------------------------------------------------------
// Print method

void Sed::printSed() {

  cout << "Sed Name = " << m_name << endl;
  cout << "Wave length  |  Intensity" << endl;

  m_sed_curve.printVectorPair();

  cout << endl;

} // Eof Filter::printFilter

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
