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
  Elements::Exception(message),m_flux(flux),m_error(error){}


  virtual ~LuminosityParsingException() noexcept { }

  const char * what() const noexcept override {
      std::string parent_message=std::string(Elements::Exception::what());
      std::string message = parent_message + "( Flux="+std::to_string(m_flux)+", Error="+std::to_string(m_error)+")";
      return message.c_str();
    }

private:

  double m_flux;
  double m_error;


};

} // namespace ChDataModel 
} // end of namespace Euclid

#endif // LUMINOSITYPARSINGEXCEPTION_H_
