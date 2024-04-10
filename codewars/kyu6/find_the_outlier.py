# given a list, find the only odd or only even number
# eg. [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# eg. [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)


# given a list
#   iterate over list 
#     if odd, place in list
#     if even, place in another list
#   whichever has a length of 1, return


def find_outlier(integers):
    condition = lambda x: x % 2 == 0
    evens = [num for num in integers if condition(num)]
    odds = [num for num in integers if not condition(num)]
    
    return odds[0] if len(odds) == 1 else evens[0]


print(find_outlier([2,6,8,10,3])) # 3 - odd at the back
print(find_outlier([2,6,8,200,700,1,84,10,4])) # 1 - odd in the middle
print(find_outlier([17,6,8,10,6,12,24,36])) # 17 - odd in the front
print(find_outlier([2,1,7,17,19,211,7])) # 2 - even in the front
print(find_outlier([1,1,1,1,1,44,7,7,7,7,7,7,7,7])) # 44 - even in the middle