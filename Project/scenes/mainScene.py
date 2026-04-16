from manim import *
import numpy as np


class Simulation3D(ThreeDScene):
    def construct(self):
        # 1. Khởi tạo hệ trục và vật thể
        axes = ThreeDAxes(axis_config={"include_tip": True})
        sphere = Sphere(radius=1.5, fill_opacity=0.4).set_color(BLUE)

        # Tạo nhãn cho các trục
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # 2. Thiết lập Camera ban đầu
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # 3. Hoạt ảnh
        self.add(axes, labels)
        self.play(Create(sphere), run_time=2)
        self.wait()

        # Di chuyển camera mượt mà sang góc khác
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=3)

        # Thêm một mặt phẳng cắt qua hình cầu
        plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.5,
            color=YELLOW,
        )
        self.play(Write(plane))
        self.begin_ambient_camera_rotation(rate=0.2)  # Xoay vòng quanh
        self.wait(4)
        self.stop_ambient_camera_rotation()
