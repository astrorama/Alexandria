/**
 * @file SourceCatalog/PhotometryParsingException.h
 *
 * Created on: Jan 20, 2017
 *     Author: Florian Dubath
 */
#ifndef PHOTOMETRYPARSINGEXCEPTION_H_
#define PHOTOMETRYPARSINGEXCEPTION_H_

#include <string>
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace SourceCatalog {


class PhotometryParsingException: public Elements::Exception {
public:

  explicit  PhotometryParsingException(const char* message, double flux, double error):
  Elements::Exception(message),m_flux(flux),m_error(error){
    *this << " ( Flux=" << flux << ", Error=" << error << ")";
  }

  virtual ~PhotometryParsingException() noexcept { }

  const double & GetFlux() const {return m_flux;}
  const double & GetError() const {return m_error;}

private:

  double m_flux;
  double m_error;


};

} // namespace ChDataModel
} // end of namespace Euclid

#endif // PHOTOMETRYPARSINGEXCEPTION_H_
