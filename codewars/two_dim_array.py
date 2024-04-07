# Function receive a two-dimensional square array of random integers. On the main diagonal, all the negative integers must be changed to 0, while the others must be changed to 1 (Note: 0 is considered non-negative, here).

# (You can mutate the input if you want, but it is a better practice to not mutate the input)

# Example:

# Input array


arr = [
  [-1,  4, -5, -9,  3 ],
  [ 6, -4, -7,  4, -5 ],
  [ 3,  5,  0, -9, -1 ],
  [ 1,  5, -7, -8, -9 ],
  [-3,  2,  1, -5,  6 ]
]

def alter(two_array):
  index = 0
  for array in two_array:
    if array[index] < 0:
      array[index] = 0
    else:
      array[index] = 1
    index += 1

alter(arr)
print(arr)