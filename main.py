from script_generator import generate_script, split_into_slides
import os
from manim_renderer import SlidesScene
from manim import config, tempconfig
import subprocess

def save_slides_data(slides, filepath="slides_data.txt"):
    with open(filepath, "w") as f:
        for slide in slides:
            f.write("Title: " + slide["title"] + "\n")
            for c in slide["content"]:
                f.write("  - " + c + "\n")
            f.write("\n")

def render_video(slides, output_name="output_video"):
    # Create a temporary manim file dynamically
    code = f"""
from manim import *
class SlidesScene(Scene):
    def construct(self):
"""
    for slide in slides:
        # indent
        title = slide["title"].replace('"', '\\"')
        code += f'        title = Text("{title}", font_size=48)\n'
        code += f'        self.play(Write(title))\n'
        code += '        self.wait(0.5)\n'
        for line in slide["content"]:
            line_escaped = line.replace('"', '\\"')
            code += f'        t = Text("• {line_escaped}", font_size=32)\n'
            code += f'        t.next_to(title, DOWN * 1.2)\n'
            code += f'        self.play(FadeIn(t))\n'
            code += f'        self.wait(0.2)\n'
        code += '        self.wait(1)\n'
        code += '        self.clear()\n'

    # write this to a file
    tmp_filename = "temp_slides_scene.py"
    with open(tmp_filename, "w") as f:
        f.write(code)

    # call manim to render it
    # low quality preview
    cmd = f"manim -pql {tmp_filename} SlidesScene -o {output_name}"
    print("Running:", cmd)
    os.system(cmd)  # or subprocess

def main():
    concept = input("Enter concept: ")
    script = generate_script(concept)
    print("=== Script ===")
    print(script)
    slides = split_into_slides(script)
    print("=== Slides ===")
    for s in slides:
        print("Slide:", s["title"])
        for c in s["content"]:
            print("  ", c)
    # optional: save slides
    save_slides_data(slides)
    # render video
    render_video(slides, output_name="video_" + concept.replace(" ", "_"))

if __name__ == "__main__":
    main()
