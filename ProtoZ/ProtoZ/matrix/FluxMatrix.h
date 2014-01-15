/** 
 * @file FluxMatrix.h
 * @date December 16, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef FLUXMATRIX_H
#define	FLUXMATRIX_H

#include <string>
#include "ChDataModel/Enumerations/SedNames.h"
#include "ChDataModel/Enumerations/FilterNames.h"
namespace dm = ChDataModel;
#include "ProtoZ/parameter/FluxModelingParameters.h"
namespace param = ProtoZ::parameter;
#include "ProtoZ/matrix/Matrix.h"
#include "ProtoZ/matrix/AxisInfo.h"

namespace ProtoZ {
namespace matrix {

/**
 * @class FluxMatrix
 * @brief
 *      Represents a matrix which keeps the calculated fluxes
 * @details
 *      This matrix is an adapter around a ProtoZ::matrix::Matrix object for
 *      facilitating its usage based on the fact that the FluxMatrix has known
 *      axes.
 */
class FluxMatrix {
  
public:
  
  /**
   * @brief
   *    Constructs a new FluxMatrix based on the given parameters
   * @details
   *    The axes of the matrix are constructed based on the given PhzParameters.
   *    The total memory of the matrix is reserved for the returned Matrix.
   * 
   * @param parameters
   *    The FluxModelingParameters object to get the information of the axes
   */
  FluxMatrix(const param::FluxModelingParameters& parameters);
  
  /**
   * @brief
   *    Constructs a new FluxMatrix based on a binary file
   * @details
   *    The binary file must be a binary representation of the FluxMatrix. These
   *    files can be created with the FluxMatrix::writeInFile(filename) method.
   * 
   * @param filename
   *    The name of the file
   */
  FluxMatrix(const std::string& filename);
  
  // Because the flux matrix will be very big, we forbid copying and allow
  // moving. The default moving is enough because Matrix implements it also.
  FluxMatrix(const FluxMatrix&) = delete;
  FluxMatrix& operator=(const FluxMatrix&) = delete;
  
  FluxMatrix(FluxMatrix&&) = default;
  FluxMatrix& operator=(FluxMatrix&&) = default;
  
  /**
   * @brief Destructor
   */
  virtual ~FluxMatrix() = default;
  
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
   * @param filterIndex
   *    The index of the filter axis
   * @param value
   *    The new value of the cell
   * @throws std::out_of_range
   *    If any of the indices is out of range
   */
  void setValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                uint32_t zIndex, uint32_t filterIndex, double value);
  
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
   * @param filterIndex
   *    The index of the filter axis
   * @return 
   *    The matrix cell value
   * @throws std::out_of_range
   *    If any of the indices is out of range
   */
  double getValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                  uint32_t zIndex, uint32_t filterIndex) const;
  
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
   *    Returns information about the filter axis.
   * 
   * @return 
   *    Information about the filter axis
   */
  const AxisInfo<dm::FilterNames>& getFilterAxis() const;
  
  /**
   * @brief
   *    Writes the FluxMatrix in a binary file
   * @details
   *    The binary file follows the boost::serialization conventions and can be
   *    used to create a new instance of FluxMatrix (by using the constructor).
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
  
private:
  
  /// The matrix where the flux values are really stored
  Matrix<double, dm::SedNames, double, std::string, double, dm::FilterNames> m_matrix;
  
};

} /* namespace matrix */
} /* namespace ProtoZ */

#endif	/* FLUXMATRIX_H */

