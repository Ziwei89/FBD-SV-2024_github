[简体中文](README_CN.md)

The Flying Bird object Dataset in Surveillance Video (FBD-SV-2024) for surveillance video flying bird object detection algorithm development and performance evaluation.  
The FBD-SV-2024 comprises 483 video clips, totaling 28,694 frames of images. Among these frames, 23,833 frames contain a total of 28,366 instances of flying birds.
# Get the dataset
kaggle address:  
Baidu Netdisk:  
# Label content
The label files are in XML format, and the main contents included in the labels are as follows:  
Item | For object detection  | For VIdeo object Detection  
---- | ----- | ------  
images size	    |   width, height, depth    |  width, height  
object class    |   bird                    |  n01503061  
difficult level |   difficult               |  difficult  
track id        |   -                       |  track_id  
bounding box    |   xmin, ymin, xmax, ymax  |  xmin, ymin, xmax, ymax  