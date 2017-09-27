#-*- coding:utf-8 -*-
#########################################################################
# File Name: traitsData.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

from traits.api import HasTraits, CFloat, TraitError

class Person(HasTraits):
    cweight = CFloat(50.0)
    weight = float(50.0)


p = Person()
p.cweight = "90"

print(p.cweight)

try:
    p.weight = "90"
except TraitError as ex:
    print(ex)


