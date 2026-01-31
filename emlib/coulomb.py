import numpy as np
from .constants import k

def coulomb_1d(q, x):
    return k * q / (x**2)

def coulomb_2d(q, r_vec):
    r = np.linalg.norm(r_vec)
    return k * q * r_vec / (r**3)

def coulomb_3d(q, r_vec):
    r = np.linalg.norm(r_vec)
    return k * q * r_vec / (r**3)