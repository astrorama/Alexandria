elements_subdir(ChMath 1.0)

#===== Libraries ===============================================================

elements_add_library(ChMath src/lib/function/*.cpp src/lib/interpolation/*.cpp
                     LINK_LIBRARIES ${CMAKE_DL_LIBS}
                     PUBLIC_HEADERS ChMath)

#===== Boost tests =============================================================

elements_add_unit_test(function_all_tests tests/src/function/*_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChMath TYPE Boost)

elements_add_unit_test(interpolation_all_tests tests/src/interpolation/*_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChMath TYPE Boost)