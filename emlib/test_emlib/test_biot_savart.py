import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from emlib.biot_savart import (
    biot_savart_1d,
    biot_savart_2d,
    biot_savart_3d
)

print("=== BIOT–SAVART TESTS ===")

I = 5.0  


r = 0.1
B1 = biot_savart_1d(I, r)
print("1D Magnetic Field:", B1, "Tesla")


dl2 = np.array([0.0, 0.01])
r2 = np.array([0.1, 0.0])
B2 = biot_savart_2d(I, dl2, r2)
print("2D Magnetic Field:", B2, "Tesla")


dl3 = np.array([0.0, 0.0, 0.01])
r3 = np.array([0.1, 0.0, 0.0])
B3 = biot_savart_3d(I, dl3, r3)
print("3D Magnetic Field:", B3, "Tesla")