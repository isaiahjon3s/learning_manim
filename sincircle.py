from manim import *
import numpy as np

class SinCurve(Scene):
    def construct(self):
        Circ = ParametricFunction(
            lambda u: (np.cos(u), np.sin(u), 0),
            t_range=[0, 2*np.pi],
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

        theta = ValueTracker(0)

        # Draw sin curve on the axes
        sinCurve = sinAxes.plot(lambda x: np.sin(x), x_range=[0, 0.001])

        # Draw radius from center of circle
        radius = Line((-4,0,0), (-3,0,0))
        self.play(Create(radius))


        # Create and animate the objects
        self.play(Create(Circ))
        self.play(Create(sinAxes))
        self.play(Create(sinCurve))

        label1 = Text("angle").scale(.50).next_to(sinAxes, RIGHT)
        label2 = Text("y - coordinate").scale(.50).next_to(sinAxes, UP).shift(3*LEFT)
        self.add(label1, label2)
        self.wait()

        def sinCurveUp(mob):
            if theta.get_value() > 0:
                mob.become(sinAxes.plot(lambda x: np.sin(x), x_range=[0, theta.get_value()]))

        sinCurve.add_updater(sinCurveUp)

        def radiusUp(mob):
            mob.become(Line((-4,0,0), (np.cos(theta.get_value())-4.05, np.sin(theta.get_value()), 0)))
        radius.add_updater(radiusUp)

        connector = DashedLine(radius.get_end(), sinCurve.get_end()).set_stroke_width(3).set_color(RED)
        self.add(connector)

        # Update the connector to follow the sin curve
        def connectorUp(mob):
            current_theta = theta.get_value()
            radius_end = (np.cos(current_theta)-4.05, np.sin(current_theta), 0)
            sin_curve_end = sinAxes.c2p(current_theta, np.sin(current_theta))
            mob.become(DashedLine(radius_end, sin_curve_end).set_stroke_width(3).set_color(RED))
        connector.add_updater(connectorUp)

        self.play(theta.animate.set_value(2*np.pi))

