/**
 * @file SourceCatalog/LuminosityParsingException.h
 *
 * Created on: Jan 20, 2017
 *     Author: Florian Dubath
 */
#ifndef LUMINOSITYPARSINGEXCEPTION_H_
#define LUMINOSITYPARSINGEXCEPTION_H_

#include <string>
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace SourceCatalog {


class LuminosityParsingException: public Elements::Exception {
public:

  explicit  LuminosityParsingException(const char* message, double flux, double error):
  Elements::Exception(CompleteMessage(message,flux,error)),m_flux(flux),m_error(error){}

  virtual ~LuminosityParsingException() noexcept { }

  const double & GetFlux() const {return m_flux;}
  const double & GetError() const {return m_error;}

private:

  const char* CompleteMessage(const char* message, double flux, double error){
    std::string str_message(message);
    str_message += " ( Flux="+std::to_string(flux)+", Error="+std::to_string(error)+")";
    return str_message.c_str();
  }

  double m_flux;
  double m_error;


};

} // namespace ChDataModel 
} // end of namespace Euclid

#endif // LUMINOSITYPARSINGEXCEPTION_H_
