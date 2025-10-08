from manim import *
import numpy as np

class CircOnGraph(Scene):
    def construct(self):
        # Create axes
        axes = Axes(x_range=[-2, 2, 0.5], y_range=[-2, 2, 0.5])
        
        # Graph a circle using parametric equations
        # For x² + y² = 1, we use:
        # x = cos(t), y = sin(t) where t goes from 0 to 2π
        circle = ParametricFunction(
            lambda t: (np.cos(t), np.sin(t), 0),
            t_range=[0, 2*np.pi],
            color=BLUE
        )
        
        # Add simple text labels (no LaTeX needed)
        x_label = Text("x").next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y").next_to(axes.y_axis.get_end(), LEFT)
        
        self.play(Create(axes))
        self.play(Create(x_label), Create(y_label))
        self.play(Create(circle))
        self.wait()