elements_subdir(GridContainer)

elements_depends_on_subdirs(ElementsKernel XYDataset)
find_package(Boost REQUIRED COMPONENTS system serialization filesystem)
find_package(CCfits)

#===== Libraries ===============================================================

elements_add_library(GridContainer src/lib/*.cpp
                     LINK_LIBRARIES Boost ElementsKernel CCfits XYDataset
                     INCLUDE_DIRS CCfits
                     PUBLIC_HEADERS GridContainer)

#===== Boost tests =============================================================

elements_add_unit_test(GridAxis_test tests/src/GridAxis_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)

elements_add_unit_test(GridAxis_serialization_test tests/src/serialization/GridAxis_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)

elements_add_unit_test(tuple_serialization_test tests/src/serialization/tuple_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)

elements_add_unit_test(GridConstructionHelper_test tests/src/GridConstructionHelper_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)

elements_add_unit_test(GridIndexHelper_test tests/src/GridIndexHelper_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)

elements_add_unit_test(GridCellManagerTraits_test tests/src/GridCellManagerTraits_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)

elements_add_unit_test(GridContainer_test tests/src/GridContainer_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)

elements_add_unit_test(serialize_test tests/src/serialize_test.cpp
                       LINK_LIBRARIES GridContainer TYPE Boost)
