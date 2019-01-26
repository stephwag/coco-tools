import sys
from PIL import Image
import numpy as np
import json
import cv2
import imutils
from config import *

def annotation_obj(image_name, image_id, min_threshold=10, max_threshold=255, category_id=1, show_annotation=False, is_crowd=False):
    image = cv2.imread("{}/{}".format(ANNOTATION_DIR, image_name))
    imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,min_threshold,max_threshold,cv2.THRESH_BINARY)
    height, width, channels = image.shape
    image_info = {
        "id" : image_id,
        "file_name" : image_name,
        "height" : height,
        "width" : width
    }

    # Draws the mask, useful for debugging
    if show_annotation:
        cv2.imshow('threshold',thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    count = 1
    results = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        results.append(
            {
                "segmentation": np.array(c).ravel().tolist(),
                "area": w * h,
                "iscrowd": ("crowd" in image_name) or is_crowd,
                "image_id": image_id,
                "bbox": (x, y, w, h),
                "category_id": category_id,
                "id": count
            }
        )
        count += 1
    return (image_info, results)


if __name__=="__main__":
    anno_arr = []
    image_arr = []

    with open("{}/base.json".format(DATASET_DIR), 'r') as f:
        data = json.loads(f.read())

    # Setup dataset.json with image and annotation data
    for i in range(1, 9):
        for category in data["categories"]:
            image_info, anno_info = annotation_obj("{}_{}.jpg".format(i, category["name"]), i, category_id=1, show_annotation=False)
            image_arr.append(image_info)
            anno_arr.append(anno_info)

    with open("{}/dataset.json".format(DATASET_DIR), 'w') as f:
        data["annotations"] = anno_arr
        data["images"] = image_arr
        anno_str = json.dumps(data)
        f.write(anno_str)







