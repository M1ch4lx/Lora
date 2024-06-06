from manimlib import *
import numpy as np
from scipy.optimize import fsolve
from Lora import Lora
from antlr4 import *
from LoraLexer import LoraLexer
from LoraParser import LoraParser
from LoraVisitorImpl import LoraVisitorImpl, StopExecution
from StandardLibrary import *

class PlotFunctions(Scene):
    def __init__(self, functions, highlight_intersections=False, highlight_zeros=False, highlight_extremes=False, draw_derivatives=False, **kwargs):
        self.functions = functions
        self.highlight_intersections = highlight_intersections
        self.highlight_zeros = highlight_zeros
        self.highlight_extremes = highlight_extremes
        self.draw_derivatives = draw_derivatives
        super().__init__(**kwargs)

    def construct(self):
        axes = Axes(
            x_range=(-10, 10, 1),
            y_range=(-10, 100, 10),
            axis_config={"color": BLUE}
        )
        
        self.add(axes)

        graphs = []
        for func, color, label in self.functions:
            graph = axes.get_graph(func, color=color)
            graph_label = axes.get_graph_label(graph, label=label)
            self.add(graph, graph_label)
            graphs.append((func, graph, color))
        
        if self.highlight_intersections:
            self.highlight_intersections_on_graphs(axes, graphs)

        if self.highlight_zeros:
            self.highlight_zeros_on_graphs(axes, graphs)

        if self.highlight_extremes:
            self.highlight_extremes_on_graphs(axes, graphs)

        if self.draw_derivatives:
            self.draw_derivatives_on_graphs(axes, graphs)

    def highlight_intersections_on_graphs(self, axes, graphs):
        for i in range(len(graphs)):
            for j in range(i + 1, len(graphs)):
                func1, graph1, _ = graphs[i]
                func2, graph2, _ = graphs[j]
                intersections = self.find_intersections_bisection(axes, func1, func2)
                for x, y in intersections:
                    dot = Dot(axes.coords_to_point(x, y), color=WHITE)
                    self.add(dot)
                    self.add(Text(f"({x:.2f}, {y:.2f})").next_to(dot, UP))

    def find_intersections_bisection(self, axes, func1, func2, x_min=-10, x_max=10, tolerance=1e-5):
        def difference(x):
            return func1(x) - func2(x)

        intersections = []
        x_values = np.linspace(x_min, x_max, 1000)

        for i in range(len(x_values) - 1):
            x0, x1 = x_values[i], x_values[i + 1]
            if difference(x0) * difference(x1) < 0:
                root = fsolve(difference, (x0 + x1) / 2)[0]
                y = func1(root)
                intersections.append((root, y))
        return intersections

    def highlight_zeros_on_graphs(self, axes, graphs):
        for func, graph, _ in graphs:
            zeros = self.find_zeros_bisection(func)
            for x in zeros:
                dot = Dot(axes.coords_to_point(x, 0), color=BLUE)
                self.add(dot)
                self.add(Text(f"({x:.2f}, 0)").next_to(dot, UP))

    def find_zeros_bisection(self, func, x_min=-10, x_max=10, tolerance=1e-5):
        zeros = []
        x_values = np.linspace(x_min, x_max, 1000)

        for i in range(len(x_values) - 1):
            x0, x1 = x_values[i], x_values[i + 1]
            if func(x0) * func(x1) < 0:
                root = fsolve(func, (x0 + x1) / 2)[0]
                zeros.append(root)
        return zeros

    def highlight_extremes_on_graphs(self, axes, graphs):
        for func, graph, _ in graphs:
            extremes = self.find_extremes_bisection(func)
            for x in extremes:
                y = func(x)
                dot = Dot(axes.coords_to_point(x, y), color=RED)
                self.add(dot)
                self.add(Text(f"({x:.2f}, {y:.2f})").next_to(dot, UP))

    def find_extremes_bisection(self, func, x_min=-10, x_max=10, h=1e-5):
        def derivative(x):
            return (func(x + h) - func(x - h)) / (2 * h)

        extremes = []
        x_values = np.linspace(x_min, x_max, 1000)

        for i in range(len(x_values) - 1):
            x0, x1 = x_values[i], x_values[i + 1]
            if derivative(x0) * derivative(x1) < 0:
                root = fsolve(derivative, (x0 + x1) / 2)[0]
                extremes.append(root)
        return extremes

    def draw_derivatives_on_graphs(self, axes, graphs):
        for func, graph, color in graphs:
            derivative_func = self.calculate_derivative(func)
            derivative_graph = axes.get_graph(derivative_func, color=color)
            self.add(derivative_graph)

    def calculate_derivative(self, func, h=1e-5):
        def derivative(x):
            return (func(x + h) - func(x - h)) / (2 * h)
        return derivative

def func1(x):
    return 3 * x**2 + 1

def func2(x):
    return 2 * x + 1

def func3(x):
    return np.sin(x)

functions = [
    (func1, RED, "3x^2 + 1"),
    #(func2, GREEN, "2x + 1"),
    #(func3, YELLOW, "sin(x)")
]

class PlotFunctionsScene(PlotFunctions):
    def __init__(self, **kwargs):
        input_stream = FileStream('test.lora')
        lexer = LoraLexer(input_stream)

        token_stream = CommonTokenStream(lexer)
        parser = LoraParser(token_stream)

        tree = parser.program()
        # print(tree.toStringTree(recog=parser))

        lora = Lora()
        lora.import_library(StandardLibrary())

        visitor = LoraVisitorImpl(lora)

        try:
            result = visitor.visit(tree)
        except StopExecution as e:
            print(lora.expression_result())
        except Exception as e:
            print(f'In line {visitor.current_statement_line}: {e}')

        super().__init__(functions, highlight_intersections=True, highlight_zeros=True, highlight_extremes=True, draw_derivatives=False, **kwargs)
