import numpy as np
import cv2

img = cv2.imread('ex.png',0)
cv2.imshow('hello world',img)
eq = img[130:220,60:120]
cv2.imshow('eq', eq)
cv2.waitKey(0)
cv2.destroyAllWindows()