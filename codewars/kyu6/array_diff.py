# implement a difference function
# subtract one list from another and return the result
# you should remove all the values from list A which are present in list B
# keep same order

# eg. array_diff([1,2],[1]) == [2]
# eg. array_diff([1,2,2,2,3],[2]) == [1,3]

# given two lists
#   iterate over the second list
#   while num exists in first list
#     remove number from first list
def array_diff(a, b):
    for num in b:
      while num in a:
        a.remove(num)
    return a

print(array_diff([1,2], [1])) #, [2], "a was [1,2], b was [1], expected [2]")
print(array_diff([1,2,2], [1])) #, [2,2], "a was [1,2,2], b was [1], expected [2,2]")
print(array_diff([1,2,2], [2])) #, [1], "a was [1,2,2], b was [2], expected [1]")
print(array_diff([1,2,2], [])) #, [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
print(array_diff([], [1,2])) #, [], "a was [], b was [1,2], expected []")
print(array_diff([1,2,3], [1, 2])) #, [3], "a was [1,2,3], b was [1, 2], expected [3]")