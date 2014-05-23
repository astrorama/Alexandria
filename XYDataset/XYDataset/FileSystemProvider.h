/**
 * @file FileSystemProvider.h
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

#include "XYDataset/XYDataset.h"
#include "XYDataset/XYDatasetProvider.h"
#include "XYDataset/FileParser.h"

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
 * operations (it gets dataset name and data)
 */

class FileSystemProvider : public XYDatasetProvider
{
 public:

  /**
   * @brief constructor
   * @param root_path : path to the dataset
   * @param parser : FileParser object
   * @throw ElementsException : path to the files not found
   * @throw ElementsException : root path not found
   * @throw ElementsException : root path is not a directory
   * @throw ElementsException : qualified name can not be inserted
   */
  FileSystemProvider(const std::string& root_path, std::unique_ptr<FileParser> parser);

  /**
   * @brief
   * Get a dataset corresponding to an unique qualified name
   *
   * @param qualified_name : dataset's qualified name
   * @return
   * A XYDataset unique pointer or null pointer
   */
  std::unique_ptr<XYDataset> getDataset(const QualifiedName& qualified_name) override;

  /**
   * @brief
   * List the files which belong to a group.
   * @details
   * As an example
   * @param group
   *  It is a string which represents a group as for instance: "filter/MER" if
   *  you want all MER filters.
   * @return
   * A vector of qualified names for the datasets in the files under the group or an empty
   * vector in case of no files for the group
   *
   */
  std::vector<QualifiedName> listContents(const std::string& group) override;


 private:

  std::string                          m_root_path;
  std::unique_ptr<FileParser>          m_parser;
  std::map<QualifiedName, std::string> m_map;

};

} /* namespace XYDataset */

#endif // FILESYSTEMPROVIDER_H_ 
