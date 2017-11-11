#########################################################################
# File Name: equation.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python

from sympy import *

x = Symbol('x')

print(solve(x * 2 - 4, x))

