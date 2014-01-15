/**
 * @file Image.h
 *
 * Created on: Sep 18, 2013
 *     Author: Pavel Binko
 */

#ifndef IMAGE_H_
#define IMAGE_H_

#include <valarray>
#include <Eigen/Core>

namespace ChDataModel {
namespace Fits {

//------------------------------------------------------------------------------

class Header;

//------------------------------------------------------------------------------

/**
 * @class Image
 * @brief
 *   The Image class contains the image header and image data.
 */
class Image {

public:

  /**
   * @brief Constructor
   */
  Image() {
  }

  /**
   * @brief Copy constructor
   * @param image
   *   Reference to a Image object
   */
  Image(const Image & image);

  /**
   * @brief Virtual destructor
   */
  virtual ~Image();

//------------------------------------------------------------------------------

  /**
   * @brief Assignment operator
   */
  virtual Image & operator =(const Image & image);

  /**
   * @brief Equal operator
   */
  virtual bool operator ==(const Image & image) const;

//------------------------------------------------------------------------------

  /**
   * @brief Getters
   */
  Header * getHeader() {
    return m_header;
  }

  Eigen::MatrixXd & getData() {
    return m_data;
  }

  long getSizeX();
  long getSizeY();

  /**
   * @brief Setters
   */
  void setHeader(Header * header) {
    m_header = header;
  }

  void setData(const std::valarray<double> & data) {
    size_t sizeX = getSizeX();
    size_t sizeY = getSizeY();
    m_data.resize(sizeX, sizeY);
    for (size_t c = 0; c < sizeY; c++) {
      for (size_t r = 0; r < sizeX; r++) {
        m_data(r,c) = data[r*sizeX + c];
      }
    }
  }
  void setData(const Eigen::MatrixXd & data) {
    m_data.resize(data.rows(), data.cols());
    m_data = data;
  }

  void setSizeX(long sizeX);
  void setSizeY(long sizeY);

//------------------------------------------------------------------------------

  /**
   * @brief print
   * #details
   *   Prints the contents of the header (all keywords)
   *   and the contents of the image.
   */
  void print();

//------------------------------------------------------------------------------

protected:

  Header * m_header { };                   ///< Image header

  Eigen::MatrixXd m_data;                  ///< Image data

};

//-----------------------------------------------------------------------------

} /* namespace Fits */
} /* namespace ChDataModel */

#endif /* IMAGE_H_ */
