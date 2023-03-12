#!/usr/bin/python3

#num = (12.1, 3)
"""Write a function called only_floats, which takes two 

parameters a and b, and returns 2 if both arguments are floats,

returns 1 if only one argument is a float, and returns 0 if neither 

argument is a float. If you pass (12.1, 23) as an argument, your 

function should return a 1"""

def only_float (a, b):
    if type(a) and type(b) == float:
        return 2
    if type(a) or type(b) == float:
        return 1
    if type(a) and type(b) != float:
        return 0

print(only_float(12.1, 23))
print(only_float(12.3, 23.1))
