#To perform histogram matching to adjust the histogram of an image to match a specified target histogram
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure


def plot_image_and_histogram(image, ax_image, ax_hist, title):
    ax_image.imshow(image, cmap='gray')
    ax_image.set_title(title)
    ax_image.axis('off')

    ax_hist.hist(image.ravel(), bins=256, range=[0, 256], color='black')
    ax_hist.set_xlim([0, 256])
    ax_hist.set_title(f'{title} Histogram')

# Load the source and target images in grayscale
source_image = cv2.imread(r"C:\Users\Administrator\Downloads\CV\highcontrast.jpg", cv2.IMREAD_GRAYSCALE)
target_image = cv2.imread(r"C:\Users\Administrator\Downloads\CV\lightimage.jpg", cv2.IMREAD_GRAYSCALE)

# Perform histogram matching
matched_image = exposure.match_histograms(source_image, target_image)

# Create subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 18))

# Plot source image and its histogram
plot_image_and_histogram(source_image, axes[0, 0], axes[0, 1], 'Source Image')

# Plot target image and its histogram
plot_image_and_histogram(target_image, axes[1, 0], axes[1, 1], 'Target Image')

# Plot matched image and its histogram
plot_image_and_histogram(matched_image, axes[2, 0], axes[2, 1], 'Matched Image')

plt.tight_layout()
plt.show()