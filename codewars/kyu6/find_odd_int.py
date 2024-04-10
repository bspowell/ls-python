# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

# given an array
# create a dictonairy object
# iterate over the list
#   check if dict has number as a key
#     if yes, + 1 to the keys value
#     if no, add key and value of 1 to object
# iterate over keys and return one with an odd value

def find_it(seq):
  obj = {}
  for num in seq:
    if num in obj:
      obj[num] += 1
    else:
      obj[num] = 1
  for key in obj.keys():
    if obj[key] % 2 != 0: return key

  return 0

print(find_it([7])) # should return 7, because it occurs 1 time (which is odd).
print(find_it([0])) # should return 0, because it occurs 1 time (which is odd).
print(find_it([1,1,2])) # should return 2, because it occurs 1 time (which is odd).
print(find_it([0,1,0,1,0])) # should return 0, because it occurs 3 times (which is odd).
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])) # should return 4, because it appears 1 time (which is odd).