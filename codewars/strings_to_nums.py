def to_float_array(arr):
  new_list = list()
  for string in arr:
    if string.find('.') == -1:
      new_list.append(int(string))
    else:
      new_list.append(float(string))
  return new_list

print(to_float_array(['1', '1.1', '1.3', '2']))

# def to_float_array(arr): 
#     new_list = []
#     for i in arr:
#         if "." in i:
#             new_list.append(float(i))
#         else:
#             new_list.append(int(i))
#     return new_list


# def to_float_array(arr): 
#     return list(map(float, arr))