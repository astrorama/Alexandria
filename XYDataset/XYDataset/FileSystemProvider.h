/**
 * @file XYDataset/FileSystemProvider.h
 *
 * @date Apr 11, 2014
 * @author Nicolas Morisset
 */

#ifndef FILESYSTEMPROVIDER_H_
#define FILESYSTEMPROVIDER_H_


#include <memory>
#include <vector>
#include <string>
#include <map>

#include "ElementsKernel/Export.h"

#include "XYDataset/XYDataset.h"
#include "XYDataset/XYDatasetProvider.h"
#include "XYDataset/FileParser.h"

namespace Euclid {
namespace XYDataset {

/**
 * @class FileSystemProvider
 *
 * @brief
 * The FileSystemProvider handles files in a directory tree
 *
 * @details
 * It handles files in a directory tree of the file system. The directory path
 * of the files and the name of the dataset are used for constructing the
 * qualified name to match with the identifier. To support different file
 * formats the work is delegated to the FileParser interface about file related
 * operations (it gets dataset name and data).
 */

class ELEMENTS_API FileSystemProvider : public XYDatasetProvider
{
 public:

  /**
   * @brief constructor
   * The FileSystemProvider handles files in a directory tree.
   * @details
   * It fills up a map containing the qualified name and the path of the corresponding file.
   * @param root_path
   * Absolute path to the dataset
   * @param parser
   * FileParser object
   * @throw Elements::Exception
   * Path to the files not found
   * @throw Elements::Exception
   * Root path not found
   * @throw Elements::Exception
   * Root path is not a directory
   * @throw Elements::Exception
   * Qualified name can not be inserted
   */
  FileSystemProvider(const std::string& root_path, std::unique_ptr<FileParser> parser);

  /**
   * @brief
   * Get a dataset corresponding to an unique qualified name
   * @param qualified_name
   * Dataset qualified name
   * @return
   * A XYDataset unique pointer or null pointer
   */
  std::unique_ptr<XYDataset> getDataset(const QualifiedName& qualified_name) override;

  /**
   * @brief
   * List all files which belong to a group.
   * @details
   * Fill up a vector with qualified name from the map created at the constructor level.
   * In the vector, only qualified name where path contains the group name at the
   * first position is inserted.
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
   *  It is a string which represents a group: e.g. "filter/MER" for getting all MER filters.
   * @return
   * A vector of qualified names for the datasets in the files under the group or an empty
   * vector in case of no files for the group
   *
   */
  std::vector<QualifiedName> listContents(const std::string& group) override;

  // Default destructor
  ~FileSystemProvider() = default;

 private:

  std::string                          m_root_path;
  std::unique_ptr<FileParser>          m_parser;
  std::map<QualifiedName, std::string> m_name_file_map;
  std::vector<QualifiedName>           m_order_names;
};

} /* namespace XYDataset */
} // end of namespace Euclid

#endif // FILESYSTEMPROVIDER_H_
