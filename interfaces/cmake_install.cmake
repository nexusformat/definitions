# Install script for directory: /afs/psi.ch/user/k/koennecke/src/workspace/interfaces/interfaces

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "0")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFarea_detector.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFarea_detector_scanned.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFarea_detector_tof.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFBeamline_component.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFcount_time.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFcount_time_scanned.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFgasdetector.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFgeneric_detector.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFgeneric_detector_scanned.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFGeneric_detector_tof.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFlinear_detector.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFlinear_detector_scanned.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFlinear_detector_tof.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFmetadata.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFmonochromator.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFphoton_counter.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFsinglecrystal.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFsingle_detector.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIFsingle_detector_scanned.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/interfaces" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/interfaces/NXIF_single_detector_tof.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

