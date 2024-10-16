import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import pandas as pd
from typing import LiteralString

# Look wheel, compare with aim reading, when match boom. 
# This is a very simple implementation. You can improve it by using more advanced techniques.
# For example, you can use a neural network to detect the steering wheel and calculate the steering angle.
#.... Idk if you wanna do that
# Use a slider to seed a starting point, then pick a frame where the steering wheel is visible and the angle is known.

def extract_frames(video_path: LiteralString, start_time: float) -> tuple[list[tuple[np.ndarray, int]], float]:
    clip = VideoFileClip(video_path).subclip(start_time)
    frames = [(frame, t) for t, frame in enumerate(clip.iter_frames())]
    return frames, clip.fps

def detect_steering_wheel(frame: np.ndarray) -> np.ndarray | None:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blurred, 50, 150)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                               param1=50, param2=30, minRadius=50, maxRadius=100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        return circles
    return None

def calculate_steering_angle(frame: np.ndarray, circles: np.ndarray | None) -> float | None:
    if circles is not None:
        for (x, y, r) in circles:
            ref_point = (frame.shape[1] // 2, frame.shape[0] // 2)
            angle = np.arctan2(y - ref_point[1], x - ref_point[0]) * 180 / np.pi
            return angle
    return None

def find_timestamp_for_steering_angle(video_path: LiteralString, start_time: float, target_angle: float) -> float | None:
    frames, fps = extract_frames(video_path, start_time)

    for frame, t in frames:
        circles = detect_steering_wheel(frame)
        angle = calculate_steering_angle(frame, circles)
        if angle is not None and np.isclose(angle, target_angle, atol=1):
            timestamp = start_time + (t / fps)
            return timestamp
    return None

video_path = "path_to_your_video.mp4"
start_time = 0  # YOU the person say this to trim pit lane stuff. Make the API accept this @Saurabh

# Utilize fine-grained error locations in tracebacks for better error debugging.
# Python 3.11 automatically provides more detailed tracebacks, so no additional code is needed for this feature.

try:
    # Example of a block where multiple exceptions might occur
    # This is a placeholder for actual code that might raise exceptions
    pass
except* (ValueError, TypeError) as e:
    # Handle multiple exceptions using the new except* syntax
    for exc in e.exceptions:
        exc.add_note("An error occurred during processing.")
        print(f"An error occurred: {exc}")
