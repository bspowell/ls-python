#take 2 strings
# only includes letters from a-z
# return a new sorted string, containing distinct lettesr 


# combine each string into a larger string, 

def longest(a1, a2):
  return ''.join(sorted(set(a1 + a2)))


print(longest("aretheyhere", "yestheyarehere")) # "aehrsty"
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding")) # "abcdefghilnoprstu"
print(longest("inmanylanguages", "theresapairoffunctions")) # "acefghilmnoprstuy"
        