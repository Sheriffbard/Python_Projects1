fruits = ['apple', 'orange', 'banana', 'apple']

names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicates(flist):
    for item in flist:
        if flist.count(item) > 1:
            return item
        else:
            return "no duplicates"

print(check_duplicates(fruits))
print(check_duplicates(names))
