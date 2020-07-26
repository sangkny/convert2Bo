# -*- coding: utf-8 -*-
"""
## itms_yolo.py collects all the images into a folder and generates yolo txt files for training.
## This file converts xml(voc) to yolo txt file ( classid, relative_center_x, relative_center_y, relative_width, relative_height)
## original version of convert2yolo.py is for voc to yolo (x,y, width, height, classid)
## arg example
## --base_dir=E:/temp/ --class_path=itms.names --image_dir=4581_20190902220000/ --anno_dir=4581_20190902220000/ --label_dir=4581_20190902220000/results/ --image_copy_path=images/ --image_copy_flag=1
If the given base_dir has some folder, then the following dir should be relative. Otherwise, absolute path

D:/sangkny/pyTest/MLDL/codes/convert2Bo/
itms.names
D:/sangkny/pyTest/MLDL/codes/convert2Bo/example/voc/JPEG/
D:/sangkny/pyTest/MLDL/codes/convert2Bo/example/voc/label/
D:/sangkny/pyTest/MLDL/codes/convert2Bo/example/voc/results/
D:/sangkny/pyTest/MLDL/codes/convert2Bo/images/ True

"""
from convert2Yolov3 import convert2Yolov3
import sys
import argparse

if __name__ == '__main__':
    print(sys.argv)
    '''
    base_dir = ''                       # if os.isdir(base_dir) then getcwd is not neccessary
    class_path = "itms.names"    
    image_dir = "example/voc/JPEG/"     # 
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
            image_copy_path = sys.argv[5]
        if sys.argv[6] is not None:
            image_copy = sys.argv[6]

    print("class_path : {}".format(class_path))
    print("image_dir : {}".format(image_dir))
    print("anno_dir : {}".format(anno_dir))
    print("label_dir : {}".format(label_dir))
    print("image_copy path : {}".format(image_copy_path))
    print("image_copy flag: {}".format(image_copy))
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--base_dir', type=str, default='d:/sangkny/pyTest/MLDL/convert2Bo/', help='base dir')#, required=True) # base
    parser.add_argument('--class_path', type=str, default='itms.names', help= 'class path and name')#, required= True)  # class path
    parser.add_argument('--image_dir', type=str, default='example/voc/JPEG/', help='image data')#, required= True) # image folder
    parser.add_argument('--anno_dir', type=str, default='example/voc/label/', help='annotation foloder: xml files')#, required=True) # label data with xml
    parser.add_argument('--label_dir', type=str, default='example/voc/results/', help='converted label path')#, required=True)
    parser.add_argument('--image_copy_path', type=str, default='example/voc/images/')#, help='image path to move from origin data')
    parser.add_argument('--image_copy_flag', type = int, default= 1, help='copy images to a folder?')#, required= True)
    parser.add_argument('--image_ext', type=str, default='jpg', help='image extension')
    opt = parser.parse_args()

    # temp settings
    ''' home 
    opt.base_dir = ""
    opt.class_path = "D:/sangkny/pyTest/MLDL/codes/convert2Bo/itms.names"
    opt.image_dir = "C:/Users/SangkeunLee/Downloads/113511-122311/"
    opt.anno_dir = "C:/Users/SangkeunLee/Downloads/113511-122311/"
    opt.label_dir = "D:/sangkny/pyTest/MLDL/codes/convert2Bo/example/itms/results/"
    opt.image_copy_path = "D:/sangkny/pyTest/MLDL/codes/convert2Bo/example/itms/images/"
    opt.image_copy_flag = True
    '''
    # ----   office ---------
    # ---- version 20200205
    # opt.base_dir = ""
    # opt.class_path = "E:/Topes_data_related/traffic_related/20190903_국도10개소수집_10분_result(2)/itms.names"
    # opt.image_dir = "E:/Topes_data_related/traffic_related/130148-141049/"
    # opt.anno_dir = "E:/Topes_data_related/traffic_related/130148-141049/"
    # opt.label_dir = "E:/Topes_data_related/traffic_related/20190903_국도10개소수집_10분_result(2)/results/"
    # opt.image_copy_path = "E:/Topes_data_related/traffic_related/20190903_국도10개소수집_10분_result(2)/images/"
    # # ---- version 20200426 with 주간 보행 라벨링 이미지 결과
    # opt.base_dir = ""
    # opt.class_path = "E:/Topes_data_related/traffic_related/20190903_국도10개소수집_10분_result(2)/itms.names"
    # opt.image_dir = "E:/Topes_data_related/주간 보행 라벨링 이미지 결과/130148-141049/"
    # opt.anno_dir = "E:/Topes_data_related/주간 보행 라벨링 이미지 결과/130148-141049/"
    # opt.label_dir = "E:/Topes_data_related/traffic_related/20200426_20200421_data/results/"
    # opt.image_copy_path = "E:/Topes_data_related/traffic_related/20200426_20200421_data/images/"

    # ---- version 20200726 with 11M
    opt.base_dir = ""
    opt.class_path = "E:/Topes_data_related/traffic_related/20190903_국도10개소수집_10분_result(2)/itms.names"
    opt.image_dir = "E:/Topes_data_related/labelling/11M/11M-20200604-105755-주간 단독 갓길 정지 보행/"
    opt.anno_dir = "E:/Topes_data_related/labelling/11M/11M-20200604-105755-주간 단독 갓길 정지 보행/"
    opt.label_dir = "E:/Topes_data_related/labelling/11M/results/"
    opt.image_copy_path = "E:/Topes_data_related/labelling/11M/images/"
    opt.image_ext = "bmp"

    opt.image_copy_flag = True
    print(opt)


    toYolo = convert2Yolov3(base_dir= opt.base_dir, classes_path = opt.class_path, image_dir=opt.image_dir, anno_dir=opt.anno_dir, label_dir=opt.label_dir,
                            images_copy_path=opt.image_copy_path, image_copy_flag=opt.image_copy_flag, image_ext= opt.image_ext)
    toYolo.parsingVocXML()