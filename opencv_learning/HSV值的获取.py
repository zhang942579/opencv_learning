import cv2
import numpy as np

red = np.uint8([[[255, 255, 255]]])

hsv_red = cv2.cvtColor(red, cv2.COLOR_RGB2HSV)

print(hsv_red)
