# -*- coding: utf-8 -*-
print("\"This is a simple list\"")
thislist =["item1", "item2", "item3", "item4", "item5", "item6", 
           "item7","item8"]
print(thislist)
print()

print("\"Accessing the list item using index-number\"")
print(thislist[0])
print(thislist[1])
print(thislist[2])
print()

print("\"Negative indexing\"")
print(thislist[-1])
print(thislist[-2])
print(thislist[-3])
print()

print("\"Range of indexes - slicing\"")
print("\"returns 3rd,4th and 5th items\"")
print(thislist[2:5])
print("\"returns items from 1st item to the 4th item\"")
print(thislist[:4])
print("\"return item from 3rd to last item\"")
print(thislist[2:])
print()

print("\"Negative range indexes\"")
print("\"returns -4th item to -2th item\"")
print(thislist[-4:-1])
print()

print("\" Changing item value\"")
print("\"changes 'item1' to 'newitem1'\"")
thislist[0] = "newitem1"
print(thislist)
print()

print("\"Loopint through a list\"")
for items in thislist:
    print(items)
print()

print("\"Check if item exists \"")
if "item7" in thislist:
    print("Yes, 'item7' is in ", thislist)
else:
    print("item not found!")
print()

print("\"NUmber of items in the list using len() function \"")
print(len(thislist))
print()

print("\"Adding item to the end of a list using append() \"")
thislist.append("enditem")
print(thislist)
print()

print("\"Insert item in a specified index using insert() \"")
thislist.insert(3, "inserteditem")
print(thislist)
print()

print("\"Remove item using remove()  \"")
print("\"removes item6 from the list \"")
thislist.remove("item6")
print(thislist)
print()

print("\"Removing items with pop() \"")
print("\"removes item5 \"")
thislist.pop(4)
print(thislist)
print()

print("\"Deleting item using del keyword \"")
print("\"deletes the 3rd item \"")
del thislist[2]
print(thislist)
#print("\"deletes the list completely \"")
#del thislist
#print(thislist)
print()

#print("\"Emptying the list using clear() method \"")
#thislist.clear()
#print(thislist)

print("\"Making a copy of a list using copy() \"")
thatlist = thislist.copy()
print(thatlist)
print()

print("\"Making a list copy using list() \"")
anotherlist = list(thislist)
print(anotherlist)
print()

print("\"Joing two list using + \"")
pluslist = ["plus1", "plus2", "plus3","plus4"]
plus_this_list = pluslist + thislist
print(plus_this_list)
print()

print("\"Joing two lists by appending each item of a list\"")
for lst in pluslist:
    thislist.append(lst)
print(thislist)
print()

print("\"Joing two list using extend() \"")
thislist.extend(pluslist)
print(thislist)
print()

print("\"Making new list with list() constructor \"")
thislist = list(("construct1", "construct2", "construct3"))
print(thislist)
print()












































































