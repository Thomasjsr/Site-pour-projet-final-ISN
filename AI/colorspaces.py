import cv2
from matplotlib import pyplot as plt

img = cv2.imread('demo.png')

img_coversion = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img_coversion),plt.show()