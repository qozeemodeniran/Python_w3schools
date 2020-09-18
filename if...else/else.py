# -*- coding: utf-8 -*-
age = 19
 
if age < 18:
     print("You cannot drive")

elif age == 18:
    print("You can learn to drive")
    
else:
    print("You can drive on your own.")

print()
#shorthand if...else
print("Not good to go") if age < 19 else print("Good to go")