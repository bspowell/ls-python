def evens(array, new_arr=[]):
  #returns new array containing even numbers
  if array == []:
    return new_arr
  elif array[0] % 2 == 0:
    new_arr.append(array[0])
  
  return evens(array[1:], new_arr)

print(evens([1,2,3,4,5,6]))