import cv2
import datetime
import argparse


def initialise_args():
    parser = argparse.ArgumentParser(description='Get flag values')
    parser.add_argument('-p', '--path', required=True, help='Path to the video file')
    args = parser.parse_args()
    video_file = args.path
    return video_file


def get_video_duration(filename):
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    seconds = frame_count / fps
    video_time = datetime.timedelta(seconds=seconds)
    return video_time


if __name__ == '__main__':
    video_duration = get_video_duration(initialise_args())
    print(f"Video Duration: {video_duration}")
