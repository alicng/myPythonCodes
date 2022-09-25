def move_to_end(lst, el):
    
    return [i for i in lst if i != el]+[i for i in lst if i == el]

a=move_to_end([1, 3, 2, 4, 4, 1], 1)
print(a)