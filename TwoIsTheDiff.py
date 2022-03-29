def difference_two(lst):
      
    return sorted([i, j] for i in lst for j in lst if j - i == 2)

a=difference_two([1, 2, 3, 4])
print(a)