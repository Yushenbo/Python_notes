#########################################################################
# File Name: matrix_reduce.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python

from sympy import *
x1, x2, x3 = symbols('x1 x2 x3')
a11, a12, a13, a22, a23, a33 = symbols('a11 a12 a13 a22 a23 a33')
m = Matrix([[x1, x2, x3]])
n = Matrix([[a11, a12, a13], [a12, a22, a23], [a13, a23, a33]])
v = Matrix([[x1], [x2], [x3]])

f = m * n * v

print f[0].subs({x1:1, x2:1, x3:1})
