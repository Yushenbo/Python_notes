#########################################################################
# File Name: diff_equa_exp1.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python

from sympy import *
f = Function('f')
x = Symbol('x')
print dsolve(diff(f(x), x) - 2*f(x)*x, f(x))


