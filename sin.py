from manim import *
import numpy as np

class Curves(Scene):
    def construct(self):
        a = Axes(x_range=[-8*np.pi,8*np.pi], y_range=[-1,1])

        #Sin Curve
        sin_curve = a.plot(lambda x: np.sin(x), color=BLUE, fill_opacity=0.5)

        #Cos Curve
        cos_curve = a.plot(lambda x: np.cos(x), color=RED, fill_opacity=0.5)

        #Tan Curve
        tan_curve = a.plot(lambda x: np.tan(x), color=GREEN, fill_opacity=0.5)

        self.play(Create(a))
        self.play(Create(sin_curve))
        self.play(Create(cos_curve))
        self.play(Create(tan_curve))
        self.wait()
        self.play(FadeOut(a,sin_curve,cos_curve,tan_curve))