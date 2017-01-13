elements_subdir(GridContainer)

elements_depends_on_subdirs(ElementsKernel)
find_package(Boost REQUIRED COMPONENTS serialization)

# Install the headers. This is necessary because we have only templates and not
# library, so the headers will not be installed automatically
elements_install_headers(GridContainer)

#===== Boost tests =============================================================

elements_add_unit_test(GridAxis_test tests/src/GridAxis_test.cpp
                       LINK_LIBRARIES TYPE Boost)

elements_add_unit_test(GirdAxis_serialization_test tests/src/serialization/GridAxis_test.cpp
                       LINK_LIBRARIES Boost TYPE Boost)

elements_add_unit_test(tuple_serialization_test tests/src/serialization/tuple_test.cpp
                       LINK_LIBRARIES Boost TYPE Boost)

elements_add_unit_test(GridConstructionHelper_test tests/src/GridConstructionHelper_test.cpp
                       LINK_LIBRARIES Boost TYPE Boost)

elements_add_unit_test(GridIndexHelper_test tests/src/GridIndexHelper_test.cpp
                       LINK_LIBRARIES Boost TYPE Boost)

elements_add_unit_test(GridCellManagerTraits_test tests/src/GridCellManagerTraits_test.cpp
                       LINK_LIBRARIES Boost TYPE Boost)

elements_add_unit_test(GridContainer_test tests/src/GridContainer_test.cpp
                       LINK_LIBRARIES Boost ElementsKernel TYPE Boost)

elements_add_unit_test(serialize_test tests/src/serialize_test.cpp
                       LINK_LIBRARIES Boost TYPE Boost)
