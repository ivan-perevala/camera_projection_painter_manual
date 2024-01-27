Bind Camera Images
##################

Associates images to cameras using names. Can be used both for all cameras present in the scene, and
for the active camera (for the texture drawing mode, this is the scene's active camera, for object mode - the selected camera or
the scene camera is also active if an object of a different type is selected).

The search for images first of all always takes place among already open files, then, if no matches are found, among
files in the selected directory. For this, the operator in the user interface has two launch modes. Import mode
should be used if the required images are not yet open - in this case, it will be possible to choose a directory for
searching for files, and if matches are found - the necessary images will be opened and linked to the cameras. Binding mode
there is no fundamental difference with the import mode, but there is no directory selection here - if the necessary files have not yet been opened
then the directory from which images or camera data were last imported will be used. This mode is useful if, for example,
other images were manually selected and need to be linked again by name.

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

