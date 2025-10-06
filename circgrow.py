from manim import *

class CircGrow(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5, radius = 1)
        self.play(Create(circle))
        self.wait()
        # Scale up and change to red
        self.play(circle.animate.scale(2).set_color(RED))
        self.wait()
        # Scale down and change to green
        self.play(circle.animate.scale(0.5).set_color(GREEN))
        self.wait()
        # Scale up again and change to purple
        self.play(circle.animate.scale(3).set_color(PURPLE))
        self.wait()
        # Final scale down and change to orange
        self.play(circle.animate.scale(0.3).set_color(ORANGE))
        self.wait()
