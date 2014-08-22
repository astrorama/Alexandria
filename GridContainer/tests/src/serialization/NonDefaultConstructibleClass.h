/** 
 * @file tests/src/serialization/NonDefaultConstructibleClass.h
 * @date June 27, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H
#define	GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H

#include "GridContainer/GridCellManagerTraits.h"

class NonDefaultConstructibleClass {
public:
  NonDefaultConstructibleClass(double v) : value{v} {}
  double value;
};

namespace boost {
namespace serialization {

template<typename Archive>
void serialize(Archive&, NonDefaultConstructibleClass&, const unsigned int) { }

template<typename Archive>
void save_construct_data(Archive &ar, const NonDefaultConstructibleClass* p, const unsigned int) {
  double v = p->value;
  ar << v;
}

template<typename Archive>
void load_construct_data(Archive &ar, NonDefaultConstructibleClass* p, const unsigned int) {
  double v;
  ar >> v;
  ::new(p) NonDefaultConstructibleClass(v);
}

}
}

namespace Euclid {
namespace Grid {

template<>
struct GridCellManagerTraits<std::vector<NonDefaultConstructibleClass>> {
  typedef NonDefaultConstructibleClass data_type;
  typedef typename std::vector<NonDefaultConstructibleClass>::iterator iterator;
  static std::unique_ptr<std::vector<NonDefaultConstructibleClass>> factory(size_t size) {
    return std::unique_ptr<std::vector<NonDefaultConstructibleClass>> {new std::vector<NonDefaultConstructibleClass>(size, NonDefaultConstructibleClass{0})};
  }
  static size_t size(const std::vector<NonDefaultConstructibleClass>& vector){
    return vector.size();
  }
  static iterator begin(std::vector<NonDefaultConstructibleClass>& vector) {
    return vector.begin();
  }
  static iterator end(std::vector<NonDefaultConstructibleClass>& vector) {
    return vector.end();
  }
  static const bool enable_boost_serialize = true;
  
};

}
} // end of namespace Euclid

#endif	/* GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H */

