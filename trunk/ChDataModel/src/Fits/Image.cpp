/**
 * @file Image.cpp
 *
 * Created on: Sep 18, 2013
 *     Author: Pavel Binko
 */

#include "ChDataModel/Fits/Image.h"
#include "ChDataModel/Fits/Header.h"
#include "ChDataModel/Fits/Keyword.h"

#include <iostream>
#include <iterator>     // ostream_iterator
using namespace std;

namespace ChDataModel {
namespace Fits {

//------------------------------------------------------------------------------

Image::Image(const Image & image) {
  m_header = new Header(*(image.m_header));
  m_data = image.m_data;
}

//------------------------------------------------------------------------------

Image::~Image() {
  delete m_header;
}

//------------------------------------------------------------------------------

Image & Image::operator =(const Image & image) {
  m_header = new Header(*image.m_header);
  m_data = image.m_data;
  return *this;
}

//------------------------------------------------------------------------------

bool Image::operator ==(const Image & image) const {

  // Compare the data size first
  if (m_data.size() != image.m_data.size()) {
    return false;
  }

  // Compare the image data elements
  for (int i = 0; i < m_data.size(); i++) {
    if (m_data(i) != image.m_data(i)) {
      return false;
    }
  }

  // If the data are the same, compare the headers) and keywords
  return *m_header == *image.m_header;

}

//------------------------------------------------------------------------------

long Image::getSizeX() {
  return dynamic_cast<LongKeyword &>(m_header->getKeyword("NAXIS1")).getValue();
}

//------------------------------------------------------------------------------

long Image::getSizeY() {
  return dynamic_cast<LongKeyword &>(m_header->getKeyword("NAXIS2")).getValue();
}

//------------------------------------------------------------------------------

void Image::setSizeX(long sizeX) {
  LongKeyword & s = m_header->getKeyword("NAXIS1");
  s = sizeX;
}

//------------------------------------------------------------------------------

void Image::setSizeY(long sizeY) {
  LongKeyword & s = m_header->getKeyword("NAXIS2");
  s = sizeY;
}

//------------------------------------------------------------------------------

void Image::print() {

  cout << "**********************************************************" << endl;
  cout << "*                                                        *" << endl;
  cout << "*         Image HDU contents                             *" << endl;
  cout << "*                                                        *" << endl;
  cout << "**********************************************************" << endl;

  // Print all keywords from the header
  if(m_header != nullptr) {
    m_header->print();
  }
  else {
    cout << "----------------------------------------------------------"
        << endl;
    cout << "          Header not loaded" << endl;
    cout << "----------------------------------------------------------"
        << endl;
  }

  // Print contents of the image
  if (m_data.size() != 0) {
    long axisX = this->getSizeX();
    long axisY = this->getSizeY();

    cout << "----------------------------------------------------------"
        << endl;
    cout << "          Image contents" << endl << endl;
    cout << "     Length of the axis X = " << axisX << endl;
    cout << "     Length of the axis Y = " << axisY << endl;
    cout << "----------------------------------------------------------"
        << endl;

    for (long j = 0; j < axisY; j += 10) {
      ostream_iterator<short> c(cout, "\t");
      copy(&m_data(j * axisX), &m_data((j + 1) * axisX - 1), c);
      cout << '\n';
    }
  }
  else {
    cout << "----------------------------------------------------------"
        << endl;
    cout << "           Image not loaded" << endl;
    cout << "----------------------------------------------------------"
        << endl;
  }

} // Eof Image::print

//------------------------------------------------------------------------------

} /* namespace Fits */
} /* namespace ChDataModel */

