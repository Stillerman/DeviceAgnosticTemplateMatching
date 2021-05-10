import json
import cv2 as cv
import numpy as np
import sys 
# from google.colab.patches import cv2_imshow # for image display
from skimage import io #for importing images directly from URLs


img_rgb = cv.imread("./SnapDataset/pixel2/IMG_0574.PNG")
img = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

template = cv.imread("./SnapDataset/pixel2/add_button_slim.png")
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

w, h = template.shape[::-1]

print ("Running template")

res = cv.matchTemplate(img,template,cv.TM_CCOEFF_NORMED)

print(res.shape)
print (res.max())

threshold = 0.5
loc = np.where( res >= threshold)

result = []

for pt in zip(*loc[::-1]):
    result.append([int(pt[0]), int(pt[1])])

print(len(result))


for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imshow('res.png',img_rgb)
res = cv.waitKey(0)

