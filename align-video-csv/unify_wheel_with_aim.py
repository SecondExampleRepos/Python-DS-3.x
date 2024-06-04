import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def extract_frames(video_path, start_time):
    clip = VideoFileClip(video_path).subclip(start_time)
    frames = [frame for frame in clip.iter_frames()]
    return frames

def detect_steering_wheel(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blurred, 50, 150)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                               param1=50, param2=30, minRadius=50, maxRadius=100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        return circles
    return None

def calculate_steering_angle(frame, circles):
    if circles is not None:
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            ref_point = (frame.shape[1] // 2, frame.shape[0] // 2)
            angle = np.arctan2(y - ref_point[1], x - ref_point[0]) * 180 / np.pi
            return angle
    return None

video_path = "path_to_your_video.mp4"
start_time = 30  # YOU the person say this to trim pit lane stuff. Make the API accept this @Saurabh

frames = extract_frames(video_path, start_time)

for frame in frames:
    circles = detect_steering_wheel(frame)
    angle = calculate_steering_angle(frame, circles)
    if angle is not None:
        print(f"Steering Angle: {angle:.2f} degrees")
