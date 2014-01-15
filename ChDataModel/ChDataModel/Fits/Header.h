/**
 * @file Header.h
 *
 * Created on: Sep 18, 2013
 *     Author: Pavel Binko
 */

#ifndef HEADER_H_
#define HEADER_H_

#include <map>
#include <iostream>

#include "ChDataModel/Fits/Keyword.h"

namespace ChDataModel {
namespace Fits {

//------------------------------------------------------------------------------

/**
 * @class Header
 * @brief
 *   The KeywordBase class contains the name, type and comment of a keyword.
 * @details
 *   Its value is contained in the templated class Keyword.
 */
class Header {

public:

  /**
   * @brief Constructor
   */
  Header() {
  }

  /**
   * @brief Copy constructor
   * @param header
   *   Reference to a header object
   */
  Header(const Header & header);

  /**
   * @brief Virtual destructor
   */
  virtual ~Header();

//------------------------------------------------------------------------------

  /**
   * @brief Equal operator
   * @ detail
   *   Deletes all existing keywords and copies all keywords.
   */
  virtual Header & operator =(const Header & header);

  /**
   * @brief Assignment operator
   * @detail
   *   Returns true if the number of keywords is identical and if all
   *   keywords are identical. The order of the keywords may be different.
   */
  virtual bool operator ==(const Header & header) const;

//------------------------------------------------------------------------------

  /**
   * @brief Getters
   */
  virtual const std::map<std::string, KeywordBase*> & getKeywords() const {
    return m_keywords;
  }

  /**
   * @brief Setters
   */
  virtual void setKeywords(const std::map<std::string, KeywordBase*> & keywords) {
    m_keywords = keywords;
  }

//------------------------------------------------------------------------------

  /**
   * @brief addKeyword
   * @detail
   *   Adds a copy of one keyword to this header (not the keyword itself).
   *   If a keyword with such name exists already, it will be overwritten.
   * @param keyword
   *   Reference to the keyword object
   */
  virtual void addKeyword(const KeywordBase & keyword);

  /**
   * @brief addKeyword
   * @detail
   *   Adds a keyword to this header based on its name, value and comment.
   *   If a keyword with such name exists already, it will be overwritten.
   *   The type of the keyword will be recognized automatically.
   * @param name
   *   Keyword name
   * @param value
   *   Keyword value - can be of the type bool, long, double, std::string
   * @param comment
   *   Keyword comment
   */
  virtual void addKeyword(const std::string & name, bool value,
      const std::string & comment = "");
  virtual void addKeyword(const std::string & name, double value,
      const std::string & comment = "");
  virtual void addKeyword(const std::string & name, long value,
      const std::string & comment = "");
  virtual void addKeyword(const std::string & name, const std::string & value,
      const std::string & comment = "");

  /**
   * @brief existKeyword
   * @param keywordName
   *   Name of the keyword
   * @return
   *   Returns true if the keyword exists in this header.
   */
  bool existKeyword(const std::string & keywordName) const;

  /**
   * @brief getKeyword
   * @param keywordName
   *   Name of the keyword
   */
  virtual KeywordBase & getKeyword(const std::string & keywordName) const;

  /**
   * @brief deleteKeyword
   * @param keywordName
   *   The name of a keyword to be deleted
   */
  virtual void deleteKeyword(const std::string & keywordName);

  /**
   * @brief getNofKeywords
   * @return
   *   Returns the number of keywords in this header.
   */
  virtual size_t getNofKeywords() const {
    return m_keywords.size();
  }

  /**
   * @brief print
   * @detail
   *   The print method prints all keywords.
   */
  virtual void print() const;

//------------------------------------------------------------------------------

protected:

  std::map<std::string, KeywordBase*> m_keywords { };      ///< Map of keywords

};

//-----------------------------------------------------------------------------

} /* namespace Fits */
} /* namespace ChDataModel */

#endif /* HEADER_H_ */
