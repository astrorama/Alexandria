/** 
 * @file tests/src/serialization/DefaultConstructibleClass.h
 * @date June 27, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_DEFAULTCONSTRUCTIBLECLASS_H
#define	CHMATRIX_DEFAULTCONSTRUCTIBLECLASS_H

class DefaultConstructibleClass {
public:
  DefaultConstructibleClass() {}
  double value = 0;
};

namespace boost {
namespace serialization {

template<typename Archive>
void serialize(Archive& ar, DefaultConstructibleClass& c, const unsigned int) {
  ar & c.value;
}

}
}

#endif	/* CHMATRIX_DEFAULTCONSTRUCTIBLECLASS_H */

