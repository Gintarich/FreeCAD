
include_directories(
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${XercesC_INCLUDE_DIRS}
)

set(gbStructure_LIBS
    FreeCADApp
)

SET(gbStructure_SRCS
    AppgbStructure.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(gbStructure SHARED ${gbStructure_SRCS})
target_link_libraries(gbStructure ${gbStructure_LIBS})


SET_BIN_DIR(gbStructure gbStructure /Mod/gbStructure)
SET_PYTHON_PREFIX_SUFFIX(gbStructure)

install(TARGETS gbStructure DESTINATION ${CMAKE_INSTALL_LIBDIR})
