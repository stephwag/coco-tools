import mrcnn

class MyDataset(mrcnn.utils.Dataset):
    def __init__(self, class_map=None):
        num_images = 3
        self._image_ids = [i for i in range(1, num_images + 1)]
        mrcnn.utils.Dataset.__init__(self, class_map=class_map)
