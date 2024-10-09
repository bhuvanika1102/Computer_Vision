# 2.Create a 2D matrix of size (8x8) with random values of 0 to 255 and display it as an image.
import matplotlib.pyplot as plt
import numpy as np

matrix = np.random.randint(0, 256, size=(8, 8))
plt.imshow(matrix, cmap='gray', vmin=0, vmax=255, interpolation='nearest')
plt.title('Random 8x8 Matrix (0-255)')
plt.show()