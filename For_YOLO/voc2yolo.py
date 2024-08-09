# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import argparse
 

classes = ["bird"]   #

 
def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h
 
def convert_annotation(xml_path, new_label_path, xml_name):
    print(xml_path + xml_name + '.xml')
    in_file = open(xml_path + xml_name + '.xml', encoding='UTF-8')
    out_file = open(new_label_path + xml_name + '.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    find_obj = False
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult) == 1:
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        find_obj = True
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    if find_obj == False:
        out_file.close()
        os.remove(new_label_path + xml_name + '.txt')
if __name__ == "__main__": 

    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_label_path', default="../dataset/FBD-SV-2024/labels/val/", type=str,
                        help='raw_label_path: The voc label path.')
    parser.add_argument('--new_label_path', default="../dataset/FBD-SV-2024/yolo_labels/val/", type=str,
                        help='new_label_path: The yolo label path.')
    args = parser.parse_args()

    os.makedirs(args.new_label_path, exist_ok=True)

    xml_file_list = os.listdir(args.raw_label_path)
    for xml_file in xml_file_list:
        xml_name = xml_file.split('.')[0]
        convert_annotation(args.raw_label_path, args.new_label_path, xml_name)