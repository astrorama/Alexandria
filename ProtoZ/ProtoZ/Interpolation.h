/**
 * @file BaseInterpolation.h
 * @date Sep 17, 2013
 * @author Nicolas Morisset
 */

#ifndef PROTOZ_INTERPOLATION_H_
#define PROTOZ_INTERPOLATION_H_

#include <string>
#include <vector>
#include <memory>

/**
 * InterpolationMethod are :
 * CUBIC  : For cubic spline interpolation
 * LINEAR : For linear interpolation
 */
enum class InterpolationMethod {
  None,  // None stands for something like NaN (not a number)
  CUBIC, // For cubic spline interpolation
  LINEAR // For linear interpolation
};

/**
 * @class BaseInterpolation
 * @brief Base class used by any interpolation classes
 */

class BaseInterpolation
{

  public:
  /**
   * @brief Constructor
   * Interpolation on a table of x's and y's of length m
   *
   * @param x : array of abscissas Xj where j=0..N-1
   * @param y : array of ordinates Y
   * @param m : size of the table to be interpolated where m <= N
   */
  BaseInterpolation(const std::vector<double>& x, const std::vector<double>& y, int m);

  /**
   * @brief Virtual Destructor
   */
  virtual ~BaseInterpolation() {};

  /**
   * @brief interpolate
   * return an interpolated value corresponding to a value x
   *
   * @details
   *
   * @param
   *  x : value to be interpolated
   *
   * @return
   *  value interpolated for the value x
   *
   * @throw
   *
   */
  double interpolate(const double x);

  const std::vector<double>  xx; // X abscissas
  const std::vector<double>  yy; // Y ordinates

private:

  /**
   * @brief locate
   * Given a value x, return a value j such that x is centered in the subrange
   * xx[j..j+mm-1] where xx is the stored pointer.
   *
   * @details
   * Given an array of abscissas Xj, j=0..,N-1, and given an integer M<=N
   * and a number X, the purpose is to find an integer J_low in order to have
   *  X centered among the M abscissas Xj_low,..,X(j_low+M-1). Center means
   *  that X is in between Xm and Xm+1
   *  where:
   *      m = Jlow + (M-2)/2
   *  and never have :
   *   J_low < 0 and (J_low + M - 1) > N-1
   *
   * @param
   * double value to locate
   *
   * @return
   * Return a value j such that x is centered in the subrange xx[j..j+mm-1]
   * The returned value is not less than 0 nor greater than n-1.
   *
   * @throw
   *
   */

  int locate(const double x);

  /**
   * @brief
   * Given a x value it returns a value J such that x is centered in the subrange
   * xx[j..j+mm-1] where xx is the stored pointer.
   *
   * @param x :  value to be located
   *
   * @throw
   * xx array size error
   *
   * @return
   * index j value, this value is not less than 0 nor greater than n-1
   */

  int hunt(const double x);


  /**
   * @brief
   *   For a value x, using pointers to xx and yy data and the stored vector
   *   of second derivatives y2, this routine returns the cubic spline
   *   interpolated value y. All derived class must define this interpolation
   *   method.
   *
   * @details
   *
   * @param j_lower : index for xx array
   * @param x  : value to be interpolated
   *
   * @throw
   * xx array size error
   *
   * @return
   *
   */

  double virtual rawinterp(int j_lower, double x) = 0;

  int          m_x_size;         /// Size of vector x
  int          m_x_subset_size;  /// Size of the subset of abscissas of x
  int          m_j_saved;        /// Remember the previous j_low
  int          m_hunt_or_locate; /// 0: use hunt function, 1: use locate function
  int          m_delta_j;


};


/**
 * @class CubicSplineInterpolation
 * @brief Apply the Cubic Spline interpolation
 */

class CubicSplineInterpolation : public BaseInterpolation
{

public:

  CubicSplineInterpolation(const std::vector<double> &xv, const std::vector<double> &yv, double yp1=1.e99, double ypn=1.e99)
: BaseInterpolation(xv, yv, 2), y2(xv.size())
  { sety2(xv, yv, yp1, ypn); }


  /**
   * @brief
   * This routine sets an array y2[0..n-1] with second derivatives of the
   * interpolating function
   *
   * @details
   * This routine sets an array y2[0..n-1] with second derivatives of the
   * interpolating function at the tabulated points pointed to by xv using
   * function values pointed to by yv. Yp1 and ypn are the first derivative
   * respectively at the first and last points. Yp1 and ypn set to 1x10^99
   * means the condition for a natural spline, with zero second derivative on
   * that boundary, otherwise they are the values of the first derivatives at
   * the end points.
   *
   * @param xv  : abscissas of points x,y
   * @param yv  : ordinates of points x,y
   * @param yp1 : first derivative of the first point
   * @param ypn : first derivative of last point
   *
   * @throw
   * division by zero
   */

  void sety2(const std::vector<double>& xv, const std::vector<double>& yv, double yp1, double ypn);

  /**
   * @brief
   * For a value x, using pointers to xx and yy data and the stored vector
   * of second derivatives y2, this routine returns the cubic spline
   * interpolated value y.
   *
   * @param j_lower : index for xx vector of the base class
   * @param x       : value to be interpolated
   *
   * @return
   * cubic spline interpolated value of x
   *
   * @throw
   * bad input to routine, h=0!!
   *
   */
  double rawinterp(const int j_low, const double x);


private:

  std::vector<double> y2; /// Second derivatives

};



/**
 * @class CubicSplineInterpolation
 * @brief Apply the Cubic Spline interpolation
 */

class LinearInterpolation : public BaseInterpolation
{

public:
  LinearInterpolation(const std::vector<double>& xv, const std::vector<double>& yv) :
                     BaseInterpolation(xv, yv, 2) {}

  /**
   * @brief rawinterp
   * For a value x, using pointers to xx and yy data and the stored vector
   * of second derivatives y2, this routine returns the cubic spline
   * interpolated value y.
   *
   * @param j : index for xx vector of the base class
   * @param x : value to be interpolated
   *
   * @return
   * cubic spline interpolated value of x
   *
   */
  double rawinterp(const int j, const double x);

private:

};



#endif /* PROTOZ_INTERPOLATION_H_ */
