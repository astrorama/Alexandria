# Special toolchain file that inherits the same heptools version as the
# used projects.
find_file(inherit_astrotools_module InheritAstroTools.cmake)
# this check is needed because the toolchain seem to be called a second time
# without the proper cache
if(inherit_astrotools_module)
  include(${inherit_astrotools_module})
  inherit_astrotools()
endif()
