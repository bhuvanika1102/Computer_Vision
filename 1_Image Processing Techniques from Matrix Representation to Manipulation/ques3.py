# 3.Read images (Gray scale, Binary, RGB) and display. Also, interpret the pixel values
import cv2
import matplotlib.pyplot as plt

rgb_image = cv2.imread(r'C:\Users\Administrator\Documents\21BAD006\tom.png', cv2.IMREAD_COLOR)
rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

plt.imshow(rgb_image)
plt.title('RGB Image')
plt.axis('off')
plt.show()