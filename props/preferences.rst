Preferences
###########

Use Mesh Preview
================

Use mesh preview for brush and inspection. This option can be useful to significantly reduce the use of video memory, for example, if the purpose of using the addon is only to import and export cameras. The current implementation of Blender forces the display to save the object's data and re-render it, just to show the brush preview. Of course, this is convenient, but it significantly increases the load on the system. Therefore, if it is not critical for you to see a preview of the brush you are drawing with, you can disable the preview

Use Previews
============

Use image previews. Whether to generate and display image previews in the viewport. This does not significantly increase the amount of video memory, but it can cause small friezes in the viewport. The generation system works according to the principle of displaying the necessary previews. That is, all camera frames in the observer's field of view will be added to the render queue. Of course, the faster you read data from the disk, the faster it will be generated. The camera on which the cursor is hovered on is always added to render queue first

Dithering Strength
==================

8x8 Bayer dithering strength. The resolution of the previews is rather small - 128x128 pixels. Of course, this add-on performs smoothing of the generated previews, but for a clearer understanding of what is shown, you can use dithering and mix it with the original preview

Smooth Previews
===============

Use fast approximated anti-aliasing for preview images. Blender generates previews as Nearest, so readability is lost. This option does not add more data from the original image but performs smoothing and thus makes it more readable

Cameras Transparency
====================

Transparency of cameras in the viewport.

Tooltip Preview Size
====================

The size of the preview image in the tooltip. Does not affect the quality of the displayed preview, only its size

Normal
 Standard size, 128x128 pixels

Large
 Stretched to double size

Tooltip Position
================

The location of the pop-up tooltip with information about the camera data on which the cursor is hovered

Static
 Appears near the brush and remains in the place where it appeared

Floating
 Appears and follows the brush

Fixed
 Appears only at the bottom of the screen, in the middle

Software
========

Preset for software for which the operation will be performed

Reality Capture
 Use presets for Reality Capture

Select Framebuffer Scale
========================

Select framebuffer scale percentage, available in "Developer Extras" section. This exists mostly for optimization purposes, since the smaller size of framebuffer significantly reduces the use of both memory and CPU. The point is that the data from framebuffer will be read not only in one particular place, but also to determine which cameras in the field of view of the observer and require rendering of preview. Changing this option requires restarting the active main operator

Log Level
=========

The level of the log that will be output to the console. For log to file, this level value will not change

Debug
 Debug messages (low priority)

Info
 Informational messages

Warning
 Warning messages (medium priority)

Error
 Error messages (high priority)

Critical
 Critical error messages

