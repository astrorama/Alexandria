/**
 * @file XYDataset/CachedProvider.h
 * @date 08/14/18
 * @author aalvarez
 *
 * @copyright (C) 2012-2020 Euclid Science Ground Segment
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
 *
 */

#ifndef _XYDATASET_CACHEDPROVIDER_H
#define _XYDATASET_CACHEDPROVIDER_H

#include <map>
#include <string>

#include "ElementsKernel/Export.h"
#include "XYDatasetProvider.h"
#include "QualifiedName.h"

namespace Euclid {
namespace XYDataset {

/**
 * @class CachedProvider
 * @brief
 * The CachedProvider wraps another XYDatasetProvider and keeps in memory
 * the results, so following calls are cheaper.
 *
 */
class ELEMENTS_API CachedProvider: public XYDatasetProvider {

public:

  /**
   * @brief Destructor
   */
  virtual ~CachedProvider() = default;

  explicit CachedProvider(std::shared_ptr<XYDatasetProvider> provider);

  /**
   * @brief
   * Virtual function to list all files contents in the "group" path
   * @details
   * let's take the following example. if you have a group sets to "A/B/C" and
   * under the "C" repository there is the following structure :
   * C/file1
   * C/file2
   * C/D/file3
   * etc...
   * then the vector of strings returned will contain the following elements:
   * vector[0] = "A/B/C/file1"
   * vector[1] = "A/B/C/file2"
   * vector[3] = "A/B/C/D/file3"
   * etc...
   * Note: The empty string for the group means the root group
   * @param group
   * Name of the dataset group
   * @return
   * A vector of the qualified names of all datasets inside the given group (recursively)
   */
  std::vector<QualifiedName> listContents(const std::string& group) override;

  /**
   * @brief
   * Virtual function for getting from a qualified name the dataset of
   * XYDataset type
   * @param qualified_name
   * Qualified name of the dataset
   * @return
   * A unique pointer of XYDataset type to the dataset
   */
  std::unique_ptr<XYDataset> getDataset(const QualifiedName& qualified_name) override;


  std::string getParameter(const QualifiedName& qualified_name, const std::string& key_word) override;

private:
  std::shared_ptr<XYDatasetProvider> m_provider;
  std::map<std::string, std::vector<QualifiedName>> m_list_cache;
  std::map<QualifiedName, std::unique_ptr<XYDataset>> m_dataset;

};  // End of CachedProvider class

}  // namespace XYDataset
}  // namespace Euclid

#endif
