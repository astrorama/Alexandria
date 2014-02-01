/** 
 * @file PdfMatrix.h
 * @date December 16, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef PDFMATRIX_H
#define	PDFMATRIX_H

#include <string>
#include "ChDataModel/Enumerations/SedNames.h"
#include "ChDataModel/Enumerations/FilterNames.h"
namespace dm = ChDataModel;
#include "ProtoZ/matrix/Matrix.h"
#include "ProtoZ/matrix/AxisInfo.h"
#include "ProtoZ/matrix/FluxMatrix.h"

namespace ProtoZ {
namespace matrix {

/**
 * @class PdfMatrix
 * @brief
 *      Represents a matrix which keeps the calculated PDFs
 * @details
 *      This matrix is an adapter around a ProtoZ::matrix::Matrix object for
 *      facilitating its usage based on the fact that the PdfMatrix has known
 *      axes.
 */
class PdfMatrix {
  
public:
  
  /**
   * @brief
   *    Constructs a new PdfMatrix based on the given FluxMatrix
   * @details
   *    The axes of the matrix are constructed based on the given FluxMatrix in
   *    such way so the PdfMatrix can be used to keep the results of the processing
   *    of the given matrix. This constructor does not do any processing of the
   *    given matrix. All the PdfMatrix values are set to 0.
   * 
   * @param fluxMatrix
   *    The FluxMatrix for which results will be stored in the constructed PdfMatrix
   */
  PdfMatrix(const FluxMatrix& fluxMatrix);
  
  /**
   * @brief
   *    Constructs a new PdfMatrix based on a binary file
   * @details
   *    The binary file must be a binary representation of the PdfMatrix. These
   *    files can be created with the PdfMatrix::writeInFile(filename) method.
   * 
   * @param filename
   *    The name of the file
   */
  PdfMatrix(const std::string& filename);
  
  // Because the PDF matrix will be very big, we forbid copying and allow
  // moving. The default moving is enough because Matrix implements it also.
  PdfMatrix(const PdfMatrix&) = delete;
  PdfMatrix& operator=(const PdfMatrix&) = delete;
  
  PdfMatrix(PdfMatrix&&) = default;
  PdfMatrix& operator=(PdfMatrix&&) = default;
  
  /**
   * @brief Destructor
   */
  virtual ~PdfMatrix() = default;
  
  /**
   * @brief
   *    Sets the value of a matrix cell
   * 
   * @param sedIndex
   *    The index of the SED axis
   * @param ebvIndex
   *    The index of the E(B-V) axis
   * @param extLawIndex
   *    The index of the extinction law axis
   * @param zIndex
   *    The index of the redshift axis
   * @param value
   *    The new value of the cell
   * @throws std::out_of_range
   *    If any of the indices is out of range
   */
  void setValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                uint32_t zIndex, double value);
  
  /**
   * @brief
   *    Returns the value of a matrix cell
   * 
   * @param sedIndex
   *    The index of the SED axis
   * @param ebvIndex
   *    The index of the E(B-V) axis
   * @param extLawIndex
   *    The index of the extinction law axis
   * @param zIndex
   *    The index of the redshift axis
   * @return 
   *    The matrix cell value
   * @throws std::out_of_range
   *    If any of the indices is out of range
   */
  double getValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                  uint32_t zIndex) const;
  
  /**
   * @brief
   *    Returns information about the SED axis.
   * 
   * @return 
   *    Information about the SED axis
   */
  const AxisInfo<dm::SedNames>& getSedAxis() const;
   
  /**
   * @brief
   *    Returns information about the E(B-V) axis.
   * 
   * @return 
   *    Information about the E(B-V) axis
   */
  const AxisInfo<double>& getEbvAxis() const;
   
  /**
   * @brief
   *    Returns information about the extinction law axis.
   * 
   * @return 
   *    Information about the extinction law axis
   */
  const AxisInfo<std::string>& getExtLawAxis() const;
   
  /**
   * @brief
   *    Returns information about the redshift axis.
   * 
   * @return 
   *    Information about the redshift axis
   */
  const AxisInfo<double>& getZAxis() const;
  
  /**
   * @brief
   *    Writes the PdfMatrix in a binary file
   * @details
   *    The binary file follows the boost::serialization conventions and can be
   *    used to create a new instance of PdfMatrix (by using the constructor).
   * 
   * @param filename
   *    The name of the file to write the matrix in
   */
  void writeInFile(const std::string& filename) const;
  
  /**
   * @brief
   *    Exports the matrix in a text ASCII file.
   * 
   * @param filename
   *    The name of the file
   */
  void exportAsAscii(const std::string& filename) const;
  
  /**
   * @brief
   *    Exports the matrix in a FITS file.
   * 
   * @param filename
   *    The name of the file
   */
  void exportAsFits(const std::string& filename) const;
  
private:
  
  /// The matrix where the PDF values are really stored
  Matrix<double, dm::SedNames, double, std::string, double> m_matrix;
  
}; /* PdfMatrix */

} /* namespace matrix */
} /* namespace ProtoZ */

#endif	/* PDFMATRIX_H */

