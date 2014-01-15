/**
 * @file Keyword.cpp
 *
 * Created on: Sep 17, 2013
 *     Author: Pavel Binko
 */

#include "ChDataModel/Fits/Keyword.h"

#include <iostream>

using namespace std;

namespace ChDataModel {
namespace Fits {

//------------------------------------------------------------------------------

KeywordBase::KeywordBase(const KeywordBase & keyword) {
  m_name    = keyword.m_name;
  m_type    = keyword.m_type;
  m_comment = keyword.m_comment;
}

//------------------------------------------------------------------------------

KeywordBase & KeywordBase::operator = (const KeywordBase & keyword) {
  m_name    = keyword.m_name;
  m_type    = keyword.m_type;
  m_comment = keyword.m_comment;
  return *this;
}

//------------------------------------------------------------------------------

bool KeywordBase::operator == (const KeywordBase & keyword) const {
  return m_name    == keyword.m_name &&
         m_type    == keyword.m_type &&
         m_comment == keyword.m_comment;
}

//------------------------------------------------------------------------------

} /* namespace Fits */
} /* namespace ChDataModel */

