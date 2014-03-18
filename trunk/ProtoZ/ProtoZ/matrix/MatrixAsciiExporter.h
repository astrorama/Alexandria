/** 
 * @file MatrixAsciiExporter.h
 * @date December 13, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef MATRIXASCIIEXPORTER_H
#define	MATRIXASCIIEXPORTER_H

#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <tuple>
#include "ProtoZ/matrix/Matrix.h"

namespace ProtoZ {
namespace matrix {

/**
 * @class MatrixAsciiExporter
 * @brief
 *      Utility class for exporting a matrix as ASCII table
 */
class MatrixAsciiExporter {
  
public:
  
  /**
   * @brief
   *    Exports the given matrix in a file as ASCII table
   * @details
   *    The first line of the file is a comment line with the names of the columns.
   *    All the columns except the last one represent the axes of the matrix. The
   *    last column contains the values of the matrix.
   * 
   * @param filename
   *    A string representation of the file to export the matrix in
   * @param matrix
   *    The matrix to export
   */
  template<typename T, typename... Axes>
  static void exportMatrixAsAsciiFile(const std::string& filename,
                                      const Matrix<T,Axes...>& matrix);
  
  /**
   * @brief
   *    Exports the given matrix in a file as ASCII table
   * @details
   *    The first line of the file is a comment line with the names of the columns.
   *    All the columns except the last one represent the axes of the matrix. The
   *    last column contains the values of the matrix and is titled with the
   *    given name.
   * 
   * @param filename
   *    A string representation of the file to export the matrix in
   * @param matrix
   *    The matrix to export
   * @param matrixName
   *    The title of the matrix values column
   */
  template<typename T, typename... Axes>
  static void exportMatrixAsAsciiFile(const std::string& filename,
                                      const Matrix<T,Axes...>& matrix,
                                      const std::string& matrixName);
  
private:
  
  // This class is used as a counter for template loops
  template<int>
  struct TemplateLoopCounter { };

  // A helper class which creates the lines of the table using template looping
  template<typename T, typename... Axes>
  class DataTextCreator;
  
  // A helper class which creates the header of the table using template looping
  template<typename... Axes>
  class AxesLabelCreator;
  
};

} /* namespace matrix */
} /* namespace ProtoZ */

#define MATRIXASCIIEXPORTER_IMPL
#include "ProtoZ/matrix/_impl/MatrixAsciiExporter.icpp"
#undef MATRIXASCIIEXPORTER_IMPL

#endif	/* MATRIXASCIIEXPORTER_H */

