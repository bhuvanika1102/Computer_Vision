#a) To apply Fourier Transform to an image and determine the magnitude spectrum.
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft2, fftshift

# Read the image in grayscale
image = cv2.imread(r"E:\7th_Sem _Lab\CV\jerry.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Fourier Transform
f_transform = fft2(image)

# Shift zero frequency component to the center
f_transform_shifted = fftshift(f_transform)

# Calculate the magnitude spectrum
magnitude_spectrum = np.abs(f_transform)
magnitude_spectrum_shifted = np.abs(f_transform_shifted)

# Apply log scale for better visualization
magnitude_spectrum = np.log(1 + magnitude_spectrum)
magnitude_spectrum_shifted = np.log(1 + magnitude_spectrum_shifted)

# Plot the results
plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Magnitude Spectrum (Unshifted)')
plt.imshow(magnitude_spectrum, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Magnitude Spectrum (Shifted)')
plt.imshow(magnitude_spectrum_shifted, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()