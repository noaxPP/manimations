from manim import *
#run this file to see if your Manim works


class Test(Scene):
    def construct(self):
        t = Text("TEST", color=WHITE)
        self.play(FadeIn(t))
        self.wait(2)
