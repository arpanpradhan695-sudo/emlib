import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from emlib.coulomb import coulomb_1d, coulomb_2d, coulomb_3d

print("=== COULOMB LAW TESTS ===")

q = 1e-9   


x = 1.0
E1 = coulomb_1d(q, x)
print("1D Electric Field:", E1, "N/C")


r2 = np.array([1.0, 0.0])
E2 = coulomb_2d(q, r2)
print("2D Electric Field:", E2, "N/C")


r3 = np.array([1.0, 0.0, 0.0])
E3 = coulomb_3d(q, r3)
print("3D Electric Field:", E3, "N/C")