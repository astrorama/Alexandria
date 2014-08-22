/**
 * @file XYDataset/XYDataset.h
 *
 * @date Apr 8, 2014
 * @author admin
 */

#ifndef XYDATASET_H_
#define XYDATASET_H_

#include <memory>
#include <vector>
#include <string>
#include <iterator>
#include <utility>

#include "ElementsKernel/Export.h"

namespace Euclid {
namespace XYDataset {

/**
 * @class Euclid::XYDataset::XYDataset
 * Interface class
 * @brief
 * This module provides an interface for accessing two dimensional datasets
 * (pairs of (X,Y) values) stored in some storage (file system, database, etc)
 * @details
 * The datasets are organized in groups (nested groups are allowed, which
 * create a tree) and they can be uniquely identified by their qualified name,
 * which consists of the group names and the dataset name, separated by slashes
 * "/" for example "groupA/groupB/name". Note that datasets might not belong
 * to any group (or alternatively that they might belong to the root group), in
 * which case they are accessed by just using their name (no leading slash).
 * The module abstracts the nature of the storage and the only assumption is
 * that the datasets can be accessed using their qualified names.
 * @throw
 * ElementException :  Vectors must have the same size!
 */

 class ELEMENTS_API XYDataset
 {

 public:

   typedef std::vector<std::pair<double, double>>::const_iterator const_iterator;

   /**
    * @brief Constructor
    * XYDataset interface represents an immutable data set
    *
    * @details
    * XYDataset interface represents an immutable data set, where both X and Y axes contain double values.
    * It provides iterators both for the (X,Y) pairs and for the axes values independently.
    *
    * @param values
    * A vector of pair of doubles
    *
    */
   XYDataset(std::vector<std::pair<double, double>> values)
             : m_values(values) {  };

   /**
    * @brief
    * Make a XYDataset object from a vector of pair of doubles
    * @param vector_pair
    * A vector of pair of doubles
     * @return
    * A unique pointer of XYDataset type
    */
   static std::unique_ptr<XYDataset> factory(std::vector<std::pair<double, double>> vector_pair);

   /**
    * @brief
    * Make a XYDataset object from two vectors of doubles
    * @param x
    * A vector of double values
    * @param y
    * A vector of double values
     * @return
    * A unique pointer of XYDataset type
    */
   static std::unique_ptr<XYDataset> factory(std::vector<double> x, std::vector<double> y);

   /**
    * @brief Destructor
    */
   virtual ~XYDataset() = default;

   /**
    * @brief
    * Returns a const iterator to the first pair of the dataset
    * @return
    * An iterator to the first pair
    */
   const_iterator begin() const;

   /**
    * @brief
    * Returns a const iterator to the last pair dataset
    * @return
    * An iterator to the last pair dataset
    */
   const_iterator end() const;

   /**
    * @brief
    *  Get the size of the vector container
    * @return
    *  The size of the container which is the number of Source objects
    */
   size_t size() const { return m_values.size(); }

 private:

   std::vector<std::pair<double, double>> m_values { };

 };

} /* namespace XYDataset */
} // end of namespace Euclid



#endif // XYDATASET_H_
