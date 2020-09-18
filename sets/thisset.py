# -*- coding: utf-8 -*-
print("\"A simple python set \"")
thisset = {"set1", "set2", "set3"}
print(thisset)
print()

print("\"Adding item(s) to a set with add() and/or update() \"")
print("\"the add() adds one item \"")
thisset.add("set4")
print(thisset)
print("\"the update() add more than one items \"")
thisset.update(["set5", "set6"])
print(thisset)
print()

print("\"Joining two set using union() \"")
thisset2 = {"newste1", "newset2"}
thisset3 = thisset.union(thisset2)
print(thisset3)
print()




















