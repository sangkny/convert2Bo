# -*- coding: utf-8 -*-
# This file converts xml(voc) to yolo txt file ( classid, relative_center_x, relative_center_y, relative_width, relative_height)
# original version of convert2yolo.py is for voc to yolo (x,y, width, height, classid)

from convert2Yolov3 import convert2Yolov3
import sys


if __name__ == '__main__':

    print(sys.argv)

    class_path = "itms.names"
    image_dir = "example/voc/JPEG/"
    anno_dir = "example/voc/label/"
    label_dir = "example/voc/results/"
    image_copy_path = "example/voc/images/"
    image_copy = True
    if len(sys.argv) < 6:
        print("need more parameter : [class file path] [jpeg file path] [annotation file path] [result file path][images copy path][image copy flag")
        print("it will process default parameter")
        print("default execute command is 'python3 voc.py test.names example/voc/JPEG/ example/voc/label/ example/voc/results/ example/voc/images/ true'")

    else:
        if sys.argv[1] is not None:
            class_path = sys.argv[1]
        if sys.argv[2] is not None:
            image_dir = sys.argv[2]
        if sys.argv[3] is not None:
            anno_dir = sys.argv[3]
        if sys.argv[4] is not None:
            label_dir = sys.argv[4]
        if sys.argv[5] is not None:
            image_copy = sys.argv[5]

    print("class_path : {}".format(class_path))
    print("image_dir : {}".format(image_dir))
    print("anno_dir : {}".format(anno_dir))
    print("label_dir : {}".format(label_dir))
    print("image_copy path : {}".format(image_copy_path))
    print("image_copy flag: {}".format(image_copy))

    toYolo = convert2Yolov3(classes_path = class_path, image_dir=image_dir, anno_dir=anno_dir, label_dir=label_dir,
                            images_copy_path = image_copy_path, image_copy_flag=image_copy)
    toYolo.parsingVocXML()