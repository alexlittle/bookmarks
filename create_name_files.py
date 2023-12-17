import argparse
import os
import subprocess

from PIL import Image, ImageDraw, ImageFont
from shutil import copyfile
from local_settings import SOURCE_DIR, OUTPUT_DIR

height = 1378
width = 6693
x_offset = 150

# accept names to generate from command line
parser = argparse.ArgumentParser("simple_example")
parser.add_argument('input_names', nargs="*")
args = parser.parse_args()

cutting_files = []

for input_name in args.input_names:
    img = Image.new(mode="RGBA", size=(width, height))

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('p052-italic.ttf', 1000)
    _, _, text_width, text_height = draw.textbbox((0, 0), input_name, font=font)
    pos_x = x_offset + (width - text_width)/2
    pos_y = (height - text_height)/2
    draw.text((pos_x, pos_y), input_name, font=font, fill='black')

    output_png = os.path.join(SOURCE_DIR, ("%s-35mm.png" % input_name.lower()))
    output_bmp = os.path.basename(output_png).replace(".png", ".bmp")
    if os.path.isfile(output_png):
        print("File for %s already exists!" % input_name)
    else:
        img.save(output_png)
        print("File for %s created" % input_name)
        subprocess.run(["convert",
                        "-quality",
                        "100",
                        os.path.join(SOURCE_DIR, output_png),
                        os.path.join(SOURCE_DIR, output_bmp)])
    cutting_files.append(output_bmp)


for cutting_file in cutting_files:
    copyfile(os.path.join(SOURCE_DIR, cutting_file), os.path.join(OUTPUT_DIR, cutting_file))
    print("%s copied" % cutting_file)
