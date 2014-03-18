/** 
 * @file FluxMatrix.cpp
 * @date December 16, 2013
 * @author Nikolaos Apostolakos
 */

#include <tuple>
#include "ProtoZ/parameter/PhzParameter.h"
#include "ProtoZ/matrix/serialize.h"
#include "ProtoZ/matrix/MatrixAsciiExporter.h"
#include "ProtoZ/matrix/MatrixFitsExporter.h"
#include "ProtoZ/matrix/FluxMatrix.h"

namespace ProtoZ {
namespace matrix {

template<typename T>
AxisInfo<T> convertPhzParamterToAxisInfo(const param::PhzParameter<T>& parameter) {
  std::vector<T> values {};
  for (uint32_t i=0; i<parameter.size(); ++i)
    values.push_back(parameter.indexToValue(i));
  return AxisInfo<T> {parameter.getName(), values};
}

FluxMatrix::FluxMatrix(const param::FluxModelingParameters& parameters) :
        m_matrix{convertPhzParamterToAxisInfo(parameters.getSeds()),
                 convertPhzParamterToAxisInfo(parameters.getEbvs()),
                 convertPhzParamterToAxisInfo(parameters.getExtLaws()),
                 convertPhzParamterToAxisInfo(parameters.getZs()),
                 convertPhzParamterToAxisInfo(parameters.getFilters())} { }

FluxMatrix::FluxMatrix(const std::string& filename) :
        m_matrix{readMatrixFromFile<double, dm::SedNames, double, std::string,
                                    double, dm::FilterNames>(filename)} { }
                                    
void FluxMatrix::setValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                           uint32_t zIndex, uint32_t filterIndex, double value) {
  uint32_t indices[] = {sedIndex, ebvIndex, extLawIndex, zIndex, filterIndex};
  m_matrix.setValue(indices, value);
}

double FluxMatrix::getValue(uint32_t sedIndex, uint32_t ebvIndex, uint32_t extLawIndex,
                             uint32_t zIndex, uint32_t filterIndex) const {
  uint32_t indices[] = {sedIndex, ebvIndex, extLawIndex, zIndex, filterIndex};
  return m_matrix.getValue(indices);
}

const AxisInfo<dm::SedNames>& FluxMatrix::getSedAxis() const {
  return std::get<0>(m_matrix.axesInfo());
}
  
const AxisInfo<double>& FluxMatrix::getEbvAxis() const {
  return std::get<1>(m_matrix.axesInfo());
}

const AxisInfo<std::string>& FluxMatrix::getExtLawAxis() const {
  return std::get<2>(m_matrix.axesInfo());
}

const AxisInfo<double>& FluxMatrix::getZAxis() const {
  return std::get<3>(m_matrix.axesInfo());
}

const AxisInfo<dm::FilterNames>& FluxMatrix::getFilterAxis() const {
  return std::get<4>(m_matrix.axesInfo());
}

void FluxMatrix::writeInFile(const std::string& filename) const {
  writeMatrixInFile(filename, m_matrix);
}

void FluxMatrix::exportAsAscii(const std::string& filename) const {
  MatrixAsciiExporter::exportMatrixAsAsciiFile(filename, m_matrix, "Flux");
}

void FluxMatrix::exportAsFits(const std::string& filename) const {
  MatrixFitsExporter::exportMatrixAsFitsFile(filename, m_matrix);
}

} /* namespace matrix */
} /* namespace ProtoZ */