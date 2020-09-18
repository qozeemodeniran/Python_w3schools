# -*- coding: utf-8 -*-

num01 = x
num02 = 1.01
num03 = 1j
num04 = 3e45

print(type(num01))
print(type(num02))
print(type(num03))
print(type(num04))

#Type conversion
num02 = int(num02)
print(type(num02))

#Random Number
import random
print(random.randrange(0, 9))