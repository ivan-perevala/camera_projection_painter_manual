Export Cameras
##############

Exports camera data to files of third-party software.

The addon stores camera data with double precision, according to the IEEE-754 standard, so files imported from third-party software can be exported back without loss of precision.

For export, you need to choose the path and name of the file, and for some formats (for example, Reality Capture Metadata (XMP), which writes each camera in a separate file) - a directory. It is also necessary to choose the file format and the name source.

Files supported by the current version of the addon:

* **Reality Capture**

  * Metadata (XMP)
  * Internal/External camera parameters
  * Comma-separated Name, X, Y, Z
  * Comma-separated Name, X, Y, Z, Heading, Pitch, Roll
  * Comma-separated Name, X, Y, Z, Omega, Phi, Kappa

* **Agisoft Metashape**

  * Omega Phi Kappa (.txt)

Regarding file format selection, you can simply select an existing file to overwrite and the export format will be selected automatically, according to the existing file format. It should be noted here that if an existing file is selected, then to export to another file format, it is necessary to remove the selection from the file and clear the file name field, only then it will be possible to choose another format.

As for choosing the source of the camera names in the exported file, it depends on the dataset of the current scene. Most of the time, the standard settings are enough (use the name of the camera object), but in certain non-standard situations, you need to specify it yourself.

Number of Cameras
=================

Write number of cameras into a file for Reality Capture CSV-like file formats

Calibration Groups
==================

Select to export the information on the created calibration groups for Reality Capture (XMP)

Include Editor Options
======================

Export editor states, e.g. enabled/disabled flags for texturing, meshing, and similar for Reality Capture (XMP)

Export Mode
===========

Depending on how much you trust your registration, you can select the following options or you can also choose not to export camera poses for Reality Capture (XMP)

Do Not Export
 Do not export camera poses

Draft
 This will treat poses as an imperfect draft to be optimized in the future. The draft mode functions also as a flight log

Exact
 If you trust the alignment absolutely. By choosing this option, you are saying to the application that poses are precise, but the global position, orientation, and scale is not known

Locked
 This is the same as the exact option with the difference that the camera position and calibration will not be changed, when locked

Calibration Group
=================

By defining a group for Reality Capture (XMP) we state that all images in this group have the same calibration properties, e.g. the same focal length, the same principal point. Use "-1" if you do not want to group the parameters

Distortion Group
================

By defining a group for Reality Capture (XMP) we state that all images in this group have the same lens properties, e.g. the same lens distortion coefficients. Use "-1" if you do not want to group the parameters

In Texturing
============

Whether to use an image to create an object texture for Reality Capture (XMP)

In Meshing
==========

Whether to use an image to create the object mesh data for Reality Capture (XMP)

Forward
=======

Axis forward

X Forward
 Use the global X axis as the forward direction

Y Forward
 Use the global Y axis as the forward direction

Z Forward
 Use the global Z axis as the forward direction

Negative X Forward
 Use the negative global X axis as the forward direction

Negative Y Forward
 Use the negative global Y axis as the forward direction

Negative Z Forward
 Use the negative global Z axis as the forward direction

Up
==

Axis up

X Up
 Use the global X axis as the up direction

Y Up
 Use the global Y axis as the up direction

Z Up
 Use the global Z axis as the up direction

Negative X Up
 Use the negative global X axis as the up direction

Negative Y Up
 Use the negative global Y axis as the up direction

Negative Z Up
 Use the negative global Z axis as the up direction

