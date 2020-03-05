import cv2
import numpy as np

def adapt(img, ref_white):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

    max_x = np.percentile(img[..., 0], 95)
    max_y = np.percentile(img[..., 1], 95)
    max_z = np.percentile(img[..., 2], 95)
    
    img_white = np.array([max_x, max_y, max_z])

    factor = ref_white / img_white

    img = img * factor * 255
    img = img.astype(np.float32)

    img = cv2.cvtColor(img, cv2.COLOR_XYZ2BGR)
    
    return img

illuminant_table = {
    "a": [1.0985, 1.0000, 0.3558],
    "b": [0.9909, 1.0000, 0.8531],
    "c": [0.9807, 1.0000, 1.1822],
    "e": [1.000, 1.000, 1.000],
    "d50": [0.9642, 1.0000, 0.8251],
    "d55": [0.9568, 1.0000, 0.9214],
    "d65": [0.9504, 1.0000, 1.0888],
    "d75": [0.9496, 1.0000, 1.2261],
    "icc": [0.9642, 1.000, 0.8249],    
}

def white(illuminant='icc'):
    illuminant = illuminant.lower()
    return np.array(illuminant_table[illuminant])