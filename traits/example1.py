#-*- coding:utf-8 -*-
#########################################################################
# File Name: example1.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python

from traits.api import HasTraits, Color

class Circle(HasTraits):
    color = Color


c = Circle()
print(c.color)

