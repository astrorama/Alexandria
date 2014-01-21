elements_subdir(ChDataModel 1.0)

#elements_depends_on_subdirs(ChTools)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)
find_package(Eigen3)


#===== Libraries ===============================================================

elements_add_library(ChDataModel src/*.cpp src/Fits/*.cpp src/lib/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost 
                  INCLUDE_DIRS Eigen3 Boost 
                  PUBLIC_HEADERS ChDataModel)


#===== Boost tests =============================================================

elements_add_unit_test(Catalog_test tests/src/Catalog_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

elements_add_unit_test(Photometry_test tests/src/Photometry_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)
                       
elements_add_unit_test(Sed_test tests/src/Sed_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

elements_add_unit_test(Source_test tests/src/Source_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

elements_add_unit_test(VectorPair_test tests/src/VectorPair_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

elements_add_unit_test(Keyword_test tests/src/Keyword_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

elements_add_unit_test(Header_test tests/src/Header_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

elements_add_unit_test(Image_test tests/src/Image_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

elements_add_unit_test(FilterName_test tests/src/FilterName_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

#-------------------------------------------------------------------------------

elements_add_unit_test(ChDataModel_all_tests tests/src/*_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataModel TYPE Boost)

#-------------------------------------------------------------------------------
