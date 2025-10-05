from manim import *

class CircGrow(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5, radius = 1)
        self.play(Create(circle))
        self.wait()
        self.play(circle.animate.scale(2))
        self.wait()
        self.play(circle.animate.scale(0.5))
        self.wait()
