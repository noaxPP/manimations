from manim import *
#this code is horrible im sorry i am going to fix it
config.assets_dir = "assets"
config.background_color = BLACK

class Hobbys(Scene):
    def construct(self):

        t =SVGMobject(
            "table-tennis",
            fill_color=WHITE,
        ).scale(0.7)
        
        f =SVGMobject(
            "football",
            fill_color=WHITE
        ).scale(0.7)

        p =SVGMobject(
            "programming",
            fill_color=WHITE
        ).scale(0.7)

        hobbys = VGroup(t, f, p)
        hobbys.arrange(buff = 1)
        self.play(Write(hobbys, run_time=2))

        text = Text(
            "My Hobbys"
        ).scale(1.2).move_to(DOWN*2)

        self.play(Transform(hobbys, text))
        self.play(Indicate(text[2:9], color=PURE_GREEN, run_time= 2))
        