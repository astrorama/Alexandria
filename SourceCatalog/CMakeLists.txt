elements_subdir(SourceCatalog 1.0)

elements_depends_on_subdirs(ChTable)

elements_depends_on_subdirs(ElementsKernel)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)
find_package(Eigen3)


#===== Libraries ===============================================================

elements_add_library(SourceCatalog src/lib/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost ChTable
                  INCLUDE_DIRS Eigen3 Boost ChTable
                  PUBLIC_HEADERS SourceCatalog)


#===== Boost tests =============================================================


elements_add_unit_test(Photometry_test tests/src/SourceAttributes/Photometry_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

elements_add_unit_test(PhotometryAttributeFromRow_test tests/src/SourceAttributes/PhotometryAttributeFromRow_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

elements_add_unit_test(Coordinates_test tests/src/SourceAttributes/Coordinates_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

elements_add_unit_test(SpectroscopicRedshift_test tests/src/SourceAttributes/SpectroscopicRedshift_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

elements_add_unit_test(SpectroscopicRedshiftAttributeFromRow_test tests/src/SourceAttributes/SpectroscopicRedshiftAttributeFromRow_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

elements_add_unit_test(Source_test tests/src/Source_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

elements_add_unit_test(Catalog_test tests/src/Catalog_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

#-------------------------------------------------------------------------------

elements_add_unit_test(SourceCatalog_all_attribute_tests tests/src/SourceAttributes/*_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

elements_add_unit_test(SourceCatalog_all_tests tests/src/*_test.cpp
                       LINK_LIBRARIES SourceCatalog TYPE Boost)

#-------------------------------------------------------------------------------
