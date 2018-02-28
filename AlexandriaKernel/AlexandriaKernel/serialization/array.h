
#ifndef ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H
#define ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H

#include <array>

namespace boost {
namespace serialization {

template <class Archive, std::size_t ND, typename CellType>
void serialize(Archive& archive, std::array<CellType, ND> array, const unsigned int) {
  for (int i = 0; i < ND; ++i) {
    archive & array[i];
  }
}

}
}

#endif /* ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H */

