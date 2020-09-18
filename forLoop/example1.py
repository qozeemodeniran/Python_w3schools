# -*- coding: utf-8 -*-
names = ["Qozeem", "Banji", "Odeniran"]

for name in names:
    print(name)

print("")

for letter in names[0]:
    print(letter)

print("")

""" -Breaking after 'Banji'
exit the loop @ name is Banji
using the break-statement"""
for name in names:
    print(name)
    
    if name == "Banji":
        break
    
print("")
""" -Breaking before Banji
exit the loop @ before name=Banji"""
for name in names:
    if name == "Banji":
        break
    
    print(name)

