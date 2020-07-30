elements_subdir(NdArray)

find_package(Boost REQUIRED COMPONENTS iostreams)

#===== Libraries ===============================================================
elements_add_library(NdArray
        LINKER_LANGUAGE CXX
        LINK_LIBRARIES AlexandriaKernel Boost
        PUBLIC_HEADERS NdArray)

#===== Boost tests =============================================================
elements_add_unit_test(NdArray_test tests/src/NdArray_test.cpp
        LINK_LIBRARIES NdArray TYPE Boost)

elements_add_unit_test(Npy_test tests/src/Npy_test.cpp
        LINK_LIBRARIES NdArray TYPE Boost)

elements_add_unit_test(NpyMmap_test tests/src/NpyMmap_test.cpp
        LINK_LIBRARIES NdArray TYPE Boost)

