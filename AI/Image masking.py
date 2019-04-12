import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('demo.jpg')
def resize_img(img):
    scale_percent = 500 / img.shape[1]
    w = int(img.shape[1] * scale_percent)
    h = int(img.shape[0] * scale_percent)
    dim = (w, h)
    new_img = cv2.resize(img, dim)
    return new_img

img = resize_img(img)

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img),plt.colorbar(),plt.show()
