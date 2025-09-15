from manim import *
import os

class SlidesScene(Scene):
    def __init__(self, slides, **kwargs):
        super().__init__(**kwargs)
        self.slides = slides

    def construct(self):
        for slide in self.slides:
            # Title
            title = Text(slide["title"], font_size=48)
            self.play(Write(title))
            self.wait(0.5)
            # Bullets
            # position bullets below title
            bullet_texts = []
            for i, line in enumerate(slide["content"]):
                t = Text(f"• {line}", font_size=32)
                t.next_to(title, DOWN * (i+1)*1.2)
                bullet_texts.append(t)
            for t in bullet_texts:
                self.play(FadeIn(t))
                self.wait(0.2)
            self.wait(1)
            self.clear()
