import numpy as np

def cartesian_to_spherical(x, y, z):
    # Calculate radius (r)
    r = np.hypot(np.hypot(x, y), z)
    
    # Calculate azimuth angle (theta) in radians [-pi, pi]
    theta = np.arctan2(y, x)
    
    # Calculate inclination angle (phi) from the z-axis [0, pi]
    # Use hypot(x, y) to get the distance in the xy plane
    phi = np.arctan2(np.hypot(x, y), z)
    
    return r, theta, phi

