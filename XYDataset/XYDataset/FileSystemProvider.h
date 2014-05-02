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
#include "XYDataset/XYDataset.h"
#include "XYDataset/XYDatasetProvider.h"
#include "XYDataset/FileParser.h"

namespace XYDataset {

/**
 *
 *
 */
/**
 * @class FileSystemProvider
 *
 * @brief The FileSystemProvider handles files in a directory tree
 *
 * @details
 * It handles files in a directory tree of the file system. The directory path
 * of the files and the name of the dataset are used for constructing the
 * qualified name to match with the identifier. To support different file
 * formats the work is delegated to the FileParser interface for file related
 * operations (gets dataset name and data)
 */

template <typename T>

class FileSystemProvider : public XYDatasetProvider<T>
{
 public:

  /**
   * @brief constructor
   * @param root_path : path to the dataset
   * @param parser : FileParser object
   */
  FileSystemProvider(const std::string& root_path, std::unique_ptr<FileParser> parser) :
                     m_root_path(root_path), m_parser(std::move(parser)) { }

  /**
   * @brief Get a dataset from an identifier
   * @param identifier : dataset's identifier
   */
  std::unique_ptr<XYDataset> getDataset(const T & identifier) override;

  /**
   * @brief List the files contained into a directory (group)
   * @param group
   *  path to a set of directories/files
   * @return
   * A vector of strings of the filenames found including the path
   * @throw ElementsException: Path to the files not found
   * @throw ElementsException: The group is not a directory
   */
  std::vector<std::string> listContents(const std::string& group) override;


 private:

  std::string                  m_root_path;
  std::unique_ptr<FileParser>  m_parser;

};

} /* namespace XYDataset */

#define FILESYSTEMPROVIDER_IMPL
#include "XYDataset/_impl/FileSystemProvider.icpp"
#undef FILESYSTEMPROVIDER_IMPL

#endif // FILESYSTEMPROVIDER_H_ 
