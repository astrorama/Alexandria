/**
 * @file Header.cpp
 *
 * Created on: Sep 18, 2013
 *     Author: Pavel Binko
 */

#include <typeinfo>
#include <sstream>

#include "ElementsKernel/ElementsException.h"

#include "ChDataModel/Fits/Header.h"
#include "ChDataModel/Fits/Keyword.h"

using namespace std;

namespace ChDataModel {
namespace Fits {

//------------------------------------------------------------------------------

Header::Header(const Header & header) {

  for (auto it = header.m_keywords.begin(); it != header.m_keywords.end();
      it++) {
    m_keywords[it->second->getName()] = it->second->keywordClone();
  }

} // Eof constructor

//------------------------------------------------------------------------------

Header::~Header() {

  // Deletes also all keywords in the header
  for (auto it = m_keywords.begin(); it != m_keywords.end(); it++) {
    delete it->second;
  }

} // Eof destructor

//------------------------------------------------------------------------------

Header & Header::operator =(const Header & header) {

  if (this != &header) {

    for (auto it = m_keywords.begin(); it != m_keywords.end(); it++) {
      delete it->second;
    }
    m_keywords.clear();

    for (auto it = header.m_keywords.begin(); it != header.m_keywords.end();
        it++) {
      m_keywords[it->second->getName()] = it->second->keywordClone();
    }

  }

  return *this;

} // Eof Header::operator =

//------------------------------------------------------------------------------

bool Header::operator ==(const Header & header) const {

  if (m_keywords.size() != header.m_keywords.size()) {
    return false;
  }

  for (auto it = m_keywords.begin(); it != m_keywords.end(); it++) {

    // Bool
    if (typeid(*(it->second)) == typeid(BoolKeyword)) {
      if (!(*dynamic_cast<BoolKeyword *>(it->second)
          == *dynamic_cast<BoolKeyword *>(header.m_keywords.at(it->first)))) {
        return false;
      }
    }

    // Int
    else if (typeid(*(it->second)) == typeid(LongKeyword)) {
      if (!(*dynamic_cast<LongKeyword *>(it->second)
          == *dynamic_cast<LongKeyword *>(header.m_keywords.at(it->first)))) {
        return false;
      }
    }

    // Double
    else if (typeid(*(it->second)) == typeid(DoubleKeyword)) {
      if (!(*dynamic_cast<DoubleKeyword *>(it->second)
          == *dynamic_cast<DoubleKeyword *>(header.m_keywords.at(it->first)))) {
        return false;
      }
    }

    // String
    else if (typeid(*(it->second)) == typeid(StringKeyword)) {
      if (!(*dynamic_cast<StringKeyword *>(it->second)
          == *dynamic_cast<StringKeyword *>(header.m_keywords.at(it->first)))) {
        return false;
      }
    }

    // Unknown types
    else {
      throw ElementsException(
          "DataModel::Fits::Header : Unknown type of Keyword<T>.");
    }
  }

  return true;

} // Eof Header::operator ==

//------------------------------------------------------------------------------

void Header::addKeyword(const KeywordBase & keyword) {

  // If a keyword with the same name exists in the map, delete it first
  deleteKeyword(keyword.getName());

  // Add the new keyword into the map
  m_keywords[keyword.getName()] = keyword.keywordClone();

} // Eof Header::addKeyword

//------------------------------------------------------------------------------

void Header::addKeyword(const std::string & name, bool value,
    const std::string & comment) {

  // Create a keyword
  BoolKeyword * keyword = new BoolKeyword(name, value, comment);

  // If a keyword with the same name exists in the map, delete it first
  deleteKeyword(keyword->getName());

  // Add the new keyword into the map
  m_keywords[keyword->getName()] = keyword;

} // Eof Header::addKeyword

//------------------------------------------------------------------------------

void Header::addKeyword(const std::string & name, double value,
    const std::string & comment) {
  DoubleKeyword * keyword = new DoubleKeyword(name, value, comment);
  deleteKeyword(keyword->getName());
  m_keywords[keyword->getName()] = keyword;
} // Eof Header::addKeyword

//------------------------------------------------------------------------------

void Header::addKeyword(const std::string & name, long value,
    const std::string & comment) {
  LongKeyword * keyword = new LongKeyword(name, value, comment);
  deleteKeyword(keyword->getName());
  m_keywords[keyword->getName()] = keyword;
} // Eof Header::addKeyword

//------------------------------------------------------------------------------

void Header::addKeyword(const std::string & name, const std::string & value,
    const std::string & comment) {
  StringKeyword * keyword = new StringKeyword(name, value, comment);
  deleteKeyword(keyword->getName());
  m_keywords[keyword->getName()] = keyword;
} // Eof Header::addKeyword

//------------------------------------------------------------------------------

bool Header::existKeyword(const std::string & keywordName) const {

  return m_keywords.find(keywordName) != m_keywords.end();

} // Eof Header::existKeyword

//------------------------------------------------------------------------------

KeywordBase & Header::getKeyword(const std::string & keywordName) const {

  return *(m_keywords.at(keywordName));

} // Eof Header::getKeyword

//------------------------------------------------------------------------------

void Header::deleteKeyword(const std::string & keywordName) {

  // Erase the entry from the map and delete the keyword object
  auto it = m_keywords.find(keywordName);
  if (it != m_keywords.end()) {
    delete it->second;
    m_keywords.erase(it);
  }

} // Eof Header::deleteKeyword

//------------------------------------------------------------------------------

void Header::print() const {

  cout << "----------------------------------------------------------" << endl;
  cout << "          Header contents" << endl;
  cout << "----------------------------------------------------------" << endl;

  for (auto & it : m_keywords) {

    cout << "Keyword name = " << it.first;
    KeywordTypes type = it.second->getType();
    cout << "     Type = " << type;

    switch (type) {
      case KeywordTypes::Bool : {                                  // Bool
        cout << "     Value (within ||) = |"
            << dynamic_cast<BoolKeyword *>(it.second)->getValue() << "|";
        break;
      }
      case KeywordTypes::Double : {                                // Double
        cout << "     Value (within ||) = |"
            << dynamic_cast<DoubleKeyword *>(it.second)->getValue() << "|";
        break;
      }
      case KeywordTypes::Long : {                                  // Long
        cout << "     Value (within ||) = |"
            << dynamic_cast<LongKeyword *>(it.second)->getValue() << "|";
        break;
      }
      case KeywordTypes::String : {                                // String
        cout << "     Value (within ||) = |"
            << dynamic_cast<StringKeyword *>(it.second)->getValue() << "|";
        break;
      }
      default : {                                                  // The rest
        stringstream errorBuffer;
        errorBuffer << "ChDataModel::Header::print : The keyword " << it.first
            << " has an unknown type " << type << "." << endl;
        throw ElementsException(errorBuffer.str());
      }
    } // Eof switch

    if (it.first != "COMMENT") {
      cout << "   Comment = " << it.second->getComment();
    }
    cout << endl;

  } // Eof for

} // Eof Header::print

//------------------------------------------------------------------------------

} /* namespace Fits */
} /* namespace ChDataModel */
