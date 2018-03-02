
#ifndef ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H
#define ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H

// Boost, starting from version 1.56, provides serialization for the templated
// std::array. This file provides basic serialization support for versions
// before that. Note that if the boost version exists it is used instead.

#include <boost/version.hpp>

#if (BOOST_VERSION / 100000) <= 1 && ((BOOST_VERSION / 100) % 1000) < 56

#include <array>

namespace boost {
namespace serialization {

template <class Archive, std::size_t ND, typename CellType>
void serialize(Archive& archive, std::array<CellType, ND>& array, const unsigned int) {
  for (int i = 0; i < ND; ++i) {
    archive & array[i];
  }
}

}
}

#else

#include <boost/serialization/array.hpp>

#endif

#endif /* ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H */

