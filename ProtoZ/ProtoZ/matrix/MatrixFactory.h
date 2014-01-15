/** 
 * @file MatrixFactory.h
 * @date December 4, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef MATRIXFACTORY_H
#define	MATRIXFACTORY_H

#include <string>
#include <memory>
#include "ProtoZ/matrix/Matrix.h"
#include "ProtoZ/matrix/AxisInfo.h"
namespace param = ProtoZ::parameter;


namespace ProtoZ {
namespace matrix {

class MatrixFactory {

public:

  template<typename T, typename... Axes>
  static Matrix<T, Axes...> makeMatrix(AxisInfo<Axes>... axes) {
    return Matrix<T, Axes...>{new Matrix<T, Axes...>{axes...}};
  }

private:

  MatrixFactory() { }

};

} /* namespace matrix */
} /* namespace ProtoZ */

#endif	/* MATRIXFACTORY_H */

