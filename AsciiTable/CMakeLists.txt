elements_subdir(AsciiTable 0.1)

elements_depends_on_subdirs(ElementsKernel)

#===== Libraries ===============================================================

elements_add_library(AsciiTable src/lib/*.cpp
                     LINK_LIBRARIES ElementsKernel
                     INCLUDE_DIRS ElementsKernel
                     PUBLIC_HEADERS AsciiTable)

#===== Boost tests =============================================================

elements_add_unit_test(ColumnInfo_test tests/src/ColumnInfo_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES AsciiTable TYPE Boost)

elements_add_unit_test(Row_test tests/src/Row_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES AsciiTable TYPE Boost)