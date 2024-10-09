#To adjust the brightness and contrast of the images to enhance the visual appeal and effectiveness. 
import cv2
import matplotlib.pyplot as plt

image_path = r"E:\7th_Sem _Lab\CV\tom.jpg"
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not open or read the image at {image_path}")
else:
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 30    # Brightness control (0-100)
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imshow('Original Image', image)
cv2.imshow('Edges', adjusted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()