def next_in_line(lst, num):
    
    return "No list has been selected" if len(lst) == 0 else lst[1:]+[num]

a=next_in_line([7, 6, 3, 23, 17], 10)
print(a)