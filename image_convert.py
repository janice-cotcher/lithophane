from PIL import Image
import numpy as np
# from PIL.ExifTags import TAGS
from scipy import ndimage
import matplotlib.pyplot as plt

# Open the image
img = Image.open("cow.png").convert("L")


# Convert to a binary array using a threshold (e.g., 128)
greys = []
binary_array = np.array(img)
# rows = binary_array.shape[0]
# columns = binary_array.shape[1]
sections = [[49, 73],
[73, 177],
[177, 189],
[189, 360],
[360, 424],
[424, 630],
[630, 692],
[692, 716],
[716, 732],
[732, 752]]
greys = []
for section in sections:
    start = section[0]
    stop = section[1]
    submatrix = binary_array[start:stop]
    grey = np.where(submatrix < 128)
    greys.append(grey)


print(greys[0][0])
print(binary_array[49:73])


