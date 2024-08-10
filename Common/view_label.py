import os
import xml.etree.ElementTree as ET
import cv2
import argparse


classes=['bird']
def convert_annotation(annotation_file):
    """ use YOLOv4's code"""
    bboxes = []
    in_file = open(annotation_file, encoding='utf-8')
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0 
        if obj.find('difficult')!=None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = [int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text)]
        bboxes.append(b + [cls_id] + [int(difficult)])
    return bboxes



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root_path', default="../dataset/FBD-SV-2024/", type=str,
                        help='data_root_path: The path of the dataset.')
    parser.add_argument('--train_or_val', default="train", type=str,
                        help='train_or_val: To view the train or val label.')
    args = parser.parse_args()

    label_path = args.data_root_path + "labels/" + args.train_or_val + "/"
    image_path = args.data_root_path + "images/" + args.train_or_val + "/"

    images = os.listdir(image_path)
    images.sort()
    i=-1
    command_str = "f"
    while (i < len(images)-1):
        select_str = input("Forward or backward? (Input 'f' means forward, Input 'b' means backward, Input Enter means to View, Input 'q' to break) Input: ")
        if select_str == "f":
            command_str = "f"
        if select_str == "b":
            command_str = "b"
        if select_str == "q":
            command_str = "q"
        
        if command_str == "f":
            i += 1
        elif command_str == "b":
            i -= 1
        elif command_str == "q":
            break
        else:
            print("Please input 'f', 'b' or 'q'.")
            continue
        if i < 0:
            i = 0
        print("View ", images[i])
        image_name = images[i].split(".")[0]
        label_full_path = label_path + image_name + ".xml"
        frame = cv2.imread(image_path + images[i])
        if not os.path.exists(label_full_path):
            cv2.imwrite("check_test.jpg",frame)
            continue
        else:
            bboxes = convert_annotation(label_full_path)
            for bbox in bboxes:
                cv2.rectangle(frame, (bbox[0],bbox[1]), (bbox[2],bbox[3]), (0,0,255), 1, 4)
            cv2.imwrite("check_test.jpg",frame)