/**
 * @file Keyword.h
 *
 * Created on: Sep 20, 2013
 *     Author: Pavel Binko
 */

#ifndef KEYWORD_H_
#define KEYWORD_H_

#include <string>
#include <typeinfo>

#include "ElementsKernel/ElementsException.h"
#include "ChDataModel/Enumerations/KeywordTypes.h"

namespace ChDataModel {
namespace Fits {

//------------------------------------------------------------------------------
// Forward declarations

template<class T> class Keyword;

// FITS standard speaks about 4 data types : integer, string, logical, real
typedef Keyword<bool> BoolKeyword;
typedef Keyword<long> LongKeyword;
typedef Keyword<double> DoubleKeyword;
typedef Keyword<std::string> StringKeyword;

//------------------------------------------------------------------------------

/**
 * @class KeywordBase
 * @brief
 *   The KeywordBase class contains the name, type and comment of a keyword.
 * @details
 *   Its value is contained in the templated class Keyword.
 */
class KeywordBase {

public:

  /**
   * @brief Constructor
   */
  KeywordBase() :
      m_name(""), m_type(KeywordTypes::None), m_comment("") {
  }

  /**
   * @brief Constructor
   * @param name
   *   Name of the keyword
   * @param type
   *   Type of the keyword
   * @param comment
   *   Comment of the keyword
   */
  KeywordBase(const std::string & name, const KeywordTypes type,
      const std::string & comment = "") :
      m_name(name), m_type(type), m_comment(comment) {
  }

  /**
   * @brief Copy constructor
   * @param keyword
   *   Reference to a KeywordBase object
   */
  KeywordBase(const KeywordBase & keyword);

  /**
   * @brief Virtual destructor
   */
  virtual ~KeywordBase() {
  }

//------------------------------------------------------------------------------

  /**
   * @brief Assignment operator
   */
  virtual KeywordBase & operator =(const KeywordBase & keyword);

  /**
   * @brief Equal operator
   */
  virtual bool operator ==(const KeywordBase & keyword) const;

  /**
   * @brief Cast operators
   */
  operator BoolKeyword &();
  operator LongKeyword &();
  operator DoubleKeyword &();
  operator StringKeyword &();

//------------------------------------------------------------------------------

  /**
   * @brief keywordClone
   * @param name
   *   Name of the keyword
   * @return
   *   Pointer to the cloned KeywordBase object
   */
  virtual KeywordBase * keywordClone() const = 0;

//------------------------------------------------------------------------------

  /**
   * @brief Getters
   */
  virtual const std::string getName() const {
    return m_name.c_str();
  }

  virtual KeywordTypes getType() const {
    return m_type;
  }

  virtual const std::string getComment() const {
    return m_comment.c_str();
  }

  /**
   * @brief Setters
   */
  virtual void setName(const std::string& name) {
    m_name = name;
  }

  virtual void setComment(const std::string& comment) {
    m_comment = comment;
  }

protected:

  virtual void setType(const KeywordTypes type) {
    m_type = type;
  }

//------------------------------------------------------------------------------

protected:

  std::string m_name { };                     ///< Name of this keyword
  KeywordTypes m_type = KeywordTypes::None;   ///< Type of this keyword

  std::string m_comment { };                  ///< Comment of this keyword

};

//==============================================================================

/**
 * @class Keyword
 * @brief
 *   The Keyword class contains the value of a keyword.
 * @details
 *   Its name, type and comment are contained in the class KeywordBase.
 */
template<class T>
class Keyword: public KeywordBase {

public:

  /**
   * @brief Constructor
   * @details
   *   It checks the type of the keyword value and
   *   sets the type member data if it is a correct one.
   *   If the type is not correct, an exception will be thrown.
   *   Then it creates an empty keyword object.
   */
  Keyword() {
    checkAndSetTypeOfTemplateParameter();
  }

  /**
   * @brief Constructor
   * @details
   *   It checks the type of the keyword value and
   *   sets the type member data if it is a correct one.
   *   If the type is not correct, an exception will be thrown.
   *   Then it creates a keyword object with the given parameters.
   * @param name
   *   Name of the keyword
   * @tparam value
   *   Value of the keyword
   * @param comment
   *   Comment of the keyword
   */
  Keyword(const std::string & name, T value, const std::string & comment) {
    setName(name);
    m_value = value;
    checkAndSetTypeOfTemplateParameter();
    setComment(comment);
  }

  /**
   * @brief Copy constructor
   * @param keyword
   *   Reference to a Keyword object
   */
  Keyword(const Keyword<T> & keyword) :
      KeywordBase(keyword) {
    m_value = keyword.m_value;
  }

  /**
   * @brief Virtual destructor
   */
  virtual ~Keyword() {
  }

//------------------------------------------------------------------------------

  /**
   * @brief Assignment operator
   */
  using KeywordBase::operator=;
  virtual Keyword<T> & operator =(const Keyword<T> & keyword) {
    KeywordBase::operator =(keyword);
    m_value = keyword.m_value;
    return *this;
  }

  /**
   * @brief Assignment operator
   */
  virtual Keyword<T> & operator =(const T & value) {
    m_value = value;
    return *this;
  }

  /**
   * @brief Equal operator
   */
  virtual bool operator ==(const KeywordBase & keyword) const {
    return KeywordBase::operator ==(keyword)
        && m_value == ((Keyword<T>&) keyword).m_value;
  }

//------------------------------------------------------------------------------

  /**
   * @brief Getter
   */
  virtual T getValue() const {
    return m_value;
  }

  /**
   * @brief Setter
   */
  virtual void setValue(T value) {
    m_value = value;
  }

//------------------------------------------------------------------------------

  /**
   * @brief keywordClone
   * @param name
   *   Name of the keyword
   * @return
   *   Pointer to the cloned KeywordBase object
   */
  virtual KeywordBase * keywordClone() const {
    return new Keyword<T>(*this);
  }

//------------------------------------------------------------------------------

protected:

  T m_value { };                              ///< Value of this keyword

//------------------------------------------------------------------------------

private:

  /**
   * @brief checkAndSetTypeOfTemplateParameter
   * @details
   *   It checks the type of the keyword value and
   *   sets the type member data if it is a correct one.
   *   If the type is not correct, an exception will be thrown.
   */
  void checkAndSetTypeOfTemplateParameter() {
    if (typeid(T) == typeid(bool)) {
      setType(KeywordTypes::Bool);                          // Bool
    }
    else if (typeid(T) == typeid(double)) {
      setType(KeywordTypes::Double);                        // Double
    }
    else if (typeid(T) == typeid(long)) {
      setType(KeywordTypes::Long);                          // Long
    }
    else if (typeid(T) == typeid(std::string)) {
      setType(KeywordTypes::String);                        // String
    }
    else {
      throw ElementsException(
          "ChDataModel::Fits::Keyword : Unknown type of Keyword<T>.");
    }
    // Note: The switch command cannot be used, because the c++ compiler
    // does not accept typeid as the switch argument
    // (it must be integer or enumeration type)
  }

};

//==============================================================================

// Implementation of the cast operators

inline KeywordBase::operator BoolKeyword &() {
  return dynamic_cast<BoolKeyword &>(*this);
}
inline KeywordBase::operator LongKeyword &() {
  return dynamic_cast<LongKeyword &>(*this);
}
inline KeywordBase::operator DoubleKeyword &() {
  return dynamic_cast<DoubleKeyword &>(*this);
}
inline KeywordBase::operator StringKeyword &() {
  return dynamic_cast<StringKeyword &>(*this);
}

//------------------------------------------------------------------------------

} /* namespace Fits */
} /* namespace ChDataModel */

#endif /* KEYWORD_H_ */
