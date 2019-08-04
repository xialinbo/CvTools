#!/usr/bin/env python3
import os
import cv2 as cv
import numpy as np

print("processing....")

this_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(this_dir, "../resource/video/slice/")
tar_dir = os.path.join(this_dir, "../result/image/slice/")

video = cv.VideoCapture(src_dir + "src.avi")
success,frame = video.read()
i = 0
while success and i < 100:
    output_name = tar_dir + "{:04d}".format(i) + ".jpg"
    #frame = cv.resize(frame, (640, 360))
    success = cv.imwrite(output_name, frame)
    success,frame = video.read()
    i = i + 1
    print(i)

video.release()

print("done!")