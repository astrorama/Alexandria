elements_subdir(NdArray)

#===== Libraries ===============================================================
elements_add_library(NdArray src/lib/*.cpp
        PUBLIC_HEADERS NdArray)


#===== Boost tests =============================================================
elements_add_unit_test(NdArray_test tests/src/NdArray_test.cpp
        LINK_LIBRARIES NdArray TYPE Boost)
