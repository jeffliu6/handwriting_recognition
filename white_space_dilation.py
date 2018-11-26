import cv2
import numpy as np


def horizontal_dilation(img):
    r, c = img.shape
    parts = []
    for i in range(c):
        pixel_vals = img[:,i]
        parts.append(pixel_vals)
        if min(pixel_vals) > 200: # All white space? 200 is arbitrary
            parts.append(pixel_vals)
    return np.transpose(np.asarray(parts))
