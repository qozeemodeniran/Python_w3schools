# -*- coding: utf-8 -*-
name = "Qozeem"
age = 26
print(name)
print(age)

print(name, "is", age, "years old.")

fullname, job = "Qozeem Odeniran", "FullStack Developer"
print(fullname, "is a", job)

#USING VARIABLES DECLARED ABOVE AS GLOBAL VARIABLES...
def myDetails():
    new_job = "Senior Developer"
    print(name, "has now become a ", new_job)
myDetails()
