
import os
import cv2
import argparse

"""Split the video frames to images for object detection"""

def split_video(in_video_path, out_image_path):
    """ split video"""
    videos = os.listdir(in_video_path)
    for video_name in videos:
        if video_name.split(".")[1] != "mp4" and video_name.split(".")[1] != "avi":
            continue
        print(video_name)
        video_file_name = in_video_path + video_name
        video_file = cv2.VideoCapture(video_file_name)
        frame_num = 0
        while (True):
            ret,frame=video_file.read()
            if ret != True:
                break
            else:
                frame_name_path = out_image_path + '/' +  video_name.split(".")[0] + '_' + str(frame_num).zfill(6) + ".jpg"
                cv2.imwrite(frame_name_path, frame)
            frame_num +=1

if __name__ == "__main__": 

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root_path', default="../../dataset/FBD-SV-2024/", type=str,
                        help='data_root_path: The path of the dataset.')
    args = parser.parse_args()

    train_video_path = args.data_root_path + "videos/train/"
    train_image_path = args.data_root_path + "images/train/"
    os.makedirs(train_image_path, exist_ok=True)
    split_video(in_video_path=train_video_path, out_image_path=train_image_path)

    val_video_path = args.data_root_path + "videos/val/"
    val_image_path = args.data_root_path + "images/val/"
    os.makedirs(val_image_path, exist_ok=True)
    split_video(in_video_path=val_video_path, out_image_path=val_image_path)
