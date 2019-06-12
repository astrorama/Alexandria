/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
 *  
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free 
 * Software Foundation; either version 3.0 of the License, or (at your option)  
 * any later version.  
 *  
 * This library is distributed in the hope that it will be useful, but WITHOUT 
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  
 * details.  
 *  
 * You should have received a copy of the GNU Lesser General Public License 
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA  
 */
 
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
             : m_values(std::move(values)) {  };

   /// Copy constructor
   XYDataset(const XYDataset&) = default;

   /// Move constructor
   XYDataset(XYDataset&&) = default;

   /**
    * @brief
    * Make a XYDataset object from a vector of pair of doubles
    * @param vector_pair
    * A vector of pair of doubles
     * @return
    * A unique pointer of XYDataset type
    */
   static XYDataset factory(std::vector<std::pair<double, double>> vector_pair);

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
   static XYDataset factory(const std::vector<double>& x, const std::vector<double>& y);

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
    * Returns a const iterator to the one after last pair dataset
    * @return
    * An iterator to the last pair dataset
    */
   const_iterator end() const;
   
   /**
    * @brief
    * Returns a reference to the first pair of the dataset
    * @return 
    * A reference to the first pair of the dataset
    */
   const std::pair<double, double>& front() const;
   
   /**
    * @brief
    * Returns a reference to the last pair of the dataset
    * @return 
    * A reference to the last pair of the dataset
    */
   const std::pair<double, double>& back() const;
   
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
