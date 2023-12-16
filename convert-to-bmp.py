import glob
import os
import subprocess

from local_settings import SOURCE_DIR

path = SOURCE_DIR + "*.png"

files = glob.glob(path)

for f in files:
    infile = os.path.basename(f)
    outfile = os.path.basename(f).replace(".png", ".bmp")

    if not os.path.isfile(os.path.join(SOURCE_DIR, outfile)):
        print("Converting %s" % infile)
        subprocess.run(["convert",
                        "-quality",
                        "100",
                        os.path.join(SOURCE_DIR, infile),
                        os.path.join(SOURCE_DIR, outfile)])

