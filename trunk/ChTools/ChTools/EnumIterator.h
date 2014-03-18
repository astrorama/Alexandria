/*
 * EnumIterator.h
 *
 *  Created on: Mar 8, 2013
 *      Author: Pavel Binko
 */

#ifndef ENUMITERATOR_H_
#define ENUMITERATOR_H_

#include <iterator>
#include <boost/range/iterator_range.hpp>

template<class enum_type>
class EnumIterator {
private:
  enum_type value;
  typedef typename std::underlying_type<enum_type>::type under;
public:
  typedef std::size_t size_type;
  typedef std::ptrdiff_t difference_type;
  typedef enum_type value_type;
  typedef enum_type reference;
  typedef enum_type* pointer;
  typedef std::random_access_iterator_tag iterator_category;

  constexpr EnumIterator() :
      value() {
  }
  constexpr EnumIterator(const EnumIterator& rhs) noexcept(true) :
      value(rhs.value) {
  }
  constexpr explicit EnumIterator(enum_type value_) noexcept(true) :
      value(value_) {
  }
  ~EnumIterator() noexcept(true) {
  }
  EnumIterator& operator=(const EnumIterator& rhs) noexcept(true) {
    value = rhs.value;
    return *this;
  }
  EnumIterator& operator++() noexcept(true) {
    value = (enum_type) (under(value) + 1);
    return *this;
  }
  EnumIterator operator++(int) noexcept(true) {
    EnumIterator r(*this);
    ++*this;
    return r;
  }
  EnumIterator& operator+=(size_type o) noexcept(true) {
    value = (enum_type) (under(value) + o);
    return *this;
  }
  friend constexpr EnumIterator operator+(const EnumIterator& it, size_type o)
      noexcept(true) {
    return EnumIterator((enum_type) (under(it) + o));
  }
  friend constexpr EnumIterator operator+(size_type o, const EnumIterator& it)
      noexcept(true) {
    return EnumIterator((enum_type) (under(it) + o));
  }
  EnumIterator& operator--() noexcept(true) {
    value = (enum_type) (under(value) - 1);
    return *this;
  }
  EnumIterator operator--(int) noexcept(true) {
    EnumIterator r(*this);
    --*this;
    return r;
  }
  EnumIterator& operator-=(size_type o) noexcept(true) {
    value = (enum_type) (under(value) + o);
    return *this;
  }
  friend constexpr EnumIterator operator-(const EnumIterator& it, size_type o)
      noexcept(true) {
    return EnumIterator((enum_type) (under(it) - o));
  }
  friend constexpr difference_type operator-(EnumIterator lhs, EnumIterator rhs)
      noexcept(true) {
    return under(lhs.value) - under(rhs.value);
  }
  constexpr reference operator*() const noexcept(true) {
    return value;
  }
  constexpr reference operator[](size_type o) const noexcept(true) {
    return (enum_type) (under(value) + o);
  }
  constexpr const enum_type* operator->() const noexcept(true) {
    return &value;
  }
  constexpr friend bool operator==(const EnumIterator& lhs,
      const EnumIterator& rhs) noexcept(true) {
    return lhs.value == rhs.value;
  }
  constexpr friend bool operator!=(const EnumIterator& lhs,
      const EnumIterator& rhs) noexcept(true) {
    return lhs.value != rhs.value;
  }
  constexpr friend bool operator<(const EnumIterator& lhs,
      const EnumIterator& rhs) noexcept(true) {
    return lhs.value < rhs.value;
  }
  constexpr friend bool operator>(const EnumIterator& lhs,
      const EnumIterator& rhs) noexcept(true) {
    return lhs.value > rhs.value;
  }
  constexpr friend bool operator<=(const EnumIterator& lhs,
      const EnumIterator& rhs) noexcept(true) {
    return lhs.value <= rhs.value;
  }
  constexpr friend bool operator>=(const EnumIterator& lhs,
      const EnumIterator& rhs) noexcept(true) {
    return lhs.value >= rhs.value;
  }
  friend void swap(const EnumIterator& lhs, const EnumIterator& rhs)
      noexcept(true) {
    std::swap(lhs.value, rhs.value);
  }
};

//template<class enum_type> constexpr boost::iterator_range<EnumIterator<enum_type>> getRange() noexcept(true) {
//  return boost::make_iterator_range(EnumIterator<enum_type>(enum_type::First), EnumIterator<enum_type>(enum_type::Last));
//}

#endif /* ENUMITERATOR_H_ */
