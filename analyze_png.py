from PIL import Image
import numpy as np

file = "door_of_durin.png"

# Open the image and convert it to 'L' mode (8-bit grayscale)
image = Image.open(file).convert('L')

# Convert the Image object to a NumPy array
grayscale_values = np.asarray(image)

print(f"Image shape: {grayscale_values.shape}") # Will output a 2D shape, e.g., (height, width)
print(f"Pixel value at (10, 20): {grayscale_values[10, 20]}") # Access a specific pixel