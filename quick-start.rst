Quick Start
###########

Standard and recommended methods of working with the add-on are described here. Of course, no one forces you to use them - here you can experiment at your own discretion.

.. tab-set::

    .. tab-item:: Reality Capture
        
        * **Export Object Wire**

        In order to simplify the task when importing the model to Blender, we export the model as a Wavefront (.obj) file. In newer versions of Blender (3.2+), this type of file is imported quickly and contains only the data needed to work with the addon. The important options here are:

            * ``Coordinate System`` - ``Same as XMP``
            * ``Transformation Preset`` - ``Blender``

        These will be used :ref:`as presets for the <Software>` import from Reality Capture when :doc:`importing the scene <./ops/import-scene>`.

        .. image:: ./images/qs-rc-export-obj.jpg
            :align: center

        * **Export Camera Data**

        .. image:: ./images/qs-rc-export-metadata-xmp.jpg
            :align: center

        * **Setup Context**

        Next, you need to import this data. Start Blender and run :doc:`setup context <./ops/setup-context>`. There is nothing in the standard scene that will help us in our work, so this data can be deleted. This should also be done if, for example, you have finished adjusting one scene and want to move on to the next dataset. Therefore, the first question will be whether to clear the existing data:

        .. image:: ./images/qs-data-cleanup.jpg
            :align: center
    

        Next, select the file containing the object wire and import it.

        .. image:: ./images/qs-rc-import-scene.jpg
            :align: center


        Then you need to choose the texture that we will adjust.

        .. image:: ./images/qs-rc-ensure-canvas.jpg
            :align: center


        Next, we import camera data. This will allow you to use lens distortion without exporting distortion corrected images.

        .. image:: ./images/qs-rc-import-cameras.jpg
            :align: center


        The next step will be linking the images to the camera objects.

        .. image:: ./images/qs-rc-bind-images.jpg
            :align: center

        And after that you can start adjusting the texture.

        .. image:: ./images/qs-rc-complete.jpg
            :align: center

    .. tab-item:: Agisoft Metashape
        
        * **Export Object Wire**
        
        Export the reconstructed scene. It is recommended to use the Wavefront (.obj) format for this, as Blender 3.2+ will import this file type the fastest and it can store all the necessary mesh data and not contain extraneous data such as camera position information that needs to be imported separately.
    
        .. image:: ./images/qs-ms-export-obj.jpg
            :align: center

        * **Export Camera Data**

        Next, we export the camera data, for this we will use the Agisoft XML format.

        .. image:: ./images/qs-ms-export-agisoft-xml.jpg
            :align: center

        * **Setup Context**
        
        Next, you need to import this data. Start Blender and run :doc:`setup context <./ops/setup-context>`. There is nothing in the standard scene that will help us in our work, so this data can be deleted. This should also be done if, for example, you have finished adjusting one scene and want to move on to the next dataset. Therefore, the first question will be whether to clear the existing data:

        .. image:: ./images/qs-data-cleanup.jpg
            :align: center

        Select the previously exported scene file and the presets for Agisoft Metashape.

        .. image:: ./images/qs-ms-import-scene.jpg
            :align: center

        Next, it is necessary to choose the texture that we will adjust.
            
        .. image:: ./images/qs-ms-ensure-canvas.jpg
            :align: center

        Then import camera data from an XML file.
        
        .. image:: ./images/qs-ms-import-cameras.jpg
            :align: center
    
        Finally, you need to bind the image to the cameras. To do this, select the directory in which the images are located.

        .. image:: ./images/qs-ms-bind-images.jpg
            :align: center

        This completes the context setting, you can adjust the texture.

        .. image:: ./images/qs-ms-complete.jpg
            :align: center
