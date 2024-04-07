result = zip(range(5, 10),    # length is 5
             range(1, 3),     # length is 2 (shortest)
             range(3, 7))     # length is 4
print(list(result)) # [(5, 1, 3), (6, 2, 4)]
print(result) # []