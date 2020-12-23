elements_subdir(NdArray)

elements_depends_on_subdirs(AlexandriaKernel)
elements_depends_on_subdirs(ElementsKernel)

find_package(Boost REQUIRED COMPONENTS iostreams)

#===== Libraries ===============================================================
elements_add_library(NdArray
        LINKER_LANGUAGE CXX
        LINK_LIBRARIES AlexandriaKernel Boost
        PUBLIC_HEADERS NdArray)

#===== Boost tests =============================================================
elements_add_unit_test(NdArray_test tests/src/NdArray_test.cpp
        LINK_LIBRARIES NdArray TYPE Boost)

if (Boost_VERSION GREATER "105800")
elements_add_unit_test(Npy_test tests/src/Npy_test.cpp
        LINK_LIBRARIES NdArray TYPE Boost)

elements_add_unit_test(NpyMmap_test tests/src/NpyMmap_test.cpp
        LINK_LIBRARIES NdArray TYPE Boost)
else ()
  message(WARNING "Boost Endian added after Boost 1.58 (Found ${Boost_VERSION}). Disabling NdArray I/O tests")
endif ()
