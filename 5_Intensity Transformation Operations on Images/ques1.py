#To perform commonly used intensity transformations on images
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image in grayscale
image = cv2.imread(r"E:\7th_Sem _Lab\CV\jerry.jpg", cv2.IMREAD_GRAYSCALE)

# 1. Image Negatives (Linear)
image_negative = 255 - image

# 2. Log Transformations
c = 255 / np.log(1 + np.max(image))
log_transformed = c * np.log(1 + image)
log_transformed = np.array(log_transformed, dtype=np.uint8)

# 3. Power-Law (Gamma) Transformations
gamma = 0.5  # Example gamma value
gamma_corrected = np.array(255 * (image / 255) ** gamma, dtype=np.uint8)

# Plot the results
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Image Negative')
plt.imshow(image_negative, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Log Transformation')
plt.imshow(log_transformed, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Gamma Correction')
plt.imshow(gamma_corrected, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()