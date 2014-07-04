/** 
 * @file ChMatrix/_impl/TemplateLoopCounter.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_TEMPLATELOOPCOUNTER_H
#define	CHMATRIX_TEMPLATELOOPCOUNTER_H

namespace ChMatrix {

/// This is a dummy class with a integer template parameter, which is used
/// as a counter for the template recursions.
template<int>
struct TemplateLoopCounter { };

}

#endif	/* CHMATRIX_TEMPLATELOOPCOUNTER_H */

