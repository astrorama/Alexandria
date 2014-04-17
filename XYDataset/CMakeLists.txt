elements_subdir(XYDataset 1.0)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)
find_package(Eigen3)


#===== Libraries ===============================================================

elements_add_library(XYDataset src/lib/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost 
                  INCLUDE_DIRS Eigen3 Boost 
                  PUBLIC_HEADERS XYDataset)


#===== Boost tests =============================================================

elements_add_unit_test(XYDataset_test tests/src/XYDataset_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES XYDataset TYPE Boost)

#elements_add_unit_test(FileSystemProvider_test tests/src/FileSystemProvider_test.cpp tests/src/TestMain.cpp
#                       LINK_LIBRARIES XYDataset TYPE Boost)


#-------------------------------------------------------------------------------

#elements_add_unit_test(XYDataset_all_tests tests/src/*_test.cpp tests/src/TestMain.cpp
#                       LINK_LIBRARIES XYDataset TYPE Boost)

#-------------------------------------------------------------------------------
