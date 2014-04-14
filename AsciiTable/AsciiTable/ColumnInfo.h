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
#include <typeindex>
#include <utility>

namespace AsciiTable {

/**
 * @class ColumnInfo
 * 
 * @brief Provides information about the columns of a Table
 * 
 * @details
 * The ColumnInfo is an immutable class which provides information about the
 * columns of a Table. Each column has a name and a type. This class can be
 * used for retrieving the name and the type of a column using its index (zero
 * based) and for searching a column with a specific name.
 * 
 * The names of the columns must by unique, they cannot be the empty string and
 * they cannot contain any whitespace characters. 
 * 
 * The ColumnInfo implements the comparisson operators "==" and "!=" in a way
 * that if they describe the same number of columns with the same names and types
 * they are equal.
 */
class ColumnInfo {

public:
  
  typedef std::pair<std::string, std::type_index> info_type;
  
  /**
   * @brief
   * Constructs a ColumnInfo representing the given column names and types
   * @details
   * The order of the columns is assumed to be the same with their order in the
   * passed vector. Because the ColumnInfo is immutable the info_list cannot
   * be empty.
   * 
   * Note that the info_list is passed by value to allow the caller to optimize
   * for performance, meaning that the constructor will take advantage of move
   * semantics if the passed object is an rvalue.
   * 
   * @param info_list A vector containing the names and types of the columns
   * @throws ElementsException
   *    if the info_list is empty
   * @throws ElementsException
   *    if the info_list contains duplicate name entries
   * @throws ElementsException
   *    if any of the given column names is the empty string
   * @throws ElementsException
   *    if any of the given column names contains whitespace characters
   */
  ColumnInfo(std::vector<info_type> info_list);
  
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
   * Returns the name of the column with the given index or throws an exception if the
   * index is bigger than the size of the ColumnInfo
   * 
   * @param index The index to search for
   * @return The name of the column
   * @throws ElementsException
   *    if the index is out of bounds
   */
  const std::string& getName(std::size_t index) const;
  
  /**
   * @brief
   * Returns the type of the column with the given index or throws an exception
   * if the index is bigger than the size of the ColumnInfo
   * 
   * @param index The index to search for
   * @return The type of the column cells
   * @throws ElementsException
   *    if the index is out of bounds
   */
  const std::type_index& getType(std::size_t index) const;
  
  /**
   * @brief
   * Returns the index of a column, given the name of it, or nullptr if there is
   * no column with this name
   * 
   * @param name The name to search for
   * @return The index of the column or nullptr if there is no such column
   */
  std::unique_ptr<std::size_t> find(const std::string& name) const;
  
private:
  std::vector<info_type> m_info_list;
  
};

}

#endif	/* ASCIITABLE_COLUMNINFO_H */

