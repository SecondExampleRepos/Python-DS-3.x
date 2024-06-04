from manim import *
import numpy as np
import cv2

class OverlayGraphOnVideo(Scene):
    def construct(self, frame):
        video_path = "path_to_your_video.mp4" # the video of you sending it -- also make the API accept this @Saurabh
        data = frame["Velocity (mph)"].values  # the data you want to overlay on the video, pick from DF

        # Load video
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        if not ret:
            raise ValueError(f"Unable to read video file {video_path}")
        frame_height, frame_width, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_rgb = np.fliplr(frame_rgb)
        video_image = ImageMobject(frame_rgb)
        video_image.scale(2)

        graph = self.create_graph(data)

        graph.to_corner(UR)

        self.add(video_image, graph)


        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = np.fliplr(frame_rgb)
            video_image = ImageMobject(frame_rgb)
            video_image.scale(2)
            self.add(video_image, graph)
            self.wait(1 / 30)  # Assuming 30 fps video

        cap.release()

    def create_graph(self, data):
        axes = Axes(
            x_range=[0, len(data), 1],
            y_range=[0, max(data) + 1, 1],
            axis_config={"color": BLUE},
        )

        graph = axes.plot_line_graph(
            x_values=range(len(data)),
            y_values=data,
            line_color=YELLOW
        )
        return VGroup(axes, graph)


