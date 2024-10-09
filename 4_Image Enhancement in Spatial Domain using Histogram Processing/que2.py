#To perform histogram equalization to enhance the contrast of the image
import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_image_and_histogram(image, ax_image, ax_hist, title):
    ax_image.imshow(image, cmap='gray')
    ax_image.set_title(title)
    ax_image.axis('off')

    ax_hist.hist(image.ravel(), bins=256, range=[0, 256], color='black')
    ax_hist.set_xlim([0, 256])
    ax_hist.set_title(f'{title} Histogram')

# Load the original image in grayscale
original_image = cv2.imread(r"C:\Users\Administrator\Downloads\CV\highcontrast.jpg", cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = cv2.equalizeHist(original_image)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot original image and its histogram
plot_image_and_histogram(original_image, axes[0, 0], axes[0, 1], 'Original Image')

# Plot equalized image and its histogram
plot_image_and_histogram(equalized_image, axes[1, 0], axes[1, 1], 'Equalized Image')

plt.tight_layout()
plt.show()