elements_subdir(MathUtils 1.0)

elements_depends_on_subdirs(XYDataset)

#===== Libraries ===============================================================

elements_add_library(MathUtils src/lib/function/*.cpp src/lib/interpolation/*.cpp
                     LINK_LIBRARIES XYDataset
                     PUBLIC_HEADERS MathUtils XYDataset)

#===== Boost tests =============================================================

elements_add_unit_test(function_all_tests tests/src/function/*_test.cpp
                       LINK_LIBRARIES MathUtils XYDataset TYPE Boost)

elements_add_unit_test(interpolation_all_tests tests/src/interpolation/*_test.cpp
                       LINK_LIBRARIES MathUtils XYDataset TYPE Boost)