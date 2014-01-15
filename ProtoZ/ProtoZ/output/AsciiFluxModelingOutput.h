/** 
 * @file AsciiFluxModelingOutput.h
 * @date December 23, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef ASCIIFLUXMODELINGOUTPUT_H
#define	ASCIIFLUXMODELINGOUTPUT_H

#include <string>
#include "ProtoZ/matrix/FluxMatrix.h"
namespace matrix = ProtoZ::matrix;
#include "ProtoZ/output/FluxModelingOutput.h"

namespace ProtoZ {
namespace output {

class AsciiFluxModelingOutput : public FluxModelingOutput {
  
public:
  
  AsciiFluxModelingOutput(const std::string& filename) : m_filename{filename} { }
  
  void outputFluxMatrix(const matrix::FluxMatrix& fluxMatrix) override {
    fluxMatrix.exportAsAscii(m_filename);
  }
  
private:
  
  std::string m_filename;
  
};

} /* namespace output */
} /* namespace ProtoZ */

#endif	/* ASCIIFLUXMODELINGOUTPUT_H */

