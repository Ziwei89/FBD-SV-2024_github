# -*- coding: utf-8 -*-
import os
import argparse

def f_video_id(video_name):
    video_id = int(video_name.split("_")[-1])
    return video_id

def f_frame_id(frame_name):
    frame_id = int(frame_name.split(".")[0])
    return frame_id



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root_path', default="../dataset/FBD-SV-2024/", type=str,
                        help='data_root_path: The path of the dataset.')
    args = parser.parse_args()

    img_prefix_path = args.data_root_path + "VID/images/"
    label_prefix_path = args.data_root_path + "VID/labels/"

    train_txt_path =  args.data_root_path + "VID/VID_train_15frames.txt" #
    val_txt_path = args.data_root_path + "VID/VID_val_videos.txt"

    for train_val in ["train", "val"]:
        if train_val == "train":
            txt_path = train_txt_path
        else:
            txt_path = val_txt_path
        txt_file = open(txt_path, 'w')
        video_names = os.listdir(img_prefix_path + train_val + "/")
        video_names.sort(key=f_video_id)
        for video_name in video_names:
            print(video_name)
            frame_image_path = img_prefix_path + train_val + "/" + video_name
            frame_count = len(os.listdir(frame_image_path))
            specified_path = train_val + "/" + video_name

            frame_label_path = label_prefix_path + train_val + "/" + video_name
            frame_labels = os.listdir(frame_label_path)
            frame_labels.sort(key=f_frame_id)
            for frame_label in frame_labels:
                frame_id = int(frame_label.split(".")[0])
                if train_val == "train":
                    print(specified_path + " 1 " + str(frame_id+1) + " " + str(frame_count))
                    txt_file.write(specified_path + " 1 " + str(frame_id+1) + " " + str(frame_count) + "\n")
                else:
                    print(specified_path + " " + str(frame_id+1) + " " + str(frame_id) + " " + str(frame_count))
                    txt_file.write(specified_path + " " + str(frame_id+1) + " " + str(frame_id) + " " + str(frame_count) + "\n")