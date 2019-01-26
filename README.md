Tools for training and managing MS COCO datasets (work-in-progress).

### Annotations

You can use `annotate.py` to create annotations from a jpg.

Let's say you have an image of a comic that looks like this, and you want to create annotations of the speech bubbles.

<a href="https://i.imgur.com/XVk1pLJ.jpg"><img src="https://i.imgur.com/XVk1pLJ.jpg" width="15%"></a>

Go to any image editing tool and create a jpg, using any color where the speech bubbles are, and black for the portions we want to leave out.

<a href="https://i.imgur.com/uPckvxn.jpg"><img src="https://i.imgur.com/uPckvxn.jpg" width="15%"></a>

Save the jpg in the annotations directory of your dataset, then run `annotate.py` to get the mask in coco's polygon format for segmentation and save it in a json file.

You can use the `show_annotations` flag to draw the polygons for testing/debugging, which will render an image that looks like this.

<a href="https://i.imgur.com/kkE5eyG.jpg"><img src="https://i.imgur.com/kkE5eyG.png" width="15%"></a>