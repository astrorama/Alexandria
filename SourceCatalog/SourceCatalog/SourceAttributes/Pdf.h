/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
 *  
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free 
 * Software Foundation; either version 3.0 of the License, or (at your option)  
 * any later version.  
 *  
 * This library is distributed in the hope that it will be useful, but WITHOUT 
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  
 * details.  
 *  
 * You should have received a copy of the GNU Lesser General Public License 
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA  
 */
 
 /*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
 *  
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free 
 * Software Foundation; either version 3.0 of the License, or (at your option)  
 * any later version.  
 *  
 * This library is distributed in the hope that it will be useful, but WITHOUT 
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  
 * details.  
 *  
 * You should have received a copy of the GNU Lesser General Public License 
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA  
 */

/* 
 * @file Pdf.h
 * @author nikoapos
 */

#ifndef SOURCE_CATALOG_PDF_H
#define SOURCE_CATALOG_PDF_H

#include <map>
#include <string>
#include <vector>
#include "GridContainer/GridContainer.h"
#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

template <typename T>
class Pdf : public Attribute {
  
public:
  
  using PdfType = GridContainer::GridContainer<std::vector<double>, T>;
  
  Pdf(std::map<std::string, PdfType> pdfs) : m_pdfs(std::move(pdfs)) { }
  
  virtual ~Pdf() = default;
  
  const PdfType& getPdf(const std::string& name) {
    return m_pdfs.at(name);
  }
  
private:
  
  std::map<std::string, PdfType> m_pdfs;
  
};

}
}

#endif /* SOURCE_CATALOG_PDF_H */

