# Complete the function to return true if
# the two arguments given are anagrams of each other; return false otherwise.

# eg. "foefet" is an anagram of "toffee"
# eg. "Buckethead" is an anagram of "DeathCubeK"

# given a string
# lowercase, break into a list, sort each one and join
# see if they equal eachother
# Note: anagrams are case insensitive


def is_anagram(test, original):
  test = ''.join(sorted(list(test.lower())))
  original = ''.join(sorted(list(original.lower())))
  return test == original


print(is_anagram("foefet", "toffee")) # True, 
print(is_anagram("Buckethead", "DeathCubeK")) # True,
print(is_anagram("Twoo", "WooT")) # True, 
print(is_anagram("dumble", "bumble")) # False
print(is_anagram("ound", "round")) # False
print(is_anagram("apple", "pale")) # False