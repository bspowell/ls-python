def double_check(strng):
    for index in range(len(strng) - 1):
        if strng[index].lower() == strng[index + 1].lower(): return True
    return False

msg = input('make a string: ')
print(double_check(msg))

# check if there are double characters side by side in a string
# not case sensitive
