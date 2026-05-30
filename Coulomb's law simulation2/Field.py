import numpy as np
from numpy.typing import NDArray

k = 9 * 10**9

def ElectricField(q: float,
                  x: NDArray,
                  y: NDArray,
                  x0: float,
                  y0: float) -> tuple[NDArray, NDArray]:

    dx = x - x0
    dy = y - y0

    r = np.sqrt(dx ** 2 + dy ** 2)
    r = np.maximum(r, 1e-9)

    Ex = k * q * (x-x0) /(r**3)
    Ey = k * q * (y-y0) /(r**3)

    return Ex, Ey

def Potential(q: float,
                  x: NDArray,
                  y: NDArray,
                  x0: float,
                  y0: float) -> tuple[NDArray, NDArray]:

    dx = x - x0
    dy = y - y0

    r = np.sqrt(dx ** 2 + dy ** 2 + 0.2**2)
    r = np.maximum(r, 1e-9)

    return k * q / r




