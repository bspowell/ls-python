# Complete the function that accepts a string parameter, and
# reverses each word in the string. 
# All spaces in the string should be retained.

# given a string
# split string into words list
# iterate over using for loop and [::-1] to reverse string
# " ".join to return words back into string

def reverse_words(text):
  word_list = text.split(' ')
  reverse_list = [word[::-1] for word in word_list]
  return ' '.join(reverse_list)


print(reverse_words('string  string'))
print(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')