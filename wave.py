from manim import *
import numpy as np

class Wave(Scene):
    def construct(self):
        a = Axes(x_range=[-8*np.pi,8*np.pi], y_range=[-1,1])

        for var in np.arange(0, 2*np.pi, 0.1):
            wave = a.plot(lambda x, v=var: np.sin(x+v), color=BLUE)
            self.play(Create(wave))
            self.play(wave.animate.shift(0.1*RIGHT))
            self.wait()
            self.play(FadeOut(wave))
            self.wait()
        self.play(FadeOut(a,wave))