import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from emlib.maxwell import (
    gauss_electric_1d,
    gauss_magnetic_3d,
    faraday_1d,
    faraday_3d,
    ampere_maxwell_1d,
    ampere_maxwell_3d
)

print("=== MAXWELL EQUATIONS TESTS ===")


rho = 1e-6
print("Gauss Electric 1D:", gauss_electric_1d(rho))


print("Gauss Magnetic 3D:", gauss_magnetic_3d())


dB_dt = 0.02
print("Faraday 1D:", faraday_1d(dB_dt))

curl_E = np.array([0.0, 0.0, -0.02])
print("Faraday 3D:", faraday_3d(curl_E, dB_dt))


J = 2.0
dE_dt = 0.01
print("Ampere-Maxwell 1D:", ampere_maxwell_1d(J, dE_dt))

curl_B = np.array([0.1, 0.0, 0.0])
print("Ampere-Maxwell 3D:", ampere_maxwell_3d(curl_B, J, dE_dt))