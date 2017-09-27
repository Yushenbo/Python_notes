#-*- coding:utf-8 -*-
#########################################################################
# File Name: traitsEnumList.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3


from traits.api import HasTraits, Enum, List

class Items(HasTraits):
    count_list = List([None, 0, 1, 2, 3, "many"])
    count = Enum(values="count_list")



item = Items()
item.count = 2
print(item.count)
item.count = "many"
print(item.count)

item.count_list.append(5)
item.count = 5
item.count
