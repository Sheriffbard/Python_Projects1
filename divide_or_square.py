def divide_or_sq(num):
    if num % 5 == 0:
        return num ** 0.5
    else:
        return num % 5

print(divide_or_sq(10))
