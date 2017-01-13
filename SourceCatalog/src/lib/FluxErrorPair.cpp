/** 
 * @file FluxErrorPair.cpp
 * @date January 22, 2015
 * @author Nikolaos Apostolakos
 */

#include "SourceCatalog/SourceAttributes/Photometry.h"

namespace Euclid {
namespace SourceCatalog {

FluxErrorPair::FluxErrorPair(double flux, double error) :
      flux(flux), error(error) { }

bool FluxErrorPair::operator ==(const FluxErrorPair& other) const {
  return this->flux == other.flux && this->error == other.error;
}

bool FluxErrorPair::operator !=(const FluxErrorPair& other) const {
  return !(*this == other);
}

} // end of namespace SourceCatalog
} // end of namespace Euclid