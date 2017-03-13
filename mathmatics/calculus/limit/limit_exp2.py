#########################################################################
# File Name: limit_exp2.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python

from sympy import *
x = Symbol('x')
print limit(1/x**2, x, 0)
#result
#oo
print limit(x*(sqrt(x**2 + 1) - x), x, oo)
#result
#1/2
