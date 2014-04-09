/** 
 * @file Table.h
 * @date April 9, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef ASCIITABLE_TABLE_H
#define	ASCIITABLE_TABLE_H

#include <memory>
#include <vector>
#include "AsciiTable/ColumnInfo.h"
#include "AsciiTable/Row.h"

namespace AsciiTable {

class Table {
  
public:
  
  typedef std::vector<Row>::const_iterator const_iterator;
  
  Table(std::vector<Row> row_list);
  
  std::shared_ptr<ColumnInfo> getColumnInfo() const;
  
  std::size_t size() const;
  
  const Row& operator[](std::size_t index) const;
  
  const_iterator begin() const;
  
  const_iterator end() const;
  
private:
  std::vector<Row> m_row_list;
  std::shared_ptr<ColumnInfo> m_column_info;
};

}

#endif	/* ASCIITABLE_TABLE_H */

