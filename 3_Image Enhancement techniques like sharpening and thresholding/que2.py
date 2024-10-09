#To perform image sharpening to enhance the edges and fine details in an image.
#To perform image sharpening to enhance the edges and fine details in an image.
import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = r"E:\7th_Sem _Lab\CV\tom.jpg"
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not open or read the image at {image_path}")
else:
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Edges', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()