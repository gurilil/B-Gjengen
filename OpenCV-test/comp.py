import numpy as np
import cv2

img = cv2.imread('ex.png',0)
ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#cv2.imshow('win', thresh)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
components = cv2.connectedComponentsWithStats(img, 4, cv2.CV_32S)

stats = components[2]

print(components[1])

c = []
for label in components[1]:
	xStart = stats[label,cv2.CC_STAT_LEFT]
	xEnd = xStart + stats[label,cv2.CC_STAT_WIDTH]
	yStart = stats[label,cv2.CC_STAT_TOP]
	yEnd = stats[label,cv2.CC_STAT_HEIGHT]
	print(xStart, xEnd, yStart, yEnd)
	c.append(img[xStart:xEnd, yStart:yEnd])
	

	
for im in c:
	cv2.imshow('window', im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
#comment
#test
