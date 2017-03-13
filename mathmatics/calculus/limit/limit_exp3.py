#########################################################################
# File Name: limit_exp3.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python

from sympy import *
n = Symbol('n')
s = ((n + 3)/(n + 2))**n
print limit(s, n, oo)
#result
#E
