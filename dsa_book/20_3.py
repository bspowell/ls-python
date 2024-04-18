# make first number lowest
# if next number is lower, make it the lowest
# if next number is higher, make it new profit
# return profit


def findMaxProfit(array):
  low_price = array[0]
  max_price = 0
  profit = 0

  for price in array:
    if price <= low_price:
      low_price = price
    elif max_price < price: 
      max_price = price
      profit = max_price - low_price
    
  return profit



print(findMaxProfit([10, 7, 5, 8, 11, 2, 6]))