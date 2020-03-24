import numpy as np
from fractions import Fraction

v1 = np.array([0, 1, -1])
v2 = np.array([1, 0, 1])
v3 = np.array([1, 1, 1])

def unitVector (vector):
    return vector / np.linalg.norm(vector)

def proj1 (x, f1):
    return (np.vdot(x, f1)) * f1

def proj2 (x, f1, f2):
    return np.vdot(x, f1) * f1 + np.vdot(x, f2) * f2

e1 = unitVector(v1)
e2 = unitVector(v2 - proj1(v2, e1))
e3 = unitVector(v3 - proj2(v3, e1, e2))

print(e1, e2, e3)
