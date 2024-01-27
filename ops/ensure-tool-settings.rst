Ensure Tool Settings
####################

The last stage of setting up the work context (:doc:`setup-context`).

First, the availability of the drawing object will be checked. The active object must be a mesh with at least one polygon and an active UV map. If such an object is not available, the first visible scene object that matches these parameters will be selected. At the end of this check, the following options are possible:

* Object found - execution will continue.
* The object is found, but it has no polygons - a message about this will be reported and execution will be interrupted.
* The object is found, it has at least one polygon, but there is no active UV map - execution will continue, but in a limited mode - such a message will be reported. Obviously, editing the canvas in this case will not work, but this mode of operation can be useful if, for example, you only need to change the parameters of certain cameras and export camera data back to third-party software.

If the execution continues, then the tool and the scene will be set up. This section can be used to understand how you can set up a work context manually:

* The work mode will be changed to texture paint.
* The Clone tool will be selected.
* Texture drawing mode will be changed to "Single Image".
* The use of the clone layer will be enabled.

At the end of the execution, the operator will change the lighting type in all viewers of the current program window to flat - this way of displaying the object is best suited for editing textures.

Next, the main workflow of the add-on will be launched - it is important that there is at least one camera in the scene, even if it is inactive. During work, the main operator will independently ensure that an active camera is set - it is from it that the projection will take place.
