#!/usr/bin/python3

"""a function called word_index that takes one argument, 

a list of strings and returns the index of the longest word in the 

list. If there is no longest word (if all the strings are of the same 

length), the function should return zero (0)"""

def word_index (list1):
    for word in list1:
        
            if len(list1[word]) == len(list1[word + 1]):
           
                return 0
            elif len(word) == len(max(list1)):
            
                return list1.index(word)

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

#call function

print(word_index(words1))
print(word_index(words2))

