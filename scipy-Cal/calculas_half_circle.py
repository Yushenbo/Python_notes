#-*- coding:utf-8 -*-
#########################################################################
# File Name: calculas_halp_circal.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import numpy as np
from scipy import integrate

def half_circle(x):
    return (1 - x**2) ** 0.5

N = 10000

x = np.linspace(-1, 1, N)

dx = 2.0 / N

y = half_circle(x)

S = dx * np.sum(y[:-1] + y[1:])

# Using trapz 
S2 = np.trapz(y, x) * 2


print("Circle's :", S)

print("S2 :", S2)

#Using quad 
pi_half, err = integrate.quad(half_circle, -1, 1)

S3 = pi_half * 2
print("S3 :", S3)
