from manim import *
import numpy as np

class Circumference(Scene):
    def construct(self):
        # Create axes with specific dimensions
        axes = Axes(
            x_range=[-2, 2, 1], 
            y_range=[-2, 2, 1],
            x_length=4,  # Physical size on screen
            y_length=4,   # Physical size on screen
            tips=False,
            axis_config={
                "include_numbers": True
            }
        )
        self.play(Create(axes))
        self.wait()

        # Add labels
        x_label = Text("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y").next_to(axes.y_axis.get_end(), UP)
        self.play(Create(x_label), Create(y_label))
        self.wait()


        # Draw radius of 1
        radius = Line((0,0,0), (1,0,0))
        self.play(Create(radius))
        self.wait()

        # Create circle with radius 1 using parametric function
        # This will respect the axes scaling
        circle = axes.plot_parametric_curve(
            lambda t: [np.cos(t), np.sin(t)],
            t_range=[0, 2*np.pi],
            color=BLUE
        )
        self.play(Create(circle))
        self.wait()

