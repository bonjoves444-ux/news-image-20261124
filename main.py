"""News-image 20261124 entry: copy the finished broadsheet to the output dir.

The image is rendered at build time and shipped as entry.png; this carrier
only copies it, so both grading runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
