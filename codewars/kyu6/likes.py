# Implement the function which takes an array containing the 
# names of people that like an item. It must return the 
# display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# given an array of strings
# use a match statement to handle conditions
#   list empty
#     return 'no one likes this'
#   list length 1
#     return f`{firstelement} likes this` 
#   list lenght 2
#     return f`{1st} and {2nd} like this`
#   list length 3 
#     return f`{1st}, {2nd} and {3rd} like this`
#   else 
#     return f`{1st}, {2nd} and {len(list) - 2} others like this`

def likes(names):
  match len(names):
    case 0:
      return 'no one likes this'
    case 1:
      return f'{names[0]} likes this'
    case 2:
      return f'{names[0]} and {names[1]} like this'
    case 3:
      return f'{names[0]}, {names[1]} and {names[2]} like this'
    case _:
      return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


print(likes([])) #, 'no one likes this')
print(likes(['Peter'])) #, 'Peter likes this')
print(likes(['Jacob', 'Alex'])) #, 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark'])) #, 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max'])) #, 'Alex, Jacob and 2 others like this')