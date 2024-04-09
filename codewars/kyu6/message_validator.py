import re

def is_a_valid_message(message):
    # split string into two lists:
      # one for numbers
      # one for strings
    # if number list is NOT same lenght as string list, return false

    # iterate over numbers list with index
      # iterate over strings list
        #if string length is NOT same as number, return false
    # return true

    string_list = list(filter(None, re.split(r'\d+', message)))
    number_list = list(filter(None, re.split(r'[a-zA-Z]+', message)))
    # print(number_list)
    # print(string_list)

    if not message: return True
    if len(number_list) != len(string_list): return False
    if list(message)[0].isalpha(): return False

    for index in range(len(number_list)):
      print(f'string: {string_list[index]} number: {number_list[index]} ')
      if len(string_list[index]) != int(number_list[index]): 
        return False

    return True  

message = input('Write a message with number of chars: ')

print(is_a_valid_message(message))