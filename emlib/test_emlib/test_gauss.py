import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from emlib.gauss import gauss_1d, gauss_2d, gauss_3d
from emlib.maxwell import gauss_electric_1d

print("=== GAUSS LAW TESTS ===")

Q = 1e-9  


print("Gauss 1D Flux:", gauss_1d(Q))
print("Gauss 2D Flux:", gauss_2d(Q))
print("Gauss 3D Flux:", gauss_3d(Q))


rho = 1e-6
print("Gauss Electric (Differential):", gauss_electric_1d(rho))