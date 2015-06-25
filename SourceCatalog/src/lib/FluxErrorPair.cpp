/**
 * @file FluxErrorPair.cpp
 * @date January 22, 2015
 * @author Nikolaos Apostolakos
 */

#include "SourceCatalog/SourceAttributes/Photometry.h"

namespace Euclid {
namespace SourceCatalog {

FluxErrorPair::FluxErrorPair(double flux, double error, bool no_data, bool upper_limit) :
      flux(flux), error(error), missing_photometry_flag(no_data), upper_limit_flag(upper_limit) {}

bool FluxErrorPair::operator ==(const FluxErrorPair& other) const {
  return (this->missing_photometry_flag && other.missing_photometry_flag) ||
      (this->flux == other.flux && this->error == other.error && this->upper_limit_flag == other.upper_limit_flag);
}

bool FluxErrorPair::operator !=(const FluxErrorPair& other) const {
  return !(*this == other);
}

} // end of namespace SourceCatalog
} // end of namespace Euclid
