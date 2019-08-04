#!/usr/bin/env python3
import cv2 as cv
import numpy as np

colors = {}
for i in range(1, 50):
    index = i * 256 * 2 / 50
    is_green_blue = index < 256
    saturation = index % 256

    colors[i] = (0 if is_green_blue else saturation, saturation if is_green_blue else 255 - saturation, 255 - saturation if is_green_blue else 0)

image = np.zeros((1000, 1000, 3), dtype=np.uint8)
for i in range(10, 500):
    cv.circle(image, (500, 500), i, colors[i//10])

cv.imshow("foo", image)
cv.waitKey(0)