#!/usr/bin/env python3
import os
import cv2 as cv
import utils.file_helper as fh
import re

def visualize(image, line):
    width = image.shape[1]
    height = image.shape[0]
    (top_left, bottom_right) = get_vertices(line, width, height)

    cv.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
    cv.imshow("foo", image)
    cv.waitKey(1000)

def get_vertices(line, image_width, image_height):
    match = re.match(r"^(\d) ([\d\.]+) ([\d\.]+) ([\d\.]+) ([\d\.]+)$", line)
    center_x = float(match.group(2))
    center_y = float(match.group(3))
    width = float(match.group(4))
    height = float(match.group(5))

    top_left = (int((center_x - width/2) * image_width), int((center_y - height/2) * image_height))
    bottom_right = (int((center_x + width/2) * image_width), int((center_y + height/2) * image_height))

    return (top_left, bottom_right)

print("processing....")

this_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(this_dir, "../resource/dl/")
img_dir = os.path.join(src_dir, "img/")
data_dir = os.path.join(src_dir, "data/")

files = fh.get_files(img_dir)
for file in files:
    print(file)
    image = cv.imread(img_dir + file + ".jpg")
    data = open(data_dir + file + ".txt")
    lines = data.readlines()
    for line in lines:
        visualize(image, line)

    data.close()

print("done!")
