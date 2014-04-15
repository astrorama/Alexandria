elements_subdir(ChCatalog 1.0)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)
find_package(Eigen3)


#===== Libraries ===============================================================

elements_add_library(ChCatalog src/lib/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost 
                  INCLUDE_DIRS Eigen3 Boost 
                  PUBLIC_HEADERS ChCatalog)


#===== Boost tests =============================================================

elements_add_unit_test(Catalog_test tests/src/Catalog_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChCatalog TYPE Boost)

elements_add_unit_test(Photometry_test tests/src/SourceAttributes/Photometry_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChCatalog TYPE Boost)
 
elements_add_unit_test(Coordinates_test tests/src/SourceAttributes/Coordinates_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChCatalog TYPE Boost)

elements_add_unit_test(SpectroscopicRedshift_test tests/src/SourceAttributes/SpectroscopicRedshift_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChCatalog TYPE Boost)
                       
elements_add_unit_test(Source_test tests/src/Source_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChCatalog TYPE Boost)

elements_add_unit_test(FilterName_test tests/src/FilterName_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChCatalog TYPE Boost)

#-------------------------------------------------------------------------------

elements_add_unit_test(ChCatalog_all_tests tests/src/*_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChCatalog TYPE Boost)

#-------------------------------------------------------------------------------
