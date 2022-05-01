
include_directories(
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
    ${Boost_INCLUDE_DIRS}
    ${COIN3D_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${XercesC_INCLUDE_DIRS}
)

set(gbStructureGui_LIBS
    gbStructure
    FreeCADGui
)

if (BUILD_QT5)
    qt5_add_resources(gbStructure_QRC_SRCS Resources/gbStructure.qrc)
else()
    qt4_add_resources(gbStructure_QRC_SRCS Resources/gbStructure.qrc)
endif()

SET(gbStructureGui_SRCS
    ${gbStructure_QRC_SRCS}
    AppgbStructureGui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

add_library(gbStructureGui SHARED ${gbStructureGui_SRCS})
target_link_libraries(gbStructureGui ${gbStructureGui_LIBS})

SET_BIN_DIR(gbStructureGui gbStructureGui /Mod/gbStructure)
SET_PYTHON_PREFIX_SUFFIX(gbStructureGui)
    
install(TARGETS gbStructureGui DESTINATION ${CMAKE_INSTALL_LIBDIR})
