from manim import *
import numpy as np

class SinCurve(Scene):
    def construct(self):
        Circ = ParametricFunction(
            lambda u: (np.cos(u), np.sin(u), 0),
            t_range=[0, 2*np.pi],
            color=BLUE
        )

        sinAxes = Axes(
            x_range=[0,7,1],
            y_range=[-2,2,1],
            x_length=7,
            y_length=4,
            axis_config={
                "include_tip": False
            },
            y_axis_config={
                "include_tip": False
            }
        )
                


        # Position the axes to the right of the circle
        sinAxes.next_to(Circ, RIGHT, buff=1)
        # Group both objects and center them
        group = VGroup(Circ, sinAxes)
        group.move_to(ORIGIN)

        # Draw sin curve on the axes
        sinCurve = sinAxes.plot(lambda x: np.sin(x), x_range=[0, 2*np.pi], color=RED)

        # TODO: radius should start with one end in center of circle not center of page, fixing this should get the animation working
        radius = Line((0,0,0), (1,0,0))
        self.play(Create(radius))

        def tempRadiusUp(mob):
            mob.become(Line((0,0,0), Circ.get_end()))
            
        radius.add_updater(tempRadiusUp)

        # Create and animate the objects
        self.play(Create(Circ))
        self.play(Create(sinAxes))
        self.play(Create(sinCurve))
