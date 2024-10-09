# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:59:31 2024

@author: bhuva
"""
#Task 4: Perform edge detection on images using Canny operator.

import cv2

img = cv2.imread(r"C:\Users\bhuva\Downloads\CV\jerry.jpg", cv2.IMREAD_GRAYSCALE)

blurred_img = cv2.GaussianBlur(img, (5, 5), 1.5)
edges = cv2.Canny(blurred_img, 100, 200)

cv2.imshow('Original Image', img)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
