def commonName(b_players, f_players):
    names = {} 
    multi_players = []

    for hash in b_players:
      key = f"{hash['first_name']} {hash['last_name']}"
      names[key] = True
    
    for hash in f_players:
      if names.get(f"{hash['first_name']} {hash['last_name']}"):
        multi_players.append(f"{hash['first_name']} {hash['last_name']}")
        
    return multi_players




basketball_players = [
    {'first_name': "Jill", 'last_name': "Huang", 'team': "Gators"},
    {'first_name': "Janko", 'last_name': "Barton", 'team': "Sharks"},
    {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Sharks"},
    {'first_name': "Jill", 'last_name': "Moloney", 'team': "Gators"},
    {'first_name': "Luuk", 'last_name': "Watkins", 'team': "Gators"}
  ]
football_players = [
  {'first_name': "Hanzla", 'last_name': "Radosti", 'team': "32ers"},
  {'first_name': "Tina", 'last_name': "Watkins", 'team': "Barleycorns"},
  {'first_name': "Alex", 'last_name': "Patel", 'team': "32ers"},
  {'first_name': "Jill", 'last_name': "Huang", 'team': "Barleycorns"},
  {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Barleycorns"}
  ]

print(commonName(basketball_players, football_players))