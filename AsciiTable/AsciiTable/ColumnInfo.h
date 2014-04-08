/** 
 * @file ColumnInfo.h
 * @date April 7, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef ASCIITABLE_COLUMNINFO_H
#define	ASCIITABLE_COLUMNINFO_H

#include <string>
#include <vector>
#include <memory>

namespace AsciiTable {

class ColumnInfo {

public:
  
  ColumnInfo(std::vector<std::string> name_list);
  
  std::size_t size() const;
  
  std::unique_ptr<std::string> getName(std::size_t index) const;
  
  std::unique_ptr<std::size_t> getIndex(const std::string& name) const;
  
private:
  std::vector<std::string> m_name_list;
  
};

}

#endif	/* ASCIITABLE_COLUMNINFO_H */

