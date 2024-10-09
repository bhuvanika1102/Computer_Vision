# 1. Create a 2D matrix of size (8x8) with values 0’s and 1’s and display it as an image
import matplotlib.pyplot as plt
import numpy as np

matrix = np.random.randint(2, size=(8, 8))
plt.imshow(matrix, cmap='binary',interpolation='nearest')
plt.title('Random 8x8 Matrix (0-255)')
plt.show()