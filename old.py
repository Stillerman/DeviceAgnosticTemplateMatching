import json
import cv2 as cv
import numpy as np
import sys 

mainPath = sys.argv[1]
templatePath = sys.argv[2]

img_rgb = cv.imread(mainPath)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread(templatePath,0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

threshold = 0.7
loc = np.where( res >= threshold)

result = []

for pt in zip(*loc[::-1]):
    result.append([int(pt[0]), int(pt[1])])

print(json.dumps(result))

if len(sys.argv) >= 4:
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv.imwrite('res.png',img_rgb)