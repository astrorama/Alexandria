/** 
 * @file CombinedFluxModelingOutput.h
 * @date December 23, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef COMBINEDFLUXMODELINGOUTPUT_H
#define	COMBINEDFLUXMODELINGOUTPUT_H

#include <vector>
#include <memory>
#include "ProtoZ/matrix/FluxMatrix.h"
namespace matrix = ProtoZ::matrix;
#include "ProtoZ/output/FluxModelingOutput.h"

namespace ProtoZ {
namespace output {

class CombinedFluxModelingOutput : public FluxModelingOutput {
  
public:
  
  CombinedFluxModelingOutput(const std::vector<std::shared_ptr<FluxModelingOutput>>& handlers)
            : m_handlers{handlers} { }
  
  void outputFluxMatrix(const matrix::FluxMatrix& fluxMatrix) override {
    for (std::shared_ptr<FluxModelingOutput> handler : m_handlers) {
      handler->outputFluxMatrix(fluxMatrix);
    }
  }
  
private:
  
  std::vector<std::shared_ptr<FluxModelingOutput>> m_handlers;
  
};

} /* namespace output */
} /* namespace ProtoZ */

#endif	/* COMBINEDFLUXMODELINGOUTPUT_H */

