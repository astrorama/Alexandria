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

/**
 * @class ColumnInfo
 * 
 * @brief Provides information about the columns of a Table
 * 
 * @details
 * The ColumnInfo is an immutable class which provides information about
 * the columns of a Table. Each column has a name and this class can be
 * used for converting the name of a column to its index (zero based) and vice
 * versa.
 * 
 * The names of the columns must by unique, they cannot be the empty string and
 * they cannot contain any whitespace characters. 
 * 
 * The ColumnInfo implements the comparisson operators "==" and "!=" in a way
 * that if they describe the same number of columns with the same names they
 * are equal.
 */
class ColumnInfo {

public:
  
  /**
   * @brief
   * Constructs a ColumnInfo representing the given column names
   * @details
   * The order of the columns is assumed to be the same with their order in the
   * passed parameter. Because the ColumnInfo is immutable the name_list cannot
   * be empty.
   * 
   * Note that the name_list is passed by value to allow the caller to optimize
   * for performance, meaning that the constructor will take advantage of move
   * semantics if the passed object is an rvalue.
   * 
   * @param name_list A vector containing the names of the columns
   * @throws Elements::ElementsException
   *    if the name_list is empty
   * @throws Elements::ElementsException
   *    if the name_list contains duplicate entries
   * @throws Elements::ElementsException
   *    if the name_list contains the empty string
   * @throws Elements::ElementsException
   *    if any of the given names contains whitespace characters
   */
  ColumnInfo(std::vector<std::string> name_list);
  
  /**
   * @brief
   * Returns true if this ColumnInfo represents the same columns with the given one
   * 
   * @param other the ColumnInfo to compare with
   * @return true if the two ColumnInfos represent the same columns, false otherwise
   */
  bool operator==(const ColumnInfo& other) const;
  
  /**
   * @brief
   * Returns false if this ColumnInfo represents the same columns with the given one
   * 
   * @param other the ColumnInfo to compare with
   * @return false if the two ColumnInfos represent the same columns, true otherwise
   */
  bool operator!=(const ColumnInfo& other) const;
  
  /**
   * @brief
   * Returns the number of columns represented by this ColumnInfo
   * 
   * @return the number of columns
   */
  std::size_t size() const;
  
  /**
   * @brief
   * Returns the name of the column with the given index or nullptr if the
   * index is bigger than the size of the ColumnInfo
   * 
   * @param index The index to search for
   * @return The name of the column or nullptr if there is no such column
   */
  std::unique_ptr<std::string> getName(std::size_t index) const;
  
  /**
   * @brief
   * Returns the index of a column, given the name of it, or nullptr if there is
   * no column with this name
   * 
   * @param name The name to search for
   * @return The index of the column or nullptr if there is no such column
   */
  std::unique_ptr<std::size_t> getIndex(const std::string& name) const;
  
private:
  std::vector<std::string> m_name_list;
  
};

}

#endif	/* ASCIITABLE_COLUMNINFO_H */

