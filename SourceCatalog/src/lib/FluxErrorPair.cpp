/** 
 * @file FluxErrorPair.cpp
 * @date January 22, 2015
 * @author Nikolaos Apostolakos
 */

#include "SourceCatalog/SourceAttributes/Photometry.h"

namespace Euclid {
namespace SourceCatalog {

FluxErrorPair::FluxErrorPair(double flux, double error, bool no_data) :
      flux(flux), error(error), no_data(no_data) { }

bool FluxErrorPair::operator ==(const FluxErrorPair& other) const {
  return (this->no_data && other.no_data) || (this->flux == other.flux && this->error == other.error);
}

bool FluxErrorPair::operator !=(const FluxErrorPair& other) const {
  return !(*this == other);
}

} // end of namespace SourceCatalog
} // end of namespace Euclid