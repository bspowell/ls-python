cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]


for el in cities: 
  if el is None:
    continue
  else:
    print(len(el))