# coding:utf-8
 
import os
import argparse

def write_image_path_to_file(file_with_path, image_file_path):
    file = open(file_with_path, 'w')
    total_img_name = os.listdir(image_file_path)
    for img_name in total_img_name:
        file.write(image_file_path + img_name)
        file.write("\n")
    file.close()



if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', default='../dataset/FBD-SV-2024/images/', type=str, help='input image path')
    parser.add_argument('--txt_path', default='../', type=str, help='output txt path')
    args = parser.parse_args()

    train_txt_file_with_path = args.txt_path + "train/"
    train_image_path = args.img_path + "train/"
    write_image_path_to_file(train_txt_file_with_path, train_image_path)

    val_txt_file_with_path = args.txt_path + "val/"
    val_image_path = args.img_path + "val/"
    write_image_path_to_file(val_txt_file_with_path, val_image_path)