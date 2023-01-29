#!/usr/bin/python3

"""
a function called my_discount. The function takes no 

arguments but asks the user to input the price and the 

discount (percentage) of the product. Once the user inputs the 

price and discount, it calculates the price after the discount. 

The function should return the price after the discount. 
"""

def my_discount():

    cp = input("Enter your price: ")  #cp = customer price

    dp = input("Enter your discount percentage: ")

    if type(dp) == float: #dp = discount percent

        pad = (cp - (1 - dp)) #pad = price after discount
        print(pad)
    elif type(dp) == int:
        con_dp = (dp / 100)
        pad = (cp - (1 - dp))
        print(pad)

    else:
        print("Error input, check your percentage format, e.g 25% or 0.25")

print(my_discount())
