elements_subdir(ChMatrix 0.1)

elements_depends_on_subdirs(ElementsKernel)
find_package(Boost REQUIRED COMPONENTS serialization)

#===== Boost tests =============================================================

elements_add_unit_test(AxisInfo_test tests/src/AxisInfo_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES TYPE Boost)

elements_add_unit_test(AxisInfo_serialization_test tests/src/serialization/AxisInfo_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES Boost TYPE Boost)

elements_add_unit_test(tuple_serialization_test tests/src/serialization/tuple_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES Boost TYPE Boost)
