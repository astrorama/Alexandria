/** 
 * @file tests/src/serialization/NonDefaultConstructibleClass.h
 * @date June 27, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H
#define	GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H

class NonDefaultConstructibleClass {
public:
  NonDefaultConstructibleClass(double v) : value{v} {}
  double value = 0;
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

#endif	/* GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H */

