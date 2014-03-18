/** 
 * @file PdfCatalogFitsOutput.h
 * @date February 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PDFCATALOGFITSOUTPUT_H
#define	PDFCATALOGFITSOUTPUT_H

#include <memory>
#include <string>
#include <vector>
#include <CCfits/CCfits>

class PdfDataFitsOutput {
  
public:
  
  PdfDataFitsOutput(const std::string& filename) : m_filename{filename} {
    remove(m_filename.c_str());
    m_pFits.reset(new CCfits::FITS(m_filename, CCfits::Write));
  }
  
  virtual ~PdfDataFitsOutput() = default;
  
  void flush() {
    m_pFits.reset(nullptr);
    m_pFits.reset(new CCfits::FITS(m_filename, CCfits::Write));
  }
  
  void addPdf(uint64_t objectId, const std::vector<double>& zValues,
              const std::vector<double>& pdfValues) {
    unsigned long rows(pdfValues.size());
    std::string hduName {std::to_string(objectId)};
    std::vector<string> colName {"Z","PDF"};
    std::vector<string> colForm {"D","D"};
    std::vector<string> colUnit {"",""};
    std::unique_ptr<CCfits::Table> pdfTable {m_pFits->addTable(hduName,rows,colName,colForm,colUnit)};
    pdfTable->column("Z").write(zValues,1);
    pdfTable->column("PDF").write(pdfValues,1);
  }
  
private:
  
  std::string m_filename;
  std::unique_ptr<CCfits::FITS> m_pFits {nullptr};
  
};

#endif	/* PDFCATALOGFITSOUTPUT_H */

