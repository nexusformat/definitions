# Install script for directory: /afs/psi.ch/user/k/koennecke/src/workspace/interfaces/base_classes

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
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXaperture.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXpinhole.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXslit.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXattenuator.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXbeam.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXbeam_stop.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXbending_magnet.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXcapillary.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXcharacterization.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXcollection.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXcollimator.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXcrystal.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXdata.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXdetector_group.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXdetector.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXdisk_chopper.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXentry.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXenvironment.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXevent_data.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXfermi_chopper.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXfilter.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXflipper.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXgeometry.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXguide.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXinsertion_device.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXinstrument.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXlog.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXmirror.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXmoderator.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXmonitor.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXmonochromator.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXnote.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXobject.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXorientation.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXparameters.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXpolarizer.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXpositioner.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXprocess.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXroot.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXsample.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXsensor.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXshape.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXsource.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXsubentry.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXtranslation.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXuser.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXvelocity_selector.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/definitions/base_classes" TYPE FILE FILES "/afs/psi.ch/user/k/koennecke/src/workspace/interfaces/dist/base_classes/NXxraylens.nxdl.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "definitions")

