# 4.Separate the channels of an RGB image and display.
import cv2
import matplotlib.pyplot as plt

rgb_image = cv2.imread(r'C:\Users\Administrator\Documents\21BAD006\rgb.jpg', cv2.IMREAD_COLOR)
rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

# Separate channels
red_channel = rgb_image[:,:,0]
green_channel = rgb_image[:,:,1]
blue_channel = rgb_image[:,:,2]

# Display each channel separately
plt.figure(figsize=(12, 4))

plt.subplot(1, 4, 1)
plt.imshow(rgb_image)
plt.title('RGB Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(red_channel, cmap='gray')
plt.title('Red Channel')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(green_channel, cmap='gray')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(blue_channel, cmap='gray')
plt.title('Blue Channel')
plt.axis('off')

plt.show()