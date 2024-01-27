Answers
#######

Here you can find answers to questions previously asked by users. We respect the privacy of the author and the source of the question is not indicated, but the questions themselves are verbatim, with minor editing (for example, the greeting was removed).

If you yourself have questions, you can ask them through the `tracker on GitHub <https://github.com/BlenderHQ/camera_projection_painter/issues/new/choose>`_ (this is the most official way) or through social networks.

------------------------------------------------------------------------------------------------------------------------

**In the github description you say "you can adjust the texture and camera data", what do you mean by that? I'm interested in what this addon is, but it's hard to piece the meaning together from the descriptions**

It allows you to paint over the texture of the reconstructed object with a clone brush from the original photo.

**Does it support multicamera rigs with images of different w x h sizes ?**

Yes, it supports.  Here, of course, it should be noted that the sensor of imported cameras matters, and this will affect whether the distortion of the lens will be correctly calculated, because Blender strictly separates the height and width of the sensor, but the import operators automatically set its value. But yes, working with different image resolutions is one of the main purposes of the add-on. For example, if a camera with the largest resolution is installed vertically in the facial rig and is aimed directly at the face, it makes sense to add details from it

**Can you input intrinsics via file?**

Yes, I can and you probably can too 😉 
I've also written some documentation for the add-on, so I think that might help.

But in general yes, of course you can import/export internal/external parameters of cameras - this significantly reduces the size of the data needed to work with the scan texture.
