# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:56:19 2024

@author: bhuva
"""

"""Task 2:
    Perform image blurring on images with help of various low pass filter 
    kernels - Gaussian Blur, Median Blur, Average Blur.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread(r"C:\Users\bhuva\Downloads\CV\jerry.jpg")
image = cv2.resize(image, (640, 480))

# Convert from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blurs with different standard deviations
gaussian_blur_1 = cv2.GaussianBlur(image_rgb, (15, 15), 1)

gaussian_blur_2 = cv2.GaussianBlur(image_rgb, (15,15), 15)

# Apply Median Blur
median_blur = cv2.medianBlur(image_rgb, 15)

# Apply Average Blur
average_blur = cv2.blur(image_rgb, (15, 15))

# Display results using subplots
plt.figure(figsize=(15, 12))

plt.subplot(231)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(232)
plt.imshow(gaussian_blur_1)
plt.title('Gaussian Blur (σ=1)')
plt.axis('off')

plt.subplot(233)
plt.imshow(gaussian_blur_2)
plt.title('Gaussian Blur (σ=15)')
plt.axis('off')


plt.subplot(234)
plt.imshow(median_blur)
plt.title('Median Blur')
plt.axis('off')

plt.subplot(235)
plt.imshow(average_blur)
plt.title('Average Blur')
plt.axis('off')

plt.tight_layout()
plt.show()