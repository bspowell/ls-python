# given a string of words
# each word will contain a number
# that number determines what position it's placed in the result string
# if empty string, return empty string

# given a string
# break into word list 
# make a copy of that word list
# for each word, grab the number within it
# use it to place the word in the new copied list with that index

import re

def order(sentence):
    curr_list = sentence.split(' ')     # creates a list of words
    order_list = re.findall(r'\d', sentence) # creates a list of each digit found
    new_list = [ None ] * len(order_list)    # creates a list of same size with None
    
    for index in order_list:
        new_list[int(index) - 1] = curr_list.pop(0) # adds 
    return ' '.join(new_list)

print(order("is2 Thi1s T4est 3a")),# "Thi1s is2 3a T4est"))
print(order("4of Fo1r pe6ople g3ood th5e the2")),# "Fo1r the2 g3ood 4of th5e pe6ople"))
print(order("")),# ""))