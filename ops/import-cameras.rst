Import Cameras
##############

The :doc:`setup context stage <setup-context>` and an independent operator for importing extrinsic and :doc:`intrinsic <../props/cameraprops>` camera parameters.

For import, you need to select one or more files - their type will be determined automatically. Unlike :doc:`scene importer <import-scene>`, the file type will be determined not only by the extension - as soon as the files are selected, they will be partially read and checked. The check will be based on the key characteristics of various file types of third-party software - it can be the first line with a file description or simply the number of elements in a line (for character-separated formats). For ``XML`` files, certain keys will be found in the tree and so on.

Files supported by the current version of the addon:

* **Reality Capture**

  * Metadata (XMP)
  * Internal/External camera parameters
  * Comma-separated Name, X, Y, Z
  * Comma-separated Name, X, Y, Z, Heading, Pitch, Roll
  * Comma-separated Name, X, Y, Z, Omega, Phi, Kappa

* **Agisoft Metashape**

  * Agisoft XML
  * Omega Phi Kappa (.txt)

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

Comparison Options
==================

Options for comparing names. At least one of the options must be selected for each compared type (object, image, etc.)

Ignore Letter Case
 Ignore character register for matching

Ignore Extensions
 Use name only, no file extension when searching



Use Object Name
 Use camera object name for comparison

Use Camera Name
 Use camera data name for comparison



Use Image Name
 Use image data-block name for comparison

Use Image File Name
 Use image file name for comparison

