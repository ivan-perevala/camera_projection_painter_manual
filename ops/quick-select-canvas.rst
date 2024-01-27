Quick Select Canvas
###################

Available during the :doc:`canvas selection stage <ensure-canvas>`.

Often the name of the exported image is similar to the name of the exported object or simply after importing into Blender it is specified as a texture in one of the materials of the imported object.

Therefore, a search is first performed among the materials of the imported object - if the material contains an image texture node, this image will be proposed. Perhaps this is a fairly simple way of searching, but it is the fastest, so it is a priority.

Most often, the first method allows you to find a suitable image, if not - a search for an image with a similar name will be carried out among all those that are currently open. Their number can be quite large, so this method is relatively slow. Here, the name of the object will be used for the search and the possible UDIM pattern of the image will be taken into account.

In any case, the operator is designed to speed up trivial tasks, and you can always choose the image manually. For example, there is an option when almost the desired image was offered, you can confirm a quick selection and then scroll a little through the list of images to the desired one.
