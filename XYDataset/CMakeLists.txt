elements_subdir(XYDataset)
elements_depends_on_subdirs(Table)
elements_depends_on_subdirs(ElementsKernel)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)
find_package(CCfits)

#===== Libraries ===============================================================
elements_add_library(XYDataset src/lib/*.cpp
                     LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost Table CCfits ElementsKernel
                     INCLUDE_DIRS Boost Table CCfits
                     PUBLIC_HEADERS XYDataset)


#===== Boost tests =============================================================
elements_add_unit_test(XYDataset_test tests/src/XYDataset_test.cpp
                     LINK_LIBRARIES XYDataset
                     TYPE Boost)

if(ELEMENTS_HIDE_WARNINGS)
  if(UNIX)
    set_property(SOURCE tests/src/XYDataset_test.cpp
                 PROPERTY COMPILE_FLAGS -Wno-float-equal)
  endif()
endif()
elements_add_unit_test(FileSystemProvider_test tests/src/FileSystemProvider_test.cpp
                     LINK_LIBRARIES XYDataset
                     TYPE Boost)
elements_add_unit_test(AsciiParser_test tests/src/AsciiParser_test.cpp
                     LINK_LIBRARIES XYDataset
                     TYPE Boost)
elements_add_unit_test(QualifiedName_test tests/src/QualifiedName_test.cpp
                     LINK_LIBRARIES XYDataset
                     TYPE Boost)
elements_add_unit_test(FitsParser_test tests/src/FitsParser_test.cpp
                     LINK_LIBRARIES XYDataset
                     TYPE Boost)
elements_add_unit_test(CachedProvider tests/src/CachedProvider_test.cpp
                     EXECUTABLE XYDataset_CachedProvider_test
                     LINK_LIBRARIES XYDataset
                     TYPE Boost)
