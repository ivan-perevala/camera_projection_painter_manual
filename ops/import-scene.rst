Import Scene
############

Stage :doc:`setting up the context <setup-context>` as well as an independent operator. In fact, it's just a wrapper for standard import operators with presets.

If the presets are not suitable for any reason, you can always import the scene manually and skip this stage when setting up the context - just do not select any file.

So, in order to use this operator, you need to select a file to import and select the default settings for :ref:`third-party <Software>` files. This setting is saved as addon preference so you can do it once.

Next, the file type will be automatically determined using its extension. Files supported by the current version of the addon:

* ``Wavefront (.obj)``, ``Collada (.dae)`` - used built-in Blender importers.
* ``Autodesk (*.fbx)`` - the standard FBX file import addon will be used, so it should be enabled.

If these requirements are not met, the files will be hidden in the file manager and refused import. However, this is more information for users who use their own Blender builds.
