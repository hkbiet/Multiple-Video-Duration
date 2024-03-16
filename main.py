import cv2
import datetime

def get_video_duration(filename):
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    seconds = frame_count / fps
    video_time = datetime.timedelta(seconds=seconds)
    return video_time

# Example usage
video_duration = get_video_duration("/home/spear/Desktop/sample.mp4")
print(f"Video Duration: {video_duration}")
