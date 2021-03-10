def where_is_waldo(lst):
    
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] != lst[0][0]:
                return [i+1, j+1]

a=where_is_waldo([
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["P", "O", "O", "O"],
  ["O", "O", "O", "O"]
])
print(a)