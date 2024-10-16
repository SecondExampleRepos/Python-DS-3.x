from manim import *
import numpy as np
import cv2

class OverlayGraphOnVideo(Scene):
    def __init__(self, df, video_path, column_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.df = df
        self.video_path = video_path
        self.column_name = column_name
        self.data = self.df[self.column_name].values
        self.construct()

    def construct(self):
        # Load video
        cap = cv2.VideoCapture(self.video_path)
        ret, frame = cap.read()
        if not ret:
            raise ValueError(f"Unable to read video file {self.video_path}")
        self.process_video(cap)

    def process_video(self, cap):
        graph = self.create_graph(self.data)
        graph.to_corner(UR.scale(0.25))  # Make it smaller?

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = np.fliplr(frame_rgb)
            video_image = ImageMobject(frame_rgb)
            video_image.scale_to_fit_height(config.frame_height)

            self.add(video_image, graph)
            self.wait(1 / 30)
            self.remove(video_image)
        cap.release()

    def create_graph(self, data):
        axes = Axes(
            x_range=[0, len(data), max(1, len(data) // 10)],
            y_range=[min(data), max(data), (max(data) - min(data)) / 10],
            axis_config={"color": BLUE},
        )
        graph = axes.plot_line_graph(
            x_values=list(range(len(data))),
            y_values=data,
            line_color=YELLOW,
        )
        return VGroup(axes, graph)

if __name__ == "__main__":
    # Dummy DataFrame setup
    meta, df = load_csv_with_custom_headers("samples/saurabh_gr86_Sonoma Race_a_0045.csv")

    video_path = "thing"  # Update this to your video path
    column_name = 'GPS Speed (mph)'  # see notebook for column names

    config.media_width = "100%"
    scene = OverlayGraphOnVideo(df, video_path, column_name)
    scene.render()
