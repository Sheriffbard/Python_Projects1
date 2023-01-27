register = {'Michael':'yes','John': 'no', 

 'Peter':'yes', 'Mary': 'yes'}

def register_check(reg):
    count = 0
    for i,v in reg.items():
        print(i,v)
        if v == 'yes':
            count += 1
    return 'The number of student present is', count

print(register_check(register))
