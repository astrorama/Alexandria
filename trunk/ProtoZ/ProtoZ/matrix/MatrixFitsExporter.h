/** 
 * @file MatrixFitsExporter.h
 * @date February 1, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATRIXFITSEXPORTER_H
#define	MATRIXFITSEXPORTER_H

#include <string>
#include "ProtoZ/matrix/Matrix.h"

namespace ProtoZ {
namespace matrix {

/**
 * @class MatrixAsciiExporter
 * @brief
 *      Utility class for exporting a matrix in FITS format
 */
class MatrixFitsExporter {
  
public:
  
  /**
   * @brief
   *    Exports the given matrix in a file in FITS format
   * @details
   *    The first HDU is a n-dimensional array which contains the matrix data.
   *    The rest of the HDUs contain the values of the different axes.
   * 
   * @param filename
   *    A string representation of the file to export the matrix in
   * @param matrix
   *    The matrix to export
   */
  template<typename T, typename... Axes>
  static void exportMatrixAsFitsFile(const std::string& filename,
                               const Matrix<T,Axes...>& matrix);
  
private:
  
  // This class is used as a counter for template loops
  template<int>
  struct TemplateLoopCounter { };
  
  // A helper class for handling the axes using template loops
  template<typename... Axes>
  class AxesHelper;
  
};

} /* namespace matrix */
} /* namespace ProtoZ */

#define MATRIXFITSEXPORTER_IMPL
#include "ProtoZ/matrix/_impl/MatrixFitsExporter.icpp"
#undef MATRIXFITSEXPORTER_IMPL

#endif	/* MATRIXFITSEXPORTER_H */

