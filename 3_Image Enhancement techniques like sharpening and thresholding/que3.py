#To perform image segmentation using simple, adaptive and Otsu thresholding methods.
# import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = r"C:\Users\bhuva\Downloads\CV\jerry.jpg"
image = cv2.imread(image_path, 0)
if image is None:
    print(f"Error: Could not open or read the image at {image_path}")
else:
    _, simple_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    _, otsu_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    ax1.imshow(simple_threshold, cmap='gray')
    ax1.set_title('Simple Thresholding')
    ax1.axis('off')
    ax2.imshow(adaptive_threshold, cmap='gray')
    ax2.set_title('Adaptive Thresholding')
    ax2.axis('off')
    ax3.imshow(otsu_threshold, cmap='gray')
    ax3.set_title("Otsu's Thresholding")
    ax3.axis('off')
    plt.tight_layout()
    plt.show()
    cv2.imwrite('simple_threshold.jpg', simple_threshold)
    cv2.imwrite('adaptive_threshold.jpg', adaptive_threshold)
    cv2.imwrite('otsu_threshold.jpg', otsu_threshold)