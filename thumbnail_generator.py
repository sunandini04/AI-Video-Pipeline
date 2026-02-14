

from moviepy import VideoFileClip
from PIL import Image, ImageDraw, ImageFont
import os


def generate_thumbnail(video_path, title_text, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

   
    clip = VideoFileClip(video_path)
    frame = clip.get_frame(1)  
    clip.close()

    image = Image.fromarray(frame)

    draw = ImageDraw.Draw(image)

   
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    width, height = image.size

   
    text_width, text_height = draw.textbbox((0, 0), title_text, font=font)[2:]
    x = (width - text_width) / 2
    y = height - text_height - 80

   
    draw.rectangle(
        [(x - 20, y - 20), (x + text_width + 20, y + text_height + 20)],
        fill=(0, 0, 0, 180)
    )

   
    draw.text((x, y), title_text, font=font, fill="white")

    image.save(output_path)

    return output_path

