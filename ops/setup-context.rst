Setup Context
#############

Sequential setting of the context for work - step by step the scene and necessary data will be imported and the parameters of the tools will be configured.

Execution is divided into stages, each of which is a separate call of automation operators. Each of the execution stages can be skipped if it is not needed in the current situation and go to the next one, or cancel its execution and thus complete the context setting at the current stage.

The sequence of execution stages is as follows:

#. :doc:`data-cleanup`
#. :doc:`import-scene`
#. :doc:`ensure-canvas`

   * :doc:`quick-select-canvas`
   * :doc:`create-new-canvas`
#. :doc:`import-cameras`
#. :doc:`bind-camera-images`
#. :doc:`ensure-tool-settings`
