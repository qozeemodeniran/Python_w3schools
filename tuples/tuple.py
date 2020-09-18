# -*- coding: utf-8 -*-
print("\"A simple pyhton tuple \"")
thistuple = ("tuple1", "tuple2", "tuple3")
print(thistuple)
print()

print("\"Accessing tuples \"")
print(thistuple[2]) 
print(thistuple[1]) 
print()

print("\"Chaning tuple values: first, convert the tuple to a..\"")
print("\"list. Then, change the list. And finally, covert the...\"")
print("\"listback to tuple. \"")
tuple2list = list(thistuple)
tuple2list[0] = "changedtuple1"
thistuple = tuple(tuple2list)
print(thistuple)
print()

print(thistuple.count("tuple1"))
print(thistuple.index("tuple3"))








































