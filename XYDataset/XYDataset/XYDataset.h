/**
 * @file XYDataset.h
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

namespace XYDataset {

   class XYDataset
   {

   public:

     typedef std::vector<std::pair<double, double>>::const_iterator const_iterator;


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
      * @param vector_pair
      * A vector of pair of doubles
       * @return
      * A unique pointer of XYDataset type
      */
     static std::unique_ptr<XYDataset> factory(std::vector<double>, std::vector<double>);

     /**
      * @brief Destructor
      */
     virtual ~XYDataset() { }

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
     size_t size() const { return m_values.size();}

   private:

     /**
      * @brief
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

     std::vector<std::pair<double, double>> m_values { };

   };

} /* namespace XYDataset */



#endif // XYDATASET_H_ 
