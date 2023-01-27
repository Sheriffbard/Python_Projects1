register = {'Michael':'yes','John': 'no', 

 'Peter':'yes', 'Mary': 'yes'}

def register_check(reg):
    count = 0
    for i in reg:
        if i.values() == 'yes':
            count += 1
    return count

print(register_check(register))
