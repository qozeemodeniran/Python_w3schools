# -*- coding: utf-8 -*-
print("Qozeem")
salutation = "Hello"
print(salutation)
age = 26
address = 34
about = """My name is Qozeem Odeniran.
I am {} years old.
I am a developer and
I love what I do. """
print(about)
print(about[0:10])
print(about[-5:-2])
print(len(about))
print(about.strip())
print(about.lower())
print(about.upper())
print(about.replace("Qozeem", "Azeez"))
new_about = print(about.split(" "))
name = "Qozeem Odeniran" in about
print(name)
name2 = "Azeez Odeniran" not in about
print(name2)
print(salutation + ", " + about.format(age))
new_about = """Hello, My name is Qozeem Odeniran.
I am {} years old. I reside at {}, Fako Street
Ogba Lagos Nigeria.
"""
print(salutation + new_about.format(age, address))

