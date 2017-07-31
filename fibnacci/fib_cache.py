#-*- coding:utf-8 -*-
#########################################################################
# File Name: fib.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python

from sys import argv

def fib(n, cache = None):
    if cache == None:
        cache = {}
    if n < 2:
        return 1
    if not n in cache:
        cache[n] =  fib(n-1, cache) + fib(n-2, cache)

    return cache[n]


print(fib(int(argv[1])))
