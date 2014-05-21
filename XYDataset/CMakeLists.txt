elements_subdir(XYDataset 1.0)
elements_depends_on_subdirs(ChTable)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)

#===== Libraries ===============================================================

elements_add_library(XYDataset src/lib/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost ChTable
                  INCLUDE_DIRS Boost ChTable
                  PUBLIC_HEADERS XYDataset )


#===== Boost tests =============================================================

elements_add_unit_test(XYDataset_test tests/src/XYDataset_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES XYDataset TYPE Boost ChTable)

elements_add_unit_test(FileSystemProvider_test tests/src/FileSystemProvider_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES XYDataset TYPE Boost ChTable)

elements_add_unit_test(AsciiParser_test tests/src/AsciiParser_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES XYDataset TYPE Boost ChTable)

elements_add_unit_test(QualifiedName_test tests/src/QualifiedName_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES XYDataset TYPE Boost ChTable)

#-------------------------------------------------------------------------------

#elements_add_unit_test(XYDataset_all_tests tests/src/*_test.cpp tests/src/TestMain.cpp
#                       LINK_LIBRARIES XYDataset TYPE Boost ChTable)

#-------------------------------------------------------------------------------
