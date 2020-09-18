# -*- coding: utf-8 -*-
print("\"A simple python dictionary \"")
thisdict = {"name": "Qozeem Odeniran",
            "ambition": "Fullstact Dev.",
            "age": 26}
print(thisdict)
print()

print("\"Accessing items \"")
name = thisdict["name"]
ambition = thisdict["ambition"]
Age = thisdict["age"]
print(name, "||", ambition, "||", Age)
print()

print("\"Accessing using get() \"")
name = thisdict.get("name")
print(name)
print()

print("\"Changing values \"")
thisdict["age"] = 27
thisdict["ambition"] ="Snr. Developer"
print(thisdict)
print()

print("\"Looping through keys and values using items() \"")
for key, value in thisdict.items():
    print(key, value)
print()

print(" \"Adding item to dictionar\" ")
thisdict["natiolity"] = "Nigerian"
print(thisdict)
print()

print(" \"Nested dictionaries\" ")
myFamily = {
        "firstchild": {
                "name": "Ahmed",
                "age": 32
                },
                
        "secondchild": {
                "name": "Azeezat",
                "age": 30
                },
                
        "thirdchild": {
                "name": "Azeez",
                "age": 28
                },
        
        "fourthchild": {
                "name": "Qozeem",
                "age": 26
                },
        }
print(myFamily)
print()

print(" \"Another way to create nested dict is...\" ")
firstchild = {"name" : "Ahmed Odeniran", "age": 32  }
secondchild = {"name" : "Azeezat Odeniran", "age": 30  }
thirdchild = {"name" : "Azeez Odeniran", "age": 28 }
fourthchild = {"name" : "Qozeem Odeniran", "age": 26  }
myFamily = {"firstchild": firstchild,
            "secondchild": secondchild,
            "thirdchild": thirdchild,
            "fourthchild": fourthchild
            }
print(myFamily)
print()



























































































