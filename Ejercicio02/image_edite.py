import numpy as np

def get_chanels(img_arr):
    red = img_arr * np.array([1, 0, 0], dtype=np.uint8)
    green = img_arr * np.array([0, 1, 0], dtype=np.uint8)
    blue = img_arr * np.array([0, 0, 1], dtype=np.uint8)
    return red, green, blue

def negative(img_arr):
    return 255 - img_arr