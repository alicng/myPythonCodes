def is_shifted(lst1, lst2):
    return lst2 == [i + (lst2[0]-lst1[0]) for i in lst1]
	

def is_multiplied(lst1, lst2):
	return lst2 == [i * (lst2[0]/lst1[0]) for i in lst1]

a=is_shifted([1, 2, 3], [2, 3, 4])
a=is_multiplied()

print(a)