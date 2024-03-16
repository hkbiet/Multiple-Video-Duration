import os

import cv2
import datetime
import argparse


def initialise_args():
    parser = argparse.ArgumentParser(description='Get flag values')
    parser.add_argument('-p', '--path', required=True, help='root directory for video files and sub directories')
    args = parser.parse_args()
    video_file = args.path
    return video_file


def get_total_video_duration(filename):
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    try:
        seconds = frame_count / fps
    except:
        return datetime.timedelta(seconds=0)
    return datetime.timedelta(seconds=seconds)


def iterate_directories(directory):
    total_duration = datetime.timedelta(seconds=0)
    for root, dirs, files in os.walk(directory):
        print(f"Current directory: {root}")
        print(f"Subdirectories: {dirs}")
        print(f"Files: {files}")
        for each_file in files:
            print(f"Processing File: {each_file}")
            total_duration += get_total_video_duration(os.path.join(root, each_file))
        print("\n")
    return total_duration


if __name__ == '__main__':
    total_duration = iterate_directories(initialise_args())
    print(f"Total Video Duration: {total_duration}")
