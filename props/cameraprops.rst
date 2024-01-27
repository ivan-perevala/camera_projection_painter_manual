Camera
######

Image
=====

Camera binded image. It will be used as a paint brush. Also, its size affects the distortion parameters in the pixel coordinate system (in which way - described in more detail for the corresponding parameters), and therefore - also the possibility of exporting to certain file formats

Millimeters Focal Length
========================

Focal length of the camera in millimeters. The value is stored with double precision

Pixels Focal Length
===================

The focal length of the camera in pixels. Calculated by the formula:

`Pixels Focal Lens = F * P / S`

where `F` is the focal length in millimeters, `P` is the larger side of the image, `S` is the size of the camera sensor in millimeters

Sensor
======

The size of the camera sensor in millimeters, taking into account the larger side of the attached image. This means that if the sensor fit option is set to horizontal - the width of the sensor will be used for calculations, for vertical fit type - height accordingly. These values can be set manually. But for when working with photogrammetric scenes, it is necessary to use the automatic type of sensor adjustment. In this case, if the image has a landscape orientation (or the sides are equal), the width of the sensor will be used, and in the case of a portrait - the height of the sensor. As you can see, there are opportunities for using non-standard workflows, but the main mode of operation is the automatic sensor type. Also note the camera-bound image, this is important for importing and exporting to some file formats. The value is stored with double precision

Millimeters Skew
================

The horizontal skew of the image in millimeters relative to its center, excluding principal deviation. The value is stored with double precision

Pixels Skew
===========

Horizontal skew of the image in pixels relative to its center without taking into account deviation. Calculated by the formula:

`Pixels Skew = S * P`

where `S` is the skew value in millimeters, `P` is the size of the larger side of the image

Aspect Ratio
============

Image aspect ratio correction factor. It means the ratio of the height of the image to its width - that is, values ​​greater than 1.0 will stretch it vertically, smaller values ​​will compress it. The value is stored with double precision

Millimeters Principal X
=======================

The deviation from the center of the image in millimeters along the X axis. Calculated by the formula:

`Millimeters Principal X = Px * S`

where `Px' is the deviation factor, `S' is the size of the camera sensor

Millimeters Principal Y
=======================

The deviation from the center of the image in millimeters along the Y axis. Calculated by the formula:

`Millimeters Principal Y = Py * S`

where `Py' is the deviation factor, `S' is the size of the camera sensor

Pixels Principal
================

The deviation from the center of the image in pixels. Calculated by the formula:

`Pixels Principal = Pxy * L + (Sxy / 2)`

where `Pxy` is the deviation factor, `L` is the larger side of the image, `Sxy` is the image size

Distortion Model
================

Mathematical model of lens distortion. Note that distortion coefficients may be inconsistent between different distortion models

None
 No distortion, only correction

Division
 The division model with two radial distortion coefficients. This is the simplest mathematical model of linear division of image coordinates, which can be used if the distortion is small, for example, for scenes where the shooting took place close to the object

Polynomial
 A polynomial model with four radial and two tangential distortion coefficients. It uses polynomial functions instead of simple linear division, so it is a more accurate and flexible model that can be used for complex scenes with significant lens distortions

Brown-Conrady
 Brown-Conrady polynomial model with four with four radial and two tangential distortion coefficients. It is the most accurate and flexible model that can be used for complex scenes with significant lens distortions. In general, it is used when a simple linear division model is no longer sufficient

K1
==

Represents linear radial distortion. It corrects or introduces distortion that increases linearly with radial distance. The value is stored with double precision

K2
==

Represents cubic radial distortion. It corrects or introduces distortion that increases with the cube of the radial distance. The value is stored with double precision

K3
==

Represents quintic (fifth-order) radial distortion. It corrects or introduces distortion that increases with the fifth power of the radial distance. The value is stored with double precision

K4
==

Represents seventh-order radial distortion. It corrects or introduces distortion that increases with the seventh power of the radial distance. The value is stored with double precision

P1
==

Represents linear tangential distortion. Corrects or introduces distortion that increases linearly with the distance from the image center. The value is stored with double precision

P2
==

Represents quadratic tangential distortion. Corrects or introduces distortion that increases with the square of the distance from the image center. The value is stored with double precision

Bind History
============

Images that were previously binded to this camera. The option is used if, for example, it is necessary to draw some area from another image, and then return to the previous one. Of course, this is not a standard workflow, but it is used sometimes

Image
-----

The image that was previously attached to this camera


Reality Capture Properties
==========================

The properties that were imported from Reality Capture.They will be used for export


