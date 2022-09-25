def chunk(array, size):
    
    return [array[i:i + size] for i in range(0, len(array), size)]
    

a=chunk([1, 2, 3, 4, 5, 6, 7], 3)
print(a)