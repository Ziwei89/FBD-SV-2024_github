[简体中文](README_CN.md)

The Flying Bird object Dataset in Surveillance Video (FBD-SV-2024) for surveillance video flying bird object detection algorithm development and performance evaluation.  
The FBD-SV-2024 comprises 483 video clips, totaling 28,694 frames of images. Among these frames, 23,833 frames contain a total of 28,366 instances of flying birds.
# Get the dataset
kaggle address:  
Baidu Netdisk:  
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