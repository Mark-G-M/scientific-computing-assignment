import numpy as np
from scipy.integrate import dblquad

# Define the function z = x^2 + y^2
def surface_function(y, x):
    return x**2 + y**2

# Integration limits: x from 0 to 1, y from 0 to 1
volume, error = dblquad(surface_function, 0, 1, lambda x: 0, lambda x: 1)

print("Volume under the surface:", volume)
