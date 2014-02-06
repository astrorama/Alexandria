/**
 * @file FilterName.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef FILTERNAME_H_
#define FILTERNAME_H_

#include <string>
#include <functional>

namespace ChDataModel {

/**
 * @class FilterName
 * 
 * @brief Represents the qualified name of a filter
 * 
 * 
 * The FilterName class represents the qualified name of a filter. This name
 * consists of the name of the group the filter belongs and the name of the
 * filter itself. The two names are separated with the '/' character (eg
 * COSMOS/IA464_Subaru). Note that the qualified name of a filter is unique and
 * it can be used for identifying the filter.
 * 
 * The FilterName class provides a method for calculating its hash. The
 * "less than" and "equals" operators are implemented using this hash value as
 * much as possible. This means the FilterName can be used as a key in ordered
 * and unordered collections in an efficient way. Note that for favoring
 * performance, the ordering of the FilterNames is not alphabetical, but based
 * on the hash key. If the alphabetical ordering is important, then the provided
 * FilterName::AlphabeticalComparator can be used:
 * 
 * \code
 * // This set will order the FilterNames based on their hash values
 * std::set<FilterName> hashOrderedSet {};
 * 
 * // This set will order the FilterNames in alphabetical order of their
 * // qualified names
 * std::set<FilterName, FilterName::AlphabeticalComparator> alphabeticalSet {};
 * \endcode
 */
class FilterName {

public:

  /**
   * @brief
   * Constructs a filter with the given group and name
   * @details
   * Both group and name cannot be empty and they cannot contain the '/'
   * character. In this case a std::invalid_argument exception is thrown.
   * 
   * @param group The group of the filter
   * @param name The name of the filter
   * @throws std::invalid_argument
   *    if any of the parameters is empty or contains the '/' character
   */
  FilterName(const std::string& group, const std::string& name);
  
  /**
   * @brief Copy constructor
   * @param The filter name to copy from
   */
  FilterName(const FilterName&) = default;
  
  /**
   * @brief Copy assignment operator
   * @param The filter name to copy from
   * @return A reference to the filter name which was copied to
   */
  FilterName& operator=(const FilterName&) = default;
  
  /**
   * @brief Move constructor
   * @param The filter name to move from
   */
  FilterName(FilterName&&) = default;
  
  /**
   * @brief Move assignment operator
   * @param The filter name to move from
   * @return A reference to the filter name in which was moved in
   */
  FilterName& operator=(FilterName&&) = default;

  /**
   * @brief Destructor
   */
  virtual ~FilterName() = default;

  /**
   * @brief Returns the name of the group in which the filter belongs
   * @return The group name 
   */
  const std::string& group() const;

  /**
   * @brief Returns the name of the filter
   * @return The name of the filter
   */
  const std::string& name() const;

  /**
   * @brief Returns the qualified name of the filter
   * @details
   * The qualified name is the combination of the group name and filter name
   * separated with the '/' character. For example: "COSMOS/IA464_Subaru".
   * @return The qualified name of the filter
   */
  const std::string& qualifiedName() const;
  
  /**
   * @brief Returns the hash value of the filter name
   * @return The hash value
   */
  size_t hash() const;
  
  /**
   * @brief Compares this filter name with the parameter
   * @details
   * The comparison is based on the hash value of the filters (for performance
   * reasons). For alphabetical comparison the FilterName::alphabeticalComparator
   * can be used.
   * @param other The filter name to compare with
   * @return 
   */
  bool operator<(const FilterName& other) const;
  
  /**
   * @brief Checks if this filter name is equal with the parameter
   * @details
   * Two filter names are considered equal if they have the same qualified name
   * (same group and name).
   * @param other The filter name to compare with
   * @return true if the two filter names have the same qualified name, false otherwise
   */
  bool operator==(const FilterName& other) const;
  
  /**
   * @class AlphabeticalComparator
   * @brief Provides alphabetical comparison for the filter names a and b
   * @param a The first FilterName to compare
   * @param b The second FilterName to compare
   * @return true if the a < b alphabetically, false otherwise
   */
  struct AlphabeticalComparator {
    bool operator()(const FilterName& a, const FilterName& b) const {
        return a.qualifiedName() < b.qualifiedName();
    }
  };

private:

  std::string m_group;
  std::string m_name;
  mutable std::string m_qual_name {};
  mutable size_t m_hash {0};

}; // class FilterName

} // namespace ChDataModel 

namespace std {

/**
 * @brief Hash operation for the ChDataModel::FilterName
 * @details
 * This method is implemented so no special hash functions need to be given as
 * template parameters to the unordered collections. It just redirects the call
 * to the FilterNames function.
 * @param filterName The filter name to get the hash key for
 * @return The hash key of the FilterName
 */
template <>
struct hash<ChDataModel::FilterName> {
  size_t operator()(const ChDataModel::FilterName& filterName) const {
    return filterName.hash();
  }
};

} // namespace std

#endif // FILTERNAME_H_ 
