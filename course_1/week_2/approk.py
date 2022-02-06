import numpy as np
import scipy as sc
from math import *
from scipy import linalg


def fun(x):
    f = sin(x/5) * exp(x/10) + 5 * exp(-x/2)
    return f

A = np.array([[1, 1, 1, 1],[1, 4, 16, 64],[1, 10, 100, 1000],[1, 15, 225, 3375]])
b = np.array([1, 4, 10, 15])
b3 = []
for el in b:
    b3.append(fun(el))
print(b3)

f1 = linalg.solve(A, b3)
print(f1)


