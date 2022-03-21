elements_subdir(MathUtils)

elements_depends_on_subdirs(GridContainer)
elements_depends_on_subdirs(NdArray)
elements_depends_on_subdirs(XYDataset)
elements_depends_on_subdirs(SourceCatalog)

find_package(GMock)
find_package(Boost REQUIRED)

#===== Libraries ===============================================================

elements_add_library(MathUtils
                      src/lib/function/*.cpp src/lib/helpers/*.cpp src/lib/interpolation/*.cpp
                      src/lib/numericalIntegration/*.cpp src/lib/numericalDifferentiation/*.cpp
                      src/lib/PDF/*.cpp src/lib/regression/*.cpp src/lib/root/*.cpp
                     LINK_LIBRARIES NdArray XYDataset
                     PUBLIC_HEADERS MathUtils)

if(ELEMENTS_HIDE_WARNINGS)
  if(UNIX)
    set_property(SOURCE src/lib/function/multiplication.cpp
                 PROPERTY COMPILE_FLAGS -Wno-float-equal)
    set_property(SOURCE src/lib/function/Piecewise.cpp
                 PROPERTY COMPILE_FLAGS -Wno-float-equal)
    set_property(SOURCE src/lib/interpolation/interpolation.cpp
                 PROPERTY COMPILE_FLAGS -Wno-float-equal)
  endif()
endif()


#===== Boost tests =============================================================
elements_add_unit_test(Distances_test tests/src/distances/Distances_test.cpp
                       LINK_LIBRARIES MathUtils SourceCatalog TYPE Boost)

elements_add_unit_test(Weights_test tests/src/distances/Weights_test.cpp
                       LINK_LIBRARIES MathUtils SourceCatalog TYPE Boost)

elements_add_unit_test(function_all_tests tests/src/function/*_test.cpp
                       LINK_LIBRARIES MathUtils XYDataset TYPE Boost)

elements_add_unit_test(helpers_all_tests tests/src/helpers/*_test.cpp
                       LINK_LIBRARIES MathUtils TYPE Boost)

elements_add_unit_test(interpolation_all_tests tests/src/interpolation/*_test.cpp
                       LINK_LIBRARIES MathUtils XYDataset TYPE Boost)

elements_add_unit_test(central_difference_tests tests/src/numericalDifferentiation/FiniteDifference_test.cpp
                       LINK_LIBRARIES MathUtils TYPE Boost)

elements_add_unit_test(SimpsonsRule_test tests/src/numericalIntegration/SimpsonsRule_test.cpp
                       LINK_LIBRARIES MathUtils TYPE Boost)

elements_add_unit_test(Cumulative_test tests/src/PDF/Cumulative_test.cpp
                     LINK_LIBRARIES MathUtils XYDataset TYPE Boost)

elements_add_unit_test(NdSampler_test tests/src/PDF/NdSampler_test.cpp
                     LINK_LIBRARIES MathUtils SourceCatalog TYPE Boost)

elements_add_unit_test(LinearRegression_test tests/src/regression/LinearRegression_test.cpp
                     LINK_LIBRARIES MathUtils TYPE Boost)

elements_add_unit_test(SecantMethod_test tests/src/root/SecantMethod_test.cpp
                     LINK_LIBRARIES MathUtils TYPE Boost)

if (Boost_VERSION GREATER "106600")
elements_add_unit_test(NdSamplerGrid_test tests/src/PDF/NdSamplerGrid_test.cpp
                     LINK_LIBRARIES MathUtils GridContainer SourceCatalog TYPE Boost)
endif ()

elements_add_unit_test(PdfModeExtraction_test tests/src/PDF/PdfModeExtraction_test.cpp
                     LINK_LIBRARIES MathUtils XYDataset TYPE Boost)

#===== Tests using GMock =======================================================
if(GMOCK_FOUND)
elements_add_unit_test(function_tools_test tests/src/function/function_tools_test_mock.cpp
                         LINK_LIBRARIES GMock MathUtils TYPE Boost
                         INCLUDE_DIRS GMock)

elements_add_unit_test(FunctionAdapter_test tests/src/function/FunctionAdapter_test_mock.cpp
                         LINK_LIBRARIES GMock MathUtils TYPE Boost
                         INCLUDE_DIRS GMock)

elements_add_unit_test(AdaptativeIntegration_test tests/src/numericalIntegration/AdaptativeIntegration_test.cpp
                         LINK_LIBRARIES GMock MathUtils TYPE Boost
                         INCLUDE_DIRS GMock)
endif(GMOCK_FOUND)

