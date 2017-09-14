#-*- coding:utf-8 -*-
#########################################################################
# File Name: example.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python

from enthought.traits.api import Delegate, HasTraits, Instance, Int, Str

class Parent(HasTraits):
    last_name = Str('Shen')


class Child(HasTraits):
    age = Int

    father = Instance(Parent)

    last_name = Delegate('father')


    def _age_changed(self, old, new):
        print('Age changed from %s to %s'%(old, new))


p = Parent()
c = Child()

c.father = p

print(p.last_name)
print(c.last_name)

c.age = 4

print(c.configure_traits())
