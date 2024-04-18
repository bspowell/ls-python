# The following function accepts an array of numbers 
# and returns the sum, as long as a particular number
#  doesn’t bring the sum above 100. If adding a 
# particular number will make the sum higher than 100,
#  that number is ignored. However, this function 
# makes unnecessary recursive calls. Fix the code 
# to eliminate the unnecessary recursion:

# def add_until_100(array):
#     if len(array) == 0:	return 0 

#     if array[0] + add_until_100(array[1, array.length - 1]) > 100:
# 		    return add_until_100(array[1, array.length - 1]) 
#     else:
# 		    return array[0] + add_until_100(array[1, array.length - 1]) 


def add_until_100(array):
    if len(array) == 0:	return 0 

    sum_so_far = add_until_100(array[1:])
    if array[0] + sum_so_far > 100:
        return sum_so_far
    else:
		    return array[0] + sum_so_far


print(add_until_100([1,2,100,3,90,20])) # 26