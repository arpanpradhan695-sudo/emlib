import numpy as np
from .constants import mu_0
import math

def biot_savart_1d(I, r):
    return mu_0 * I / (2 * math.pi * r)

def biot_savart_2d(I, dl_vec, r_vec):
    r = np.linalg.norm(r_vec)
    return (mu_0 / (4 * math.pi)) * I * np.cross(dl_vec, r_vec) / (r**3)

def biot_savart_3d(I, dl_vec, r_vec):
    r = np.linalg.norm(r_vec)
    return (mu_0 / (4 * math.pi)) * I * np.cross(dl_vec, r_vec) / (r**3)