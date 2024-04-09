# given a number
  # have an array global constant with every number 0-10 in string format
  # use another function to return name of numbers
    # split number into a list using list()
    # map over list, change each number based on the relevant string in the array
    # combine all numbers written in strings together
    # return combined form - 'onetwo' = 12
  # count length of string returned -
    # while loop
      # pass integer to function
      # if string returned is equal to length, stop
      # if not, add number to array

ALPHA = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_name(num):
  num_list = str(num)
  digits_list = list(map(lambda x: ALPHA[int(x)], num_list))
  digits_string = "".join(digits_list)
  return digits_string

def numbers_of_letters(n):
  num_word = get_name(n)
  num_list = [num_word]
  while len(num_word) != n:
    n = len(num_word)
    num_word = get_name(n)
    num_list.append(num_word)
  return num_list

numbers_of_letters(12)#, ["onetwo", "six", "three", "five", "four"]
numbers_of_letters(1)#, ["one", "three", "five", "four"]
numbers_of_letters(37)#, ["threeseven", "onezero", "seven", "five", "four"]
numbers_of_letters(311)#, ['threeoneone', 'oneone', 'six', 'three', 'five', 'four']
numbers_of_letters(999)#, ["nineninenine", "onetwo", "six", "three", "five", "four"]