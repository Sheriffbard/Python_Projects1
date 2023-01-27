names = ["kerry", "dickson", "John", "Mary", 

 "carol", "Rose", "adam"]
#returns the lowercase names in a tuple

newlist = []
for name in names:
    if name.islower():
        newlist.append(name.lower())

tuple_name = tuple(newlist)
print(tuple_name)
