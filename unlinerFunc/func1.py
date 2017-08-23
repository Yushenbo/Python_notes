#-*- coding:utf-8 -*-
#########################################################################
# File Name: func1.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python
# scipy lib fsolve solve unlinear function set

from scipy.optimize import fsolve
from math import sin,cos

def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])

    return [
            5 * x1 + 3,
            4 * x0 * x0 - 2 * sin(x1 * x2),
            x1  * x2 - 1.5
            ]

result = fsolve(f, [1, 1, 1])

print(result)
print(f(result))


