def counting(array):
  if len(array) == 1:
    return len(array[0])
  else:
    return len(array[-1]) + counting(array[:-1])


print(counting(["ab", "c", "def", "ghij"]))