def peel_layer_off(lst):

    return [i[1:-1] for i in lst[1:-1]]

a=peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) 
print(a)