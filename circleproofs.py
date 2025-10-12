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
        # Add labels
        x_label = Text("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y").next_to(axes.y_axis.get_end(), UP)
        self.play(Create(x_label), Create(y_label))
        self.wait()

        # Create theta tracker starting at 0
        theta = ValueTracker(0)
        
        # Draw radius of 1
        radius = Line((0,0,0), (1,0,0), color=YELLOW)
        self.play(Create(radius))
        self.wait()
        
        # Add radius label
        radius_label = Text("r", color=YELLOW).scale(0.7)
        radius_label.add_updater(lambda m: m.next_to(radius.get_center(), UP*0.3))
        self.play(Create(radius_label))
        self.wait()
        
        # Add updater to make radius rotate with theta
        def radiusUp(mob):
            mob.become(Line((0,0,0), (np.cos(theta.get_value()), np.sin(theta.get_value()), 0), color=YELLOW))
        radius.add_updater(radiusUp)
        
        # Create circle that will be traced by the radius
        circle = ParametricFunction(
            lambda t: (np.cos(t), np.sin(t), 0),
            t_range=[0, theta.get_value()],  # Start with no circle
            color=BLUE
        )
        self.add(circle)
        
        # Add updater to make circle grow with theta
        def circleUp(mob):
            mob.become(
                ParametricFunction(
                    lambda t: (np.cos(t), np.sin(t), 0),
                    t_range=[0, theta.get_value()],
                    color=BLUE
                )
            )
        circle.add_updater(circleUp)
        
        # Animate theta from 0 to 2*pi to draw the circle
        self.play(theta.animate.set_value(2*np.pi), run_time=4, rate_func=linear)
        self.wait()


