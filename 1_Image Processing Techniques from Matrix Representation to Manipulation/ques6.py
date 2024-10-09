# 6. Crop, resize the image to a specific dimension.

import cv2

image_path = r"C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-07-10 110729.png"
image = cv2.imread(image_path)
x, y, w, h = 100, 100, 300, 200
cropped_image = image[y:y+h, x:x+w] 
desired_width = 400
desired_height = 300
resized_image = cv2.resize(cropped_image, (desired_width, desired_height))

cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()