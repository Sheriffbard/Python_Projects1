""" Write a function called zeroed code that takes a list of numbers 

as an argument. The code should zero (0) the first and the last 

number in the list. """

list1 = [2, 1, 4, 6, 3, 5, 9, 8]
def zeroed(num_list):

    num_list[0] = 0

    num_list[-1] = 0

    print(num_list)

zeroed(list1)


