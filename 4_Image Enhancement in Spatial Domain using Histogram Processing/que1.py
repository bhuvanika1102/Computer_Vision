#To verify the histograms of dark, light, low contrast and high contrast images. 
import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_image_and_histogram(image, ax_image, ax_hist, title):
    ax_image.imshow(image, cmap='gray')
    ax_image.set_title(title)
    ax_image.axis('off')

    ax_hist.hist(image.ravel(), bins=256, range=[0, 256], color='black')#2d-1d
    ax_hist.set_xlim([0, 256])
    ax_hist.set_title(f'{title} Histogram')

# Load the images
dark_image = cv2.imread(r"C:\Users\Administrator\Downloads\CV\darkimage.jpg", cv2.IMREAD_GRAYSCALE)
light_image = cv2.imread(r"C:\Users\Administrator\Downloads\CV\lightimage.jpg", cv2.IMREAD_GRAYSCALE)
low_contrast_image = cv2.imread(r"C:\Users\Administrator\Downloads\CV\lowcontrast.jpg", cv2.IMREAD_GRAYSCALE)
high_contrast_image = cv2.imread(r"C:\Users\Administrator\Downloads\CV\highcontrast.jpg", cv2.IMREAD_GRAYSCALE)

# Create subplots
fig, axes = plt.subplots(4, 2, figsize=(12, 18))

# Plot images and histograms
plot_image_and_histogram(dark_image, axes[0, 0], axes[0, 1], 'Dark Image')
plot_image_and_histogram(light_image, axes[1, 0], axes[1, 1], 'Light Image')
plot_image_and_histogram(low_contrast_image, axes[2, 0], axes[2, 1], 'Low Contrast Image')
plot_image_and_histogram(high_contrast_image, axes[3, 0], axes[3, 1], 'High Contrast Image')

plt.tight_layout()
plt.show()