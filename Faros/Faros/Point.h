/*
 * @file Point.h
 *
 *  Created on: Jun 28, 2013
 *      Author: Nicolas Morisset
 */

#ifndef POINT_H_
#define POINT_H_

#include <iostream>
#include <iomanip>

/**
 * @class Point
 * @brief
 *   Point is a generic class defining a point which consists of an abscissa X
 *   and an ordinate Y
 */

class Point {

public:

  /**
   * @brief Default Constructor
   * Member m_tolerence is the tolerence for any double comparison
   */
  Point(): m_x(0.0), m_y(0.0), m_tolerence(0.001) {}

  /**
   * @brief Constructor with member assignment
   * A point is defined an abscissa X and an ordinate Y
   * Member m_tolerence is the tolerence used for any double comparison
   * @detail
   */
  Point(const double& x, const double& y) : m_x(x), m_y(y), m_tolerence(0.001) {}

  /**
   * @brief Default destructor
   */
  virtual ~Point() {
  }

  /**
   * @brief getX
   * @return
   *   The value on the X axis
   */
  double getX() const { return m_x;}

  /**
   * @brief getY
   * @return
   *   The value on the Y axis
   */
  double getY() const { return m_y;}

  /**
   * @brief setX
   * @return
   *   Set the value on the X axis
   */
  void setX(const double x) { m_x = x; }

  /**
   * @brief setY
   * @return
   *   Set the value on the Y axis
   */
  void setY(const double y) { m_y = y; }

  /**
   * @brief setXY
   */
  void setXY(const double x, const double y) { m_x = x; m_y = y; }

  /**
   * @brief define operator <
   * @return
   *   True or false
   */
  inline bool operator < (const Point &p) const
  {
      return ( (p.m_x < m_x) );
  }

  /**
   * @brief define operator ==
   * @return
   *   True or false
   */
  inline bool operator == (const Point &p) const
  {
    return ( ( abs(m_x - p.m_x) <= m_tolerence ) && ( abs(m_y - p.m_y) <= m_tolerence) ? true : false);
  }

  /**
   * @brief define operator !=
   * @return
   *   True or false
   */
  inline bool operator != (const Point &p) const
  {
    return ( ( abs(m_x - p.m_x) > m_tolerence ) || ( abs(m_y - p.m_y) > m_tolerence) ? true : false);
  }

  /**
   * @brief Print point coordinates
   */
  void print() { std::cout <<  " Abscissa : "
                           << std::fixed
                           << std::setprecision(10)
                           << m_x
                           << std::setw(20)
                           << std::fixed
                           << " Ordinate : "
                           << std::fixed
                           << std::setprecision(10)
                           << m_y
                           << std::endl; }

private:

  /**
   * X axis
   */
  double m_x{};

  /**
   * Y axis
   */
  double m_y{};

  /**
   * tolerence for double
   */
  double m_tolerence{};


}; // Eof class Point

#endif // POINT_H_

