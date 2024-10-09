# # 7. Perform image rotation and image flipping.


# img_cw_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# img_ccw_90 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

import cv2

image_path = r"C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-07-10 110729.png"
image = cv2.imread(image_path)
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
flipped_horizontal = cv2.flip(image, 1)
flipped_vertical = cv2.flip(image, 0)
cv2.imshow('Original', image)
cv2.imshow('Rotated', rotated_image)
cv2.imshow('Flipped Horizontal', flipped_horizontal)
cv2.imshow('Flipped Vertical', flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()