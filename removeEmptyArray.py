def remove_empty_arrays(arr):
		return [x for x in arr if len(x) != 0]
    
a=remove_empty_arrays(["a", "b", [], [], [1, 2, 3]])
print(a)