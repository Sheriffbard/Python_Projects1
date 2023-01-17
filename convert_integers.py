rlist = [ "1", "3", "5"]
def convert_add(list):
    b = []
    for flist in list:
        b.append(int(flist))
    return sum(b)

print(convert_add(rlist))
