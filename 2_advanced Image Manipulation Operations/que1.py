# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:44:27 2024

@author: bhuva
"""
#Task: Perform Bitwise Operation on Images - AND OR XOR

import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\bhuva\Downloads\CV\binary1.png")
img2 = cv2.imread(r"C:\Users\bhuva\Downloads\CV\binary2.png")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)

cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise XOR', bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()