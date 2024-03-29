elements_subdir(Table)

elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(AlexandriaKernel)
elements_depends_on_subdirs(NdArray)

find_package(CCfits)
find_package(GMock)

#===== Libraries ===============================================================
elements_add_library(Table src/lib/*.cpp
                     LINK_LIBRARIES ElementsKernel CCfits AlexandriaKernel
                     INCLUDE_DIRS ElementsKernel CCfits
                     PUBLIC_HEADERS Table)

#===== Boost tests =============================================================

if(GMOCK_FOUND)
# inhibits the -Wsuggest-override that is not supported by gmock (yet)
if(CXX_HAS_SUGGEST_OVERRIDE)
  set_property(SOURCE tests/src/TableWriter_test.cpp
               PROPERTY COMPILE_FLAGS -Wno-suggest-override)
endif()
elements_add_unit_test(TableWriter_test tests/src/TableWriter_test.cpp
                     LINK_LIBRARIES Table GMock
                     INCLUDE_DIRS GMock
                     TYPE Boost)
endif(GMOCK_FOUND)
elements_add_unit_test(ColumnInfo_test tests/src/ColumnInfo_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(Row_test tests/src/Row_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(Table_test tests/src/Table_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(AsciiReaderHelper_test tests/src/AsciiReaderHelper_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(AsciiWriterHelper_test tests/src/AsciiWriterHelper_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(FitsReaderHelper_test tests/src/FitsReaderHelper_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(FitsWriterHelper_test tests/src/FitsWriterHelper_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(CastVisitor_test tests/src/CastVisitor_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(ColumnDescription_test tests/src/ColumnDescription_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(AsciiWriter_test tests/src/AsciiWriter_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(FitsWriter_test tests/src/FitsWriter_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(AsciiReader_test tests/src/AsciiReader_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
elements_add_unit_test(FitsReader_test tests/src/FitsReader_test.cpp
                     LINK_LIBRARIES Table
                     TYPE Boost)
