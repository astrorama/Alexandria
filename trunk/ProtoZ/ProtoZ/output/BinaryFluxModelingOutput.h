/** 
 * @file BinaryFluxModelingOutput.h
 * @date December 23, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef BINARYFLUXMODELINGOUTPUT_H
#define	BINARYFLUXMODELINGOUTPUT_H

#include <string>
#include "ProtoZ/matrix/FluxMatrix.h"
namespace matrix = ProtoZ::matrix;
#include "ProtoZ/output/FluxModelingOutput.h"

namespace ProtoZ {
namespace output {

class BinaryFluxModelingOutput : public FluxModelingOutput {
  
public:
  
  BinaryFluxModelingOutput(const std::string& filename) : m_filename{filename} { }
  
  void outputFluxMatrix(const matrix::FluxMatrix& fluxMatrix) override {
    fluxMatrix.writeInFile(m_filename);
  }
  
private:
  
  std::string m_filename;
  
};

} /* namespace output */
} /* namespace ProtoZ */

#endif	/* BINARYFLUXMODELINGOUTPUT_H */

