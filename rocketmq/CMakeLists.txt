cmake_minimum_required(VERSION 2.8.12)
project(cmake_wrapper)

message(STATUS "Conan CMake Wrapper")
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include(CMakeListsOriginal.txt)
