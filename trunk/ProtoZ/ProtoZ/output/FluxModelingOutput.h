/** 
 * @file FluxModelingOutput.h
 * @date December 23, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef FLUXMODELINGOUTPUT_H
#define	FLUXMODELINGOUTPUT_H

#include "ProtoZ/matrix/FluxMatrix.h"
namespace matrix = ProtoZ::matrix;

namespace ProtoZ {
namespace output {

class FluxModelingOutput {
  
public:
  
  virtual ~FluxModelingOutput() = default;
  
  virtual void outputFluxMatrix(const matrix::FluxMatrix& fluxMatrix) = 0;
  
}; /* class FluxModelingOutput */

} /* namespace output */
} /* namespace ProtoZ */

#endif	/* FLUXMODELINGOUTPUT_H */

