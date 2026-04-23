import numpy as np
from scipy.interpolate import RegularGridInterpolator
import cairosvg
from PIL import Image
import io

# --- Step 1: SVG → 2D heightmap array ---
png_data = cairosvg.svg2png(url="pattern.svg", output_width=1024, output_height=1024)
img = Image.open(io.BytesIO(png_data)).convert("L")  # grayscale
heightmap = np.array(img) / 255.0  # 0.0 to 1.0

# --- Step 2: Build interpolator over the heightmap ---
u = np.linspace(0, 1, heightmap.shape[1])
v = np.linspace(0, 1, heightmap.shape[0])
sampler = RegularGridInterpolator((v, u), heightmap, method="linear", bounds_error=False, fill_value=0)

# --- Step 3: Toroid UV parameterization ---
# Toroid: R = major radius, r = minor radius
# vertices shape (N, 3)
def toroid_uv(vertices, R, r):
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
    theta = np.arctan2(y, x)                          # around main ring
    cx = R * np.cos(theta)
    cy = R * np.sin(theta)
    phi = np.arctan2(z, np.sqrt(x**2 + y**2) - R)    # around tube
    u = (theta / (2 * np.pi)) % 1.0
    v = (phi   / (2 * np.pi)) % 1.0
    return np.stack([u, v], axis=1)

uv = toroid_uv(vertices, R=50, r=10)

# --- Step 4: Sample displacement at each vertex ---
displacement = sampler(uv[:, [1, 0]])  # note: interpolator is (v, u)

# --- Step 5: Displace along vertex normals ---
emboss_depth = 2.0  # mm
new_vertices = vertices + normals * (displacement * emboss_depth)[:, np.newaxis]
