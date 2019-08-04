#!/usr/bin/env python3
import os
import cv2 as cv
import numpy as np

def get_processed_image(image):
    img = image[66:533, 333:1066]
    
    #rows,cols = image.shape[0:2]
    #if rows != height or cols != width:
    #    image = cv.resize(image, (width, height))
    
    return img

print("processing....")

this_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(this_dir, "../resource/video/retouch/")
tar_dir = os.path.join(this_dir, "../result/video/retouch/")

video = cv.VideoCapture(src_dir + "src.mp4")
success,frame = video.read()
while success:
    image = get_processed_image(frame)

    if "video_writer" not in locals():
        video_writer = cv.VideoWriter(tar_dir + "tar.avi", cv.VideoWriter_fourcc(*"XVID"), 13, (image.shape[1], image.shape[0]))

    video_writer.write(image)
    success,frame = video.read()

    cv.imshow("foo", image)
    cv.waitKey(10)

video_writer.release()
video.release()

print("done!")