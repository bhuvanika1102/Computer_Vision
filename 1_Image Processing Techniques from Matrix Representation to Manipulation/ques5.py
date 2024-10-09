# 5. Display the image dimension.
import cv2


def display_image_dimensions(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image file '{image_path}'.")
        return
    height, width, channels = image.shape
    print(f"Image dimensions for '{image_path}':")
    print(f"- Width  : {width} pixels")
    print(f"- Height : {height} pixels")
    print(f"- Channels: {channels}")
image_path = r"C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-07-10 110729.png"

display_image_dimensions(image_path)

