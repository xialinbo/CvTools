#!/usr/bin/env python3
import os
import cv2 as cv
import utils.file_helper as fh
import re

def visualize(image, line):
    width = image.shape[1]
    height = image.shape[0]
    (x, y, w, h) = getVertices(line, width, height)
    top_left = (int(x * width), int(y * height))
    bottom_right = (int((x + w) * width), int((y + h) * height))

    cv.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
    cv.imshow("foo", image)
    cv.waitKey(1000)

def getVertices(line, imageWidth, imageHeight):
    match = re.match(r"^(\d) ([\d\.]+) ([\d\.]+) ([\d\.]+) ([\d\.]+)$", line)
    centerX = float(match.group(2))
    centerY = float(match.group(3))
    width = float(match.group(4))
    height = float(match.group(5))

    return (centerX - width/2, centerY - height/2, width, height)

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
