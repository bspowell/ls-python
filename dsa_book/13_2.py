def findMissing(array):
	array.sort()
	
	for index in range(len(array)):
		if array[index] != index:
			return index
		index += 1
	return None


print(findMissing([5, 2, 4, 1, 0]))
print(findMissing([9, 3, 2, 5, 6, 7, 1, 0, 4]))