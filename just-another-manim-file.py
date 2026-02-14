from manim import *
#config.assets_dir = "assets"
#↑ if you want to use svgs
config.background_color = WHITE

class Productivity(Scene):
    def construct(self):
        
        t = Text("Productivity", font="Ashbury", weight=BOLD, font_size=48).set_color_by_gradient("#40c9ff", "#e81cff").scale(2)    
        t2 = Text("But how do you achieve Productivity?", font="Ashbury", weight=BOLD, font_size=24).scale(1.3).set_color("#252526")
        t2[3:6].set_color_by_gradient("#40c9ff", "#e81cff")
        t2[-13:].set_color_by_gradient("#40c9ff", "#e81cff")
        self.play(Write(t, run_time=3))
        self.play(Transform(t, t2))

        t3 = Text("Do you need a new browser", font="Ashbury", weight=BOLD, font_size=24).scale(1.3).set_color("#252526")
        t4 = Text("Or is it just a mindset", font="Ashbury", weight=BOLD, font_size=24).scale(1.3).set_color("#252526")
        t3[-7:].set_color_by_gradient("#40c9ff", "#e81cff")
        t4[-7:].set_color_by_gradient("#40c9ff", "#e81cff")
        
        self.wait(4)