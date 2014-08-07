/** 
 * @file GridContainer/_impl/TemplateLoopCounter.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_TEMPLATELOOPCOUNTER_H
#define	GRIDCONTAINER_TEMPLATELOOPCOUNTER_H

namespace Grid {

/// This is a dummy class with a integer template parameter, which is used
/// as a counter for the template recursions.
template<int>
struct TemplateLoopCounter { };

}

#endif	/* GRIDCONTAINER_TEMPLATELOOPCOUNTER_H */

