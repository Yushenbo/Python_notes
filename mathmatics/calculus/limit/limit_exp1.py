#########################################################################
# File Name: limit.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python

from sympy import *
n = Symbol('n')
print limit((((n + 3)/(n + 2)) ** n), n, oo)

