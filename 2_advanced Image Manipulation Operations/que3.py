# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:58:05 2024

@author: bhuva
"""


"""Task 3:
    Perform image interpolation and 
    apply it to image resizing (shrinking & zooming)
"""
import cv2
import matplotlib.pyplot as plt

# Load the original image
image = cv2.imread(r"C:\Users\bhuva\Downloads\CV\tom.jpg")

# Define new sizes
shrink_size = (image.shape[1] // 2, image.shape[0] // 2)  # Shrink to half
zoom_size = (image.shape[1] * 4, image.shape[0] * 4)      # Zoom to four times

# Shrink the image using different interpolation methods
shrinked_nearest = cv2.resize(image, shrink_size, interpolation=cv2.INTER_NEAREST)
shrinked_bilinear = cv2.resize(image, shrink_size, interpolation=cv2.INTER_LINEAR)
shrinked_bicubic = cv2.resize(image, shrink_size, interpolation=cv2.INTER_CUBIC)

# Zoom the image using different interpolation methods
zoomed_nearest = cv2.resize(image, zoom_size, interpolation=cv2.INTER_NEAREST)
zoomed_bilinear = cv2.resize(image, zoom_size, interpolation=cv2.INTER_LINEAR)
zoomed_bicubic = cv2.resize(image, zoom_size, interpolation=cv2.INTER_CUBIC)

# Convert images from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
shrinked_nearest_rgb = cv2.cvtColor(shrinked_nearest, cv2.COLOR_BGR2RGB)
shrinked_bilinear_rgb = cv2.cvtColor(shrinked_bilinear, cv2.COLOR_BGR2RGB)
shrinked_bicubic_rgb = cv2.cvtColor(shrinked_bicubic, cv2.COLOR_BGR2RGB)
zoomed_nearest_rgb = cv2.cvtColor(zoomed_nearest, cv2.COLOR_BGR2RGB)
zoomed_bilinear_rgb = cv2.cvtColor(zoomed_bilinear, cv2.COLOR_BGR2RGB)
zoomed_bicubic_rgb = cv2.cvtColor(zoomed_bicubic, cv2.COLOR_BGR2RGB)

# Add dimensions as text
font = cv2.FONT_HERSHEY_SIMPLEX

def add_dimensions(img, img_name):
    cv2.putText(img, f"{img.shape[1]} px", (img.shape[1] // 2 - 50, img.shape[0] - 10), font, 1, (255, 255, 255), 2)
    cv2.putText(img, f"{img.shape[0]} px", (10, img.shape[0] // 2), font, 1, (255, 255, 255), 2)

add_dimensions(image_rgb, "Original")
add_dimensions(shrinked_nearest_rgb, "Shrinked (Nearest)")
add_dimensions(shrinked_bilinear_rgb, "Shrinked (Bilinear)")
add_dimensions(shrinked_bicubic_rgb, "Shrinked (Bicubic)")
add_dimensions(zoomed_nearest_rgb, "Zoomed (Nearest)")
add_dimensions(zoomed_bilinear_rgb, "Zoomed (Bilinear)")
add_dimensions(zoomed_bicubic_rgb, "Zoomed (Bicubic)")

# Plot the images
plt.figure(figsize=(18, 10))

plt.subplot(2, 4, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 4, 2)
plt.imshow(shrinked_nearest_rgb)
plt.title('Shrunk (Nearest Interpolation)')
plt.axis('off')

plt.subplot(2, 4, 3)
plt.imshow(shrinked_bilinear_rgb)
plt.title('Shrunk (Bilinear Interpolation)')
plt.axis('off')

plt.subplot(2, 4, 4)
plt.imshow(shrinked_bicubic_rgb)
plt.title('Shrunk (Bicubic Interpolation)')
plt.axis('off')

plt.subplot(2, 4, 6)
plt.imshow(zoomed_nearest_rgb)
plt.title('Zoomed (Nearest Interpolation)')
plt.axis('off')

plt.subplot(2, 4, 7)
plt.imshow(zoomed_bilinear_rgb)
plt.title('Zoomed (Bilinear Interpolation)')
plt.axis('off')

plt.subplot(2, 4, 8)
plt.imshow(zoomed_bicubic_rgb)
plt.title('Zoomed (Bicubic Interpolation)')
plt.axis('off')

plt.tight_layout()
plt.show()
