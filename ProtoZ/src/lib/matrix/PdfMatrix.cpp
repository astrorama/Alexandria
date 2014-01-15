/** 
 * @file PdfMatrix.cpp
 * @date December 16, 2013
 * @author Nikolaos Apostolakos
 */

#include <tuple>
#include "ProtoZ/matrix/serialize.h"
#include "ProtoZ/matrix/MatrixAsciiExporter.h"
#include "ProtoZ/matrix/PdfMatrix.h"

namespace ProtoZ {
namespace matrix {

PdfMatrix::PdfMatrix(const FluxMatrix& fluxMatrix) :
        m_matrix {fluxMatrix.getSedAxis(), fluxMatrix.getEbvAxis(),
                  fluxMatrix.getExtLawAxis(), fluxMatrix.getZAxis()} { }

PdfMatrix::PdfMatrix(const std::string& filename) :
        m_matrix{readMatrixFromFile<double, dm::SedNames, double, std::string,
                                    double>(filename)} { }
                                    
void PdfMatrix::setValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                           uint32_t zIndex, double value) {
  uint32_t indices[] = {sedIndex, ebvIndex, extLawIndex, zIndex};
  m_matrix.setValue(indices, value);
}

double PdfMatrix::getValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                             uint32_t zIndex) const {
  uint32_t indices[] = {sedIndex, ebvIndex, extLawIndex, zIndex};
  return m_matrix.getValue(indices);
}

const AxisInfo<dm::SedNames>& PdfMatrix::getSedAxis() const {
  return std::get<0>(m_matrix.axesInfo());
}
  
const AxisInfo<double>& PdfMatrix::getEbvAxis() const {
  return std::get<1>(m_matrix.axesInfo());
}

const AxisInfo<std::string>& PdfMatrix::getExtLawAxis() const {
  return std::get<2>(m_matrix.axesInfo());
}

const AxisInfo<double>& PdfMatrix::getZAxis() const {
  return std::get<3>(m_matrix.axesInfo());
}

void PdfMatrix::writeInFile(const std::string& filename) const {
  writeMatrixInFile(filename, m_matrix);
}

void PdfMatrix::exportAsAscii(const std::string& filename) const {
  MatrixAsciiExporter::exportMatrixAsAsciiFile(filename, m_matrix, "chi^2");
}


} /* namespace matrix */
} /* namespace ProtoZ */
