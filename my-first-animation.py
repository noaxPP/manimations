from manim import *

class Scene1(Scene):
    def construct(self):
        rect1 = Rectangle(height=0.5, width=0.5, color=WHITE, fill_opacity=1)
        rect2 = Rectangle(height=0.5, width=0.5, color=WHITE, fill_opacity=1).move_to([5, 0, 0])
        r1 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r2 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r3 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r4 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r5 = Rectangle(height=0.5, width=0.5, fill_opacity=1)

        group = VGroup(r1, r2, r3 ,r4 ,r5)
        group.arrange()
        group.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN)
        
        self.play(Write(rect1))
        self.play(rect1.animate.shift(LEFT*5))
        self.play(Write(rect2))

        rects = VGroup(rect1, rect2)

        self.play(rect2.animate.next_to(rect1, RIGHT))
        self.play(ReplacementTransform(rects, group))

        s1 = SurroundingRectangle(group, color=WHITE)
        s2 = SurroundingRectangle(s1, color=WHITE)
        self.play(Write(s1), Write(s2, run_time=1.5))

        T = Text("1 2 3 4 5").next_to(s2, UP, buff=0.3).scale(1.2)
        self.play(Write(T))

        self.play(Indicate(T[0], color=RED, scale_factor=1.5), Indicate(r1, color=RED, scale_factor=0.3))
        self.play(Indicate(T[1], color=RED, scale_factor=1.5), Indicate(r2, color=RED, scale_factor=0.3))
        self.play(Indicate(T[2], color=RED, scale_factor=1.5), Indicate(r3, color=RED, scale_factor=0.3))
        self.play(Indicate(T[3], color=RED, scale_factor=1.5), Indicate(r4, color=RED, scale_factor=0.3))
        self.play(Indicate(T[4], color=RED, scale_factor=1.5), Indicate(r5, color=RED, scale_factor=0.3))
        
        dot = Dot(color=RED)

        all = VGroup(group, s1, s2, T)

        self.play(ReplacementTransform(all ,dot))
        self.play(dot.animate.scale(150))
        self.play(FadeOut(dot, run_time=1.5))
        
        self.wait(3) 