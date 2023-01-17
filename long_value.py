fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(fruity):
    longest = max(fruity.values(), key=len)
    return longest
print(longest_value(fruits))
