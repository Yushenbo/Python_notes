#-*- coding:utf-8 -*-
#########################################################################
# File Name: fib.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python

from sys import argv

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(int(argv[1])))
