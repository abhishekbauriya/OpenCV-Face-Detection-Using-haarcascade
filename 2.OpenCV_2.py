# OpenCV - Working with Images-II
#Simple Program to Read Images

import cv2

img = cv2.imread('Dog.png')
gray = cv2.imread('Dog.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image',img)
cv2.imshow('Gray Dog Image',gray)

cv2.waitkey(0)
cv2.destroyAllWindows()