#!/usr/bin/python3

"""
a function called my_discount. The function takes no 

arguments but asks the user to input the price and the 

discount (percentage) of the product. Once the user inputs the 

price and discount, it calculates the price after the discount. 

The function should return the price after the discount. 
"""

def my_discount():

    cp = float(input("Enter your price: ")) 
    #cp = customer price

    dp = float(input("Enter your discount percentage: (Note: Your percentage should be an integer 1, 20, 15 etc "))

    pp = dp / 100
    pad = cp * (1 - pp)

    return pad


print(my_discount())
