# get the length of the array 
# iterate from 1 to array length -1 and create a hash with the numbers equal to 0
# iterate through the list and add 1 to each number in hash
# return the number that contains 0

def findMissingNum(array):
  numbers = {}

  for i in range(len(array)+1):
    numbers[i] = 0
  
  print(numbers)
  for number in array:
    numbers[number] += 1

  for key in numbers:
    if numbers[key] == 0:
      return key
  


print(findMissingNum([2,3,0,6,1,5])) # 4
print(findMissingNum([8, 2, 3, 9, 4, 7, 5, 0, 6])) # 1
