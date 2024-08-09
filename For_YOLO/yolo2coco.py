import os
import cv2
import json
from tqdm import tqdm
import argparse

classes = ['bird']#

parser = argparse.ArgumentParser()
parser.add_argument('--image_path', default='../dataset/FBD-SV-2024/images/val',type=str, help="path of images")# 图片路径改一下
parser.add_argument('--label_path', default='../dataset/FBD-SV-2024/labels/val',type=str, help="path of labels.txt")#图片标签路径改一下
parser.add_argument('--save_path', type=str,default='../val.json', help="if not split the dataset, give a path to a json file")
arg = parser.parse_args()

def yolo2coco(arg):
    print("Loading data from ", arg.image_path, arg.label_path)

    assert os.path.exists(arg.image_path)
    assert os.path.exists(arg.label_path)
    
    originImagesDir = arg.image_path                                   
    originLabelsDir = arg.label_path
    # images dir name
    indexes = os.listdir(originImagesDir)

    dataset = {'images': [], 'categories': [], 'annotations': []}
    for i, cls in enumerate(classes, 0):
        dataset['categories'].append({'id': i, 'name': cls})
    
    # 标注的id
    ann_id_cnt = 1
    for k, index in enumerate(tqdm(indexes)):
        # 支持 png jpg 格式的图片.
        txtFile = f'{index[:index.rfind(".")]}.txt'
        # stem = index[:index.rfind(".")]
        stem = index.split(".")[0]
        # 读取图像的宽和高
        try:
            im = cv2.imread(os.path.join(originImagesDir, index))
            height, width, _ = im.shape
        except Exception as e:
            print(f'{os.path.join(originImagesDir, index)} read error.\nerror:{e}')
        # 添加图像的信息
        dataset['images'].append({'file_name': index,
                                'height': height,
                                'width': width,
                                'id': stem})
        if not os.path.exists(os.path.join(originLabelsDir, txtFile)):
            # 如没标签，跳过，只保留图片信息.
            continue
        with open(os.path.join(originLabelsDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                label = label.strip().split()
                x = float(label[1])
                y = float(label[2])
                w = float(label[3])
                h = float(label[4])

                # convert x,y,w,h to x1,y1,x2,y2
                H, W, _ = im.shape
                x1 = (x - w / 2) * W
                y1 = (y - h / 2) * H
                x2 = (x + w / 2) * W
                y2 = (y + h / 2) * H
                # 标签序号从0开始计算。
                cls_id = int(label[0])   
                width = max(0, x2 - x1)
                height = max(0, y2 - y1)
                dataset['annotations'].append({
                    'image_id': stem,
                    'bbox': [x1, y1, width, height],
                    'category_id': cls_id,
                    'iscrowd': 0,
                    'id': ann_id_cnt,
                    'area': width * height,
                })
                ann_id_cnt += 1

    # 保存结果
    with open(arg.save_path, 'w') as f:
        json.dump(dataset, f)
        print('Save annotation to {}'.format(arg.save_path))

if __name__ == "__main__":
    yolo2coco(arg)