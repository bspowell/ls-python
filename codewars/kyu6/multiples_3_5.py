# find all numbers below given number
# that are multiples of 3 or 5
# each number counted only once
# return sum of all multiples
# if number given is negative, return 0

# iterate over number from 0 to -1 number
# if number % 5 == 0 or number % 3 == 0 then add number to total


def solution(number):
  total = 0
  for num in range(number):
    if (num % 3 == 0) or (num % 5 == 0):
      total += num
  return total
  
print(solution(4)) # 3
print(solution(6)) # 8
print(solution(16)) # 60
print(solution(3)) # 0
print(solution(5)) # 3
print(solution(15)) # 45
print(solution(0)) # 0
print(solution(-1)) # 0
print(solution(10)) # 23
print(solution(20)) # 78
print(solution(200)) # 9168