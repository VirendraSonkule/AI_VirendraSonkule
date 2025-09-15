import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_script(concept: str) -> str:
    prompt = f"""
You are an educational tutor. Write a detailed script explaining the concept: **{concept}**.
Include:
1. A short introduction
2. Key definitions
3. Examples
4. Summary

Make it structured with headings.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",   # or another model you have access to
        messages=[
            {"role": "system", "content": "You are a helpful tutor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )
    script = response.choices[0].message.content.strip()
    return script

def split_into_slides(script: str):
    """
    Very naive slide splitting: splits on headings (lines starting with "###" or numeric headings)
    Returns a list of slides, each a dict with title and content (list of bullet lines).
    """
    slides = []
    current_slide = {"title": "", "content": []}
    for line in script.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Simple detection: if line starts with a heading
        if line.startswith("## ") or line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4.") or line.startswith("###"):
            # start new slide
            if current_slide["title"] or current_slide["content"]:
                slides.append(current_slide)
            current_slide = {"title": line, "content": []}
        else:
            # treat it as content
            current_slide["content"].append(line)
    # Add last
    if current_slide["title"] or current_slide["content"]:
        slides.append(current_slide)
    return slides
