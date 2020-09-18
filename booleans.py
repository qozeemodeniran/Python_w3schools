# -*- coding: utf-8 -*-
print("\"Boolean statement\"")
print(10>5)
print(10 == 9)
print(10 < 9)
print()


print("\"Printing a statement based on if-condition\"")
a = 100
b = 3
if(b > a):
    print("b is greater than a\n")
else:
    print("b is not greater than a")
print()


print("\"Most statement evaluates to true\"")
print(bool("Hello"))
print(bool(15))
print()


print("\"Most variabales evaluates to true\"")
x = "hello"
y = 15
print(bool(x))
print(bool(y))
print()

print("\"functions with zero return value evaluates to false\"")
class myClass():
    def __len__(self):
        return 0
myobj = myClass()
print(bool(myobj))
print()

print("\"functions can return a boolean\"")
def returnBoolean():
    return True
print(returnBoolean())
print()

print("\"execute code based on boolean answer of a function\"")
def myFunction():
    return True
if myFunction():
    print("YES")
else:
    print("NO")
print()

print("\"the isinstance() function\"")
x = 100
print(isinstance(x, int))
print()



















