"""
Write a function called user_name that generates a username 

from the user’s email. The code should ask the user to input an 

email and the code should return everything before the @ sign 

as their user name. For example, if someone enters 

ben@gmail.com, the code should return ben as their user 

name.
"""
def user_name():
    email = input("Enter your email address: ")

    username = email.split("@") [0]
    return f'Your default username is, {username}'
print(user_name())
