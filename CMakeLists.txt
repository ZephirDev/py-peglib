cmake_minimum_required(VERSION 3.18.4)
project(py_peglib VERSION 1.0.0)

if (DEFINED ENV{PROJECT_NAME})
    set(PROJECT_NAME $ENV{PROJECT_NAME})
endif()

set(CMAKE_CXX_STANDARD 17)

find_package(Boost 1.66.0 COMPONENTS python)
include_directories(/usr/include/python3.9)

include_directories(src)
include_directories(3rd-party)
configure_file(src/py_peglib/info.cpp.in src/py_peglib/info.cpp)

add_library(${PROJECT_NAME} SHARED
    ./src/py_peglib/lib.cpp
    ./src/py_peglib/parser.hpp
    ./src/py_peglib/parser.cpp
    ./src/py_peglib/info.hpp
    ${CMAKE_BINARY_DIR}/src/py_peglib/info.cpp
    ./src/py_peglib/semantic_values.hpp
    ./src/py_peglib/semantic_values.cpp)
target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES})
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "")
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT "py_peglib")