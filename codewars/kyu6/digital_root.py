# given n, take the sum of the digits of n
# If has more than 1 digit - reduce to a sum of the digits 
# if that sum has more than 1 digit - reduce to a sum of the digits
# repeat until only 1 digit

# given a number
# while number > 9
#   make into a list with individual digits
#   use reduce to sum all  over that list as ints

def digital_root(n):
    while n > 9:
        n = sum([int(num) for num in list(str(n))])
    return n
        


print(digital_root(16)) #  7
print(digital_root(942)) #  6
print(digital_root(132189)) #  6
print(digital_root(493193)) #  2