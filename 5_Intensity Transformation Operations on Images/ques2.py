#To perform Piecewise-Linear Transformation Functions on images.
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image in grayscale
image = cv2.imread(r"E:\7th_Sem _Lab\CV\jerry.jpg", cv2.IMREAD_GRAYSCALE)

# 1. Contrast Stretching
def contrast_stretching(img, low_in, high_in, low_out, high_out):
    stretched = np.clip((img - low_in) * (high_out - low_out) / (high_in - low_in) + low_out, 0, 255)
    return np.array(stretched, dtype=np.uint8)

# Parameters for Contrast Stretching
low_in, high_in = 50, 200
low_out, high_out = 0, 255
contrast_stretched = contrast_stretching(image, low_in, high_in, low_out, high_out)

# 2. Intensity Level Slicing
def intensity_level_slicing(img, low, high):
    sliced = np.where((img >= low) & (img <= high), 255, 0)
    return np.array(sliced, dtype=np.uint8)

# Parameters for Intensity Level Slicing
low, high = 100, 150
sliced_image = intensity_level_slicing(image, low, high)

# 3. Bit-Plane Slicing
def bit_plane_slicing(img, bit):
    sliced = (img >> bit) & 1
    return np.array(sliced * 255, dtype=np.uint8)

# Parameters for Bit-Plane Slicing
bit_plane = bit_plane_slicing(image, 7)  # Example for the 7th bit plane (most significant bit)

# Plot the results
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Contrast Stretching')
plt.imshow(contrast_stretched, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Intensity Level Slicing')
plt.imshow(sliced_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Bit-Plane Slicing (Bit 7)')
plt.imshow(bit_plane, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
