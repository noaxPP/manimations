from manim import *

class JustAnotherManimFile(Scene):
    def construct(self):

        box = Rectangle(stroke_color= GREEN, stroke_opacity= 0.2, width = 1, height= 1, fill_color= RED_B, fill_opacity= 0.2)

        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time= 2)
        self.play(box.animate.shift(UP*3), run_time= 2)
        self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=2)
        self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=2)
        
        self.wait(1)
