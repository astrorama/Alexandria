elements_subdir(ChTable 0.1)

elements_depends_on_subdirs(ElementsKernel)

find_package(Boost REQUIRED COMPONENTS regex)
find_package(Cfitsio)
find_package(CCfits)

#===== Libraries ===============================================================

elements_add_library(ChTable src/lib/*.cpp
                     LINK_LIBRARIES ElementsKernel Cfitsio CCfits
                     INCLUDE_DIRS ElementsKernel Cfitsio CCfits
                     PUBLIC_HEADERS ChTable)

#===== Boost tests =============================================================

elements_add_unit_test(ColumnInfo_test tests/src/ColumnInfo_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(Row_test tests/src/Row_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(Table_test tests/src/Table_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(AsciiReader_test tests/src/AsciiReader_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(AsciiReaderHelper_test tests/src/AsciiReaderHelper_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(AsciiWriter_test tests/src/AsciiWriter_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(AsciiWriterHelper_test tests/src/AsciiWriterHelper_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(FitsReader_test tests/src/FitsReader_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)

elements_add_unit_test(FitsReaderHelper_test tests/src/FitsReaderHelper_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChTable TYPE Boost)