def sorting(array):
	array.sort()
	return array[-1] * array[-2] * array[-3]


print(sorting([5,4,2,5,1,5])) # 125