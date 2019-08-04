#!/usr/bin/env python3
import os
import cv2 as cv
import imageio as ii

print("processing....")

this_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(this_dir, "../resource/image/gif/")
tar_dir = os.path.join(this_dir, "../result/image/gif/")

buff = []
for i in range(4, 25):
    image = cv.imread(src_dir + "{:04d}".format(i) + ".jpg")
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    buff.append(image)
    print(i)

gif = ii.mimsave(tar_dir + "tar.gif", buff, "GIF", duration=1)

print("done!")