[English](README.md)

监控视频飞鸟目标数据集FBD-SV-2024用于监控视频飞鸟目标检测算法的开发和性能评估。  
监控视频飞鸟目标数据集(FBD-SV-2024)包含有483个视频片段，共计28694帧图像。其中23833帧图像中包含有28366只飞鸟目标实例。
# 获取该数据集
kaggle地址：  
百度网盘:  
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
           |        |            |---bird_1.mp4
           |        |            |---bird_2.mp4
           |        |---val/             ...
           |                 ...
           |
           |---images/
           |        |---train/
           |        |            |---bird_1_000000.jpg
           |        |            |---bird_1_000001.jpg
           |        |---val/              ...
           |                 ...
           |
           |---labels/
           |        |---train/
           |        |            |---bird_1_000000.xml
           |        |            |---bird_1_000001.xml
           |        |---val/               ...
           |                 ...
           |---VID/
                   |---images/
                   |        |---train/
                   |        |            |---bird_1/
                   |        |            |       |---000000.JPEG
                   |        |            |       |---000001.JPEG
                   |        |            |              ...
                   |        |            |---bird_2/
                   |        |---val/        ...
                   |                 ...
                   |
                   |---labels/
                            |---train/
                            |            |---bird_1/
                            |            |       |---000000.xml
                            |            |       |---000001.xml
                            |            |              ...
                            |            |---bird_2/
                            |---val/        ...
                                      ...
```
# 视频拆帧
提供了两个脚本用于对视频进行拆帧处理：FBD-SV-2024/Common/split_video_frames_for_object_detection.py和FBD-SV-2024/Common/split_video_frames_for_video_object_detection.py。运行这两个脚本需要安装opencv-python，需要指定FBD-SV-2024数据集所在路径。
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
## 1、查看标签脚本