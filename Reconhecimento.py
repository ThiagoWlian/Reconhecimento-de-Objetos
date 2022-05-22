import cv2
from matplotlib import pyplot as plt
import numpy as np

template = cv2.imread('carta.png', 0)
img_rgb = cv2.imread('baralho.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
largura, altura = template.shape[::-1]
bottom_right = (min_loc[0] + largura, min_loc[1] + altura)
cv2.rectangle(img_rgb,min_loc, bottom_right, (127,255,255), 4)

cv2.imshow("Resultado", img_rgb)
cv2.waitKey()