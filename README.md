[简体中文](README_CN.md)

The Flying Bird object Dataset in Surveillance Video (FBD-SV-2024) for surveillance video flying bird object detection algorithm development and performance evaluation.  
The FBD-SV-2024 comprises 483 video clips, totaling 28,694 frames of images. Among these frames, 23,833 frames contain a total of 28,366 instances of flying birds.
# Get the dataset
kaggle address:  
Baidu Netdisk: https://pan.baidu.com/s/1sw7bv4BeiMnHWyH4BNutYg Extraction code: 48w4
# Label contents
The label files are in XML format, and the main contents included in the labels are as follows:  
 Item            | For object detection   | For VIdeo object Detection  
 :----:          | :-----:                | :------:  
 images size     |   width, height, depth | width, height  
 object class    |   bird                 | n01503061  
 difficult level | difficult              | difficult  
 track id        | -                      | track_id  
 bounding box    | xmin, ymin, xmax, ymax | xmin, ymin, xmax, ymax  

# The directory structure of the dataset
The structure of FBD-SV-2024 is as follows (where the subdirectories under the VID directory are used for video object detection. Due to the large size of image data, no images have been uploaded, but relevant Python scripts are provided. These scripts can be run to extract frames from the videos. Instructions on how to use the provided scripts will be provided later):
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

<font color=red>Note: </font> Some of the scripts come from other projects or the Internet, thanks here. If you need to specify or have rights requirements, please contact sun_zi_wei@my.swjtu.edu.cn.

# Frame extraction from video
Two scripts are provided for extracting frames from videos: FBD-SV-2024_github/Common/split_video_frames_for_object_detection.py and FBD-SV-2024_github/Common/split_video_frames_for_video_object_detection.py. To run these two scripts, you need to install opencv-python and specify the path to the FBD-SV-2024 dataset.
## 1. Frame extraction for object detection, the images will be saved in the directories FBD-SV-2024/images/train/ and FBD-SV-2024/images/val/.
```
python split_video_frames_for_object_detection.py \
                     --data_root_path=/path/to/your/FBD-SV-2024/
```
## 2. Frame extraction for VIdeo object Detection, the images will be saved in the directories FBD-SV-2024/VID/images/train/ and FBD-SV-2024/VID/images/val/.
```
python split_video_frames_for_video_object_detection.py \
                    --data_root_path=/path/to/your/FBD-SV-2024/
```
# Other Scripts
## 1. To view the Ground Truth label, FDD-SV-2024_github /Common/view_label.py
With this script, you can view the Ground Truth label. A bounding box is drawn on the image, saved in check_test.jpg, and can be traversed forward and backward as prompted. To run this script, you need to install the package XMl.etree.elementtree that parses the xml file, specify the path where the FDD-SV-2024 dataset resides, and specify whether to traverse train or val.  
```
python view_label.py \
        --data_root_path=/path/to/your/FBD-SV-2024/ \
        --train_or_val=train
```
## 2. The scripts for preparing YOLO series object detection dataset
### (1) To convert the xml label of VOC to the txt label required by YOLO, FBD-SV-2024_github/For_YOLO/voc2yolo.py
To run this script, you need to specify the VOC label path (original label path) and the YOLO label path (new label path), run the train label and the val label, respectively.  
```
python voc2yolo.py \
        --raw_label_path=/path/to/your/FBD-SV-2024/labels/train \
        --new_label_path=/path/to/your/yolo_labels/train
```
### (2) To get train.txt and val.txt, FDD-SV-2024_github/For_YOLO/get_train_val_txt_for_yol.py
To run this script, you need to specify the image path and the output txt path.  
```
python get_train_val_txt_for_yolo.py \
        --img_path=/path/to/your/FBD-SV-2024/images/ \
        --txt_path=/path/to/your/yolo_txt_out_path/
```
### (3) To convert the YOLO label to COCO label, FDD-SV-2024_github/For_YOLO/yolo2coco.py
To run the script, you need to specify the image path, YOLO label path, and output COCO label path.  
```
python yolo2coco.py \
        --img_path=/path/to/your/FBD-SV-2024/images/ \
        --label_path=/path/to/your/yolo_txt_label_path/val \
        --save_path=/path/to/your/coco_json_out_path/val.json
```
## 3. The script for preparing VID (VIdeo object Detection) dataset: To obtain VID_train_15frames.txt and VID_val_videos.txt，FBD-SV-2024_github/For_VID/get_train_val_txt_for_vid.py
To run the script, you need to specify the path to the FBD-SV-2024 dataset.  
```
python get_train_val_txt_for_vid.py \
        --data_root_path=/path/to/your/FBD-SV-2024/
```
# The detection performance of advanced object detection algorithm, video object detection algorithm and flying bird object detection algorithm on this dataset
Train on the training set, test on the val set.  
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
 FBOD-BMI           | 0.692            | 0.302            | 0.351      | 0.306           | 0.434           | 0.401  
 FBOD-SV            | 0.719            | 0.341            | 0.371      | 0.313           | 0.479           | 0.425  

# In addition, we have done some work for the detection of flying birds in surveillance videos (for reference) :
\[1\] Z. -W. Sun, Z. -X. Hua, H. -C. Li and H. -Y. Zhong, "Flying Bird Object Detection Algorithm in Surveillance Video Based on Motion Information," in IEEE Transactions on Instrumentation and Measurement, vol. 73, pp. 1-15, 2024, Art no. 5002515, doi: 10.1109/TIM.2023.3334348.  
<br>
\[2\] Z. -W. Sun, Z. -X. Hua, H. -C. Li and Y. Li, "A Flying Bird Object Detection Method for Surveillance Video," in IEEE Transactions on Instrumentation and Measurement, vol. 73, pp. 1-14, 2024, Art no. 5026914, doi: 10.1109/TIM.2024.3435183.

# Contribution:
Zi-Wei Sun, a Ph.D. candidate at the School of Information Science and Technology, Southwest Jiaotong University, is the main person in charge of this project.  His specific contributions include: initiating the project;  planning and implementing the project;  equipment deployment, data acquisition, video clip screening, and data processing;  participating in 16.3% of the data annotation work.  
<br>
Ze-Xi Hua, a professor at the School of Information Science and Technology, Southwest Jiaotong University, is the sponsor and manager of this project. His specific contributions include: providing equipment and financial support, and managing the progress of the project.  
<br>
Zhi-Peng Qi, a Ph.D. candidate at the School of Information Science and Technology, Southwest Jiaotong University, is a participant in this project. His specific contribution includes: participating in 28.2% of the data annotation work.  
<br>
Xiang Li, a graduate student at the School of Information Science and Technology, Southwest Jiaotong University, is a participant in this project. His specific contribution includes: participating in 19.7% of the data annotation work.  
<br>
Yan Li, a Ph.D. candidate at the School of Information Science and Technology, Southwest Jiaotong University, is a participant in this project. Her specific contribution includes: participating in 18.0% of the data annotation work.  
<br>
Jin-Chi Zhang, a graduate student at the School of Information Science and Technology, Southwest Jiaotong University, is a participant in this project. His specific contribution includes: participating in 17.8% of the data annotation work.