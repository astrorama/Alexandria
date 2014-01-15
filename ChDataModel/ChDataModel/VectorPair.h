/**
 * @file VectorPair.h
 *
 * Created on: May 10, 2013
 *     Author: Pavel Binko
 */

#ifndef VECTORPAIR_H_
#define VECTORPAIR_H_

#include <vector>
#include <stddef.h>

namespace ChDataModel {

/**
 * Class VectorPair is a generic class containing two STL vectors
 */
class VectorPair {

public:

  /**
   * @brief Constructor
   */
  VectorPair() = default;

  /**
   * @brief Constructor with member assignment
   * @detail
   *   The two vectors provided x and y must be related together and,
   *   in particular must have the same length. In the case of different axes
   *   lengths, ElementsException will be thrown.
   * @param
   *   If true, orderliness and uniqueness will be checked.
   *   In the case defective input data, ElementsException will be thrown.
   *   If false (the default value), no additional checks will be performed.
   */
  VectorPair(const std::vector<double> & x, const std::vector<double> & y,
      bool check_sort_unique = false);

  /**
   * @brief Default destructor
   */
  virtual ~VectorPair() {
  }

  //---------------------------------------------------------------------------

  /**
   * @brief getX
   * @param i
   *   Index on the X axis
   * @return
   *   The i-th value on the X axis
   */
  double getX(const int i) const;

  /**
   * @brief getAxisX
   * @return
   *   The whole X axis
   */
  const std::vector<double> getAxisX() const {
    return m_x;
  }

  /**
   * @brief getY
   * @param i
   *   Index on the Y axis
   * @return
   *   The i-th value on the Y axis
   */
  double getY(const int i) const;

  /**
   * @brief getAxisY
   * @return
   *   The whole Y axis
   */
  const std::vector<double> getAxisY() const {
    return m_y;
  }

  //---------------------------------------------------------------------------

  /**
   * @brief getFilterName
   * @return
   *   The filter name (as class enum FilterNames)
   */
  size_t size() const {
    return m_x.size();
  }

  //---------------------------------------------------------------------------

  /**
   * @brief printVectorPair
   *   The print method prints the contents of both contained vectors
   */
  void printVectorPair();

  //---------------------------------------------------------------------------

  void setX(const std::vector<double> & x) {
    m_x = x;
  }

  void setY(const std::vector<double> & y) {
    m_y = y;
  }

  //---------------------------------------------------------------------------

protected:

  std::vector<double> m_x;     /**< X axis */
  std::vector<double> m_y;     /**< Y axis */

}; // Eof class VectorPair

} /* namespace ChDataModel */

#endif /* VECTORPAIR_H_ */
