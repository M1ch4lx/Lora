from Export import export
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from typing import Callable

lora = None


@export
def plot(x: list, y: list):
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()


@export
def plot_function(callback: Callable, args_range: list):
    left, right = args_range[0], args_range[1]
    args = np.linspace(left, right)
    values = np.array([lora.call_function(callback, [x]) for x in args])
    plot(args.tolist(), values.tolist())


@export
def numpy_array(values: list):
    return np.array(values)


@export
def vector(values: list):
    return np.array(values)


@export
def matrix(values: list):
    return np.array(values)


@export(np.ndarray.__name__)
class NumpyArray:
    @export
    def to_list(array: np.ndarray):
        return array.tolist()

    @export
    def dot(array: np.ndarray, other: np.ndarray):
        return array.dot(other)


class Animation:
    def __init__(self):
        self.frames = []
        self.current_frame_data = []
        self.vector_count = None
        self.anchor = [0, 0]
        self.marker = 'blue'

    def add_vector_state(self, x, y):
        self.current_frame_data.append(([x, y], self.anchor, self.marker))

    def save_frame(self):
        if self.vector_count is None:
            self.vector_count = len(self.current_frame_data)
        elif self.vector_count != len(self.current_frame_data):
            raise Exception('Objects count in animation frame is not matching')
        self.frames.append(self.current_frame_data)
        self.current_frame_data = []

    def vector_scatter(self, vector, anchor=None, color='blue'):
        def normalized(v):
            norm = np.linalg.norm(v)
            if norm == 0:
                return v
            return v / norm

        if anchor is None:
            anchor = np.array([0, 0])
        else:
            anchor = np.array(anchor)
        x, y = vector[0], vector[1]
        norm = np.linalg.norm(np.array(vector))
        w = normalized(np.array(vector))
        size = 0.1
        h = size * np.sqrt(3)
        arrow_end = w * h
        arrow_left = np.array([-w[1], w[0]]) * size
        arrow_right = np.array([w[1], -w[0]]) * size
        triangle = [arrow_left, arrow_end, arrow_right, arrow_left]
        for i, p in enumerate(triangle):
            triangle[i] = p + (normalized(arrow_end) * (norm - h))
            triangle[i] += anchor
        return [go.Scatter(x=[anchor[0], anchor[0] + x], y=[anchor[1], anchor[1] + y], mode='lines',
                           line=dict(color=color)),
                go.Scatter(x=[v[0] for v in triangle], y=[v[1] for v in triangle], fill="toself", mode='lines',
                           line=dict(color=color))]

    def frame_to_scatter_plot(self, frame):
        scatters = []
        for vec, anchor, color in frame:
            scatters += self.vector_scatter(vec, anchor, color)
        return scatters

    def play(self):
        fig = go.Figure(
            data=self.frame_to_scatter_plot(self.frames[0]),
            layout=go.Layout(
                autosize=False,
                width=700,
                height=600,
                xaxis=dict(range=[0, 5], autorange=False, scaleanchor='x', scaleratio=1),
                yaxis=dict(range=[0, 5], autorange=False, scaleanchor='y', scaleratio=1),
                title="Start Title",
                updatemenus=[dict(
                    type="buttons",
                    buttons=[dict(label="Play",
                                  method="animate",
                                  args=[None])])]
            ),
            frames=[go.Frame(data=self.frame_to_scatter_plot(frame)) for frame in self.frames[1:]]
        )

        fig.show()


@export
def create_animation():
    return Animation()


@export(Animation.__name__)
class AnimationPrototype:
    @export
    def save_frame(animation: Animation):
        animation.save_frame()

    @export
    def anchor(animation: Animation, x: float, y: float):
        animation.anchor = [x, y]

    @export
    def set_marker_color(animation: Animation, color: str):
        animation.marker = color

    @export
    def vector(animation: Animation, x: float, y: float):
        animation.add_vector_state(x, y)

    @export
    def vector_array(animation: Animation, vectors: np.ndarray):
        pass

    @export
    def play(animation: Animation):
        animation.play()
