# contains numbers or strings
# will not be empty or sparse
# return single array
  # numbers first, sorted in ascending order
  # strings second, sorted alphabetical order
  # values must maintain original type


# given an array
# findall digits
# findall strings



#

def db_sort(arr): 
    strings = [elem for elem in arr if isinstance(elem, str)]
    numbers = [elem for elem in arr if isinstance(elem, (int, float))] 
    strings.sort()
    numbers.sort()
    numbers = numbers + strings
    return numbers



db_sort([6, 2, 3, 4, 5])#, [2, 3, 4, 5, 6]
db_sort([14, 32, 3, 5, 5])#, [3, 5, 5, 14, 32]
db_sort([1, 2, 3, 4, 5])#, [1, 2, 3, 4, 5]
db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2])#, [0,2,2,"Apple","Banana","Mango","Orange"]
db_sort(["C", "W", "W", "W", 1, 2, 0])#, [0,1,2,"C","W","W","W"]
db_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6])#, [5,6,6,7,10,15,110,"!","2500","come","on"]
db_sort(["Apple",46,"287",574,"Peach","3","69",78,"Grape","423"])#, [46, 78, 574, '287', '3', '423', '69', 'Apple', 'Grape', 'Peach'] 