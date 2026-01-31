import numpy as np
from .constants import epsilon_0, mu_0


def gauss_electric_1d(rho):
    return rho / epsilon_0

def gauss_electric_2d(div_E, rho):
    return div_E - rho / epsilon_0

def gauss_electric_3d(div_E, rho):
    return div_E - rho / epsilon_0




def gauss_magnetic_1d():
    return 0.0

def gauss_magnetic_2d():
    return 0.0

def gauss_magnetic_3d():
    return 0.0



def faraday_1d(dB_dt):
    return -dB_dt

def faraday_2d(curl_E_z, dB_dt):
    return curl_E_z + dB_dt

def faraday_3d(curl_E, dB_dt):
    return curl_E + dB_dt



def ampere_maxwell_1d(J, dE_dt):
    return mu_0 * J + mu_0 * epsilon_0 * dE_dt

def ampere_maxwell_2d(curl_B_z, J_z, dE_dt_z):
    return curl_B_z - (mu_0 * J_z + mu_0 * epsilon_0 * dE_dt_z)

def ampere_maxwell_3d(curl_B, J, dE_dt):
    return curl_B - (mu_0 * J + mu_0 * epsilon_0 * dE_dt)