#!/usr/bin/env python3
import os
import cv2 as cv
import numpy as np
import utils.file_helper as fh
from PIL import Image, ImageDraw, ImageFont

def draw_text(image, text, position):
    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("simsun.ttc", 24)
    draw.text(position, text, fill=(0, 127, 255), font=font)
    return np.asarray(img)

print("processing....")

this_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(this_dir, "../resource/image/compose/")
tar_dir = os.path.join(this_dir, "../result/video/compose/")

files = fh.get_files_fullname(src_dir)
for file in files:
    print(file)
    image = cv.imread(src_dir + file)
    image = draw_text(image, file, (50, 100))

    if "video_writer" not in locals():
        video_writer = cv.VideoWriter(tar_dir + "tar.mp4", cv.VideoWriter_fourcc(*"XVID"), 12, (image.shape[1], image.shape[0]))
    
    video_writer.write(image)

    cv.imshow("foo", image)
    cv.waitKey(10)

video_writer.release()

print("done!")