cmake_minimum_required(VERSION 4.2)
project(esphome-components)

# Diese Datei dient nur der Nutzung im CLion


set(ESPHOME $ENV{HOME}/development/esphome)

include_directories(${ESPHOME})


add_subdirectory(components)