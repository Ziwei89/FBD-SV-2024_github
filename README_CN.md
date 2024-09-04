[English](README.md)

监控视频飞鸟目标数据集FBD-SV-2024用于监控视频飞鸟目标检测算法的开发和性能评估。  
监控视频飞鸟目标数据集(FBD-SV-2024)包含有483个视频片段，共计28694帧图像。其中23833帧图像中包含有28366只飞鸟目标实例。  

请查阅与该数据集相关的paper获取更多关于该数据集特征的描述。paper链接: https://arxiv.org/abs/2409.00317  
如果该数据集对您的工作有用请引用该paper:  
```
@misc{sun2024fbdsv2024,
    title={FBD-SV-2024: Flying Bird Object Detection Dataset in Surveillance Video},
    author={Zi-Wei Sun and Ze-Xi Hua and Heng-Chao Li and Zhi-Peng Qi and Xiang Li and Yan Li and Jin-Chi Zhang},
    year={2024},
    eprint={2409.00317},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```
# 获取该数据集
kaggle地址：https://www.kaggle.com/datasets/swjtuziwei/fbd-sv-2024  
百度网盘: https://pan.baidu.com/s/1sw7bv4BeiMnHWyH4BNutYg 提取码：48w4
# 标签内容
标签文件为xml格式，标签中包含的主要内容如下：  
 项目       | 用于目标检测            | 用于视频目标检测  
 :----:     | :-----:                | :------:  
 图像尺寸    |   width, height, depth | width, height  
 目标类型    |   bird                 | n01503061  
 难度等级    | difficult              | difficult  
 目标号      | -                      | track_id  
 目标边界框  | xmin, ymin, xmax, ymax | xmin, ymin, xmax, ymax  

# 数据集目录结构
FBD-SV-2024的结构如下（其中，VID目录下分支用于视频目标检测。FBD-SV-2024的结构如下（其中，VID目录下分支用于视频目标检测。由于图片数据较大，没有上传图片，但是提供了相关python脚本，可以通过运行该脚本，对视频进行拆帧得到，后面将说明如何使用所提供的脚本）：
```
FBD-SV-2024/
           |---videos/
           |        |---train/
           |        |         |---bird_1.mp4
           |        |         |---bird_2.mp4
           |        |---val/        ...
           |                 ...
           |
           |---images/
           |        |---train/
           |        |         |---bird_1_000000.jpg
           |        |         |---bird_1_000001.jpg
           |        |---val/        ...
           |                 ...
           |
           |---labels/
           |        |---train/
           |        |         |---bird_1_000000.xml
           |        |         |---bird_1_000001.xml
           |        |---val/        ...
           |                 ...
           |---VID/
                   |---images/
                   |        |---train/
                   |        |         |---bird_1/
                   |        |         |         |---000000.JPEG
                   |        |         |         |---000001.JPEG
                   |        |         |              ...
                   |        |         |---bird_2/
                   |        |---val/        ...
                   |                 ...
                   |
                   |---labels/
                            |---train/
                            |         |---bird_1/
                            |         |         |---000000.xml
                            |         |         |---000001.xml
                            |         |              ...
                            |         |---bird_2/
                            |---val/      ...
                                      ...
```

<font color=red>注意：</font> 某些脚本来源于其他工程或互联网，在此鸣谢。若需要特别指明或存在权力要求，请联系sun_zi_wei@my.swjtu.edu.cn。

# 视频拆帧
提供了两个脚本用于对视频进行拆帧处理：FBD-SV-2024_github/Common/split_video_frames_for_object_detection.py和FBD-SV-2024_github/Common/split_video_frames_for_video_object_detection.py。运行这两个脚本需要安装opencv-python，需要指定FBD-SV-2024数据集所在路径。
## 1、拆帧用于目标检测，图片将保存于FBD-SV-2024/images/train/ 和FBD-SV-2024/images/val/目录下。
```
python split_video_frames_for_object_detection.py \
                     --data_root_path=/path/to/your/FBD-SV-2024/
```
## 2、拆帧用于视频目标检测，图片将保存于FBD-SV-2024/VID/images/train/ 和FBD-SV-2024/VID/images/val/目录下。
```
python split_video_frames_for_video_object_detection.py \
                    --data_root_path=/path/to/your/FBD-SV-2024/
```
# 其他脚本
## 1、查看真值标签，FBD-SV-2024_github/Common/view_label.py
通过这个脚本，可以查看真值标签。将在图片目标上画出边界框，保存于check_test.jpg，可以按提示向前和向后遍历。运行这个脚本需要安装解析xml文件的包xml.etree.ElementTree，需要指定FBD-SV-2024数据集所在路径和指定遍历train还是val。
```
python view_label.py \
        --data_root_path=/path/to/your/FBD-SV-2024/ \
        --train_or_val=train
```
## 2、准备YOLO目标检测数据相关脚本
### （1）voc的xml标签转换为yolo所需的txt标签，FBD-SV-2024_github/For_YOLO/voc2yolo.py
运行该脚本需要指定voc标签路径（原始标签路径）和yolo标签路径（新标签路径）,训练标签和测试标签运行两次。
```
python voc2yolo.py \
        --raw_label_path=/path/to/your/FBD-SV-2024/labels/train \
        --new_label_path=/path/to/your/yolo_labels/train
```
### （2）获取train.txt和val.txt，FBD-SV-2024_github/For_YOLO/get_train_val_txt_for_yolo.py
运行该脚本需要指定图像路径和输出txt路径。
```
python get_train_val_txt_for_yolo.py \
        --img_path=/path/to/your/FBD-SV-2024/images/ \
        --txt_path=/path/to/your/yolo_txt_out_path/
```
### （3）yolo标签txt转coco标签json，FBD-SV-2024_github/For_YOLO/yolo2coco.py
运行该脚本需要指定图像路径、yolo标签路径和输出coco标签路径。
```
python yolo2coco.py \
        --img_path=/path/to/your/FBD-SV-2024/images/ \
        --label_path=/path/to/your/yolo_txt_label_path/val \
        --save_path=/path/to/your/coco_json_out_path/val.json
```
## 3、准备VID视频目标检测数据相关脚本：获取VID_train_15frames.txt和VID_val_videos.txt，FBD-SV-2024_github/For_VID/get_train_val_txt_for_vid.py
运行该脚本需要指定FBD-SV-2024数据集所在路径。
```
python get_train_val_txt_for_vid.py \
        --data_root_path=/path/to/your/FBD-SV-2024/
```
# 先进目标检测算法、视频目标检测算法和监控视频飞鸟目标检测算法在该数据集上的效果
在训练集上训练，测试集上测试。  
 METHOD             | AP<sub>50</sub> | AP<sub>75</sub> | AP        | AP<sub>S</sub> | AP<sub>M</sub> | AP<sub>L</sub>  
 :----:             | :-----:         | :------:        | :------:  | :------:       | :------:       | :------:  
 YOLOV5L            | 0.558            | 0.307            | 0.299      | 0.220           | 0.417           | 0.521  
 YOLOV6L            | 0.585            | 0.308            | 0.304      | 0.214           | 0.437           | 0.528  
 YOLOX              | 0.620            | 0.337            | 0.338      | 0.280           | 0.423           | 0.561  
 YOLOV8L            | 0.584            | 0.327            | 0.318      | 0.233           | 0.437           | 0.597  
 YOLOV9E            | 0.577            | 0.322            | 0.318      | 0.227           | 0.456           | 0.577  
 YOLOV10L           | 0.550            | 0.289            | 0.294      | 0.199           | 0.424           | 0.598  
 SSD                | 0.599            | 0.277            | 0.299      | 0.231           | 0.395           | 0.510  
 FGFA               | 0.198            | 0.072            | 0.092      | 0.020           | 0.187           | 0.420  
 SELSA              | 0.400            | 0.162            | 0.193      | 0.050           | 0.414           | 0.614  
 Temporal RoI Align | 0.371            | 0.180            | 0.186      | 0.038           | 0.411           | 0.582  
 [FBOD-BMI](https://ieeexplore.ieee.org/document/10329987)           | 0.692            | 0.302            | 0.351      | 0.306           | 0.434           | 0.401  
 [FBOD-SV](https://ieeexplore.ieee.org/document/10614237)            | 0.719            | 0.341            | 0.371      | 0.313           | 0.479           | 0.425  

# 另外，我们做了一些工作用于监控视频飞鸟目标的检测（供参考）：
\[1\] Z. -W. Sun, Z. -X. Hua, H. -C. Li and H. -Y. Zhong, "Flying Bird Object Detection Algorithm in Surveillance Video Based on Motion Information," in IEEE Transactions on Instrumentation and Measurement, vol. 73, pp. 1-15, 2024, Art no. 5002515, doi: 10.1109/TIM.2023.3334348.  
<br>
\[2\] Z. -W. Sun, Z. -X. Hua, H. -C. Li and Y. Li, "A Flying Bird Object Detection Method for Surveillance Video," in IEEE Transactions on Instrumentation and Measurement, vol. 73, pp. 1-14, 2024, Art no. 5026914, doi: 10.1109/TIM.2024.3435183.

# 贡献：
孙自伟，西南交通大学信息科学与技术学院博士研究生，该项目的主要负责人。具体贡献有：发起项目；规划、实施项目；设备部署、数据采集、视频片段筛选、数据处理；参与16.3%的数据标注工作。  
<br>
华泽玺，西南交通大学信息科学与技术学院教授，该项目资助人，管理人。具体贡献有：提供设备和资金支持，管理该项目的进度。  
<br>
漆智鹏，西南交通大学信息科学与技术学院博士研究生，该项目的参与者。具体贡献有：参与28.2%的数据标注工作。  
<br>
李翔，西南交通大学信息科学与技术学院硕士研究生，该项目的参与者。具体贡献有：参与19.7%的数据标注工作。  
<br>
李艳，西南交通大学信息科学与技术学院博士研究生，该项目的参与者。具体贡献有：参与18.0%的数据标注工作。  
<br>
张金驰，西南交通大学信息科学与技术学院硕士研究生，该项目的参与者。具体贡献有：参与17.8%的数据标注工作。