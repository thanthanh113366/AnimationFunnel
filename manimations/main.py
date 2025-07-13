from manim import *
from manim_slides import Slide

class Example(Slide):
    def construct(self):
        circle = Circle()
        dot = Dot().move_to(circle.get_right())

        self.play(Create(circle), GrowFromCenter(dot))
        self.next_slide()

        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()


        self.play(dot.animate.move_to(ORIGIN))
        self.next_slide()    