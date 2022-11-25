import glob
import os
import cv2
from tqdm import tqdm
import numpy as np

target_path = os.path.join(os.getcwd(), 'data', 'dataset', 'imagesTr')
dataset_dir = os.path.join(os.getcwd(), 'data', 'dataset')
dataset_folders = list = glob.glob(os.path.join(dataset_dir, 'Set_*_Cam_*'))

i=0

for folder in dataset_folders:
    green_imgs_list = glob.glob(os.path.join(folder, '*.1.jpg'))
    red_imgs_list = glob.glob(os.path.join(folder, '*.2.jpg'))
    optical_imgs_list = glob.glob(os.path.join(folder, '*.0.jpg'))

    for img_path in tqdm(optical_imgs_list):
        old_name = os.path.basename(img_path)
        name = str(i) + '.' + str(old_name.split('.')[1]) + '.' + str(old_name.split('.')[2])
        optical_img = cv2.imread(img_path)
        red_img = cv2.imread(img_path.replace('.0', '.2'))
        green_img = cv2.imread(img_path.replace('.0', '.1'))

        out_frame = np.zeros((green_img.shape[0],green_img.shape[1],3),dtype = np.uint8)
        out_frame[:,:,1] = green_img[:,:,1]
        out_frame[:,:,2] = red_img[:,:,2]

        #visualisation
        # cv2.namedWindow('optical_img', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('optical_img', 463, 346)
        # cv2.namedWindow('out_frame', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('out_frame', 463, 346)
        # cv2.imshow('out_frame', out_frame)
        # cv2.imshow('optical_img', optical_img)
        # cv2.waitKey(0)

        #saving new imgs
        input_img_path = os.path.join(target_path, name)
        cv2.imwrite(input_img_path, optical_img)

        label_img_path = os.path.join(target_path.replace('imagesTr', 'labelsTr'), name.replace('.0', '.3'))
        cv2.imwrite(label_img_path, out_frame)

        i+=1
