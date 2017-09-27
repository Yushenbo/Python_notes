#-*- coding:utf-8 -*-
#########################################################################
# File Name: traitsListener.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

from traits.api import HasTraits, Str, Int

class Child(HasTraits ):
    name = Str
    age = Int
    doing = Str

    def __str__(self):
        return "%s<%x>" %(self.name, id(self))

    # Below funciton will be called when property age have been modified

    def  _age_changed(self, old, new):
        print("%s.age changed: from %s to %s" %(self, old, new))


    def _anytrait_changed(self, name, old, new):
        print("anytrait changed: %s.%s from %s to %s" %(self, name, old, new))


def log_trait_changed(obj, name, old, new):
    print("log: %s.%s changed from %s to %s "%(obj, name, old, new))


h = Child(name = "Jack", age = 9)
k = Child(name = "Bob", age = 9)

h.on_trait_change(log_trait_changed, name = "doning")


h.age = 10

h.doing = "sleeping"

k.doing = "playing"

