def is_potential_friend(set1, set2):
    
    return set1 == set2 or len(set1.intersection(set2)) > 1
a=is_potential_friend({"music"},
  {"music"})
print(a)