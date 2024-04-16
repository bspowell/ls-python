# Use recursion to write a function that accepts a string and 
# returns the first index that contains the character “x.” 
# For example, the string, "abcdefghijklmnopqrstuvwxyz" has an 
# “x” at index 23. To keep things simple, assume the string
#  definitely has at least one “x.”

def x_index(str, count=0):
  if str[0] == 'x':
    return count
  else:
    count+=1
  return x_index(str[1:], count)

print(x_index("abcdefghijklmnopqrstuvwxyz")) #23
