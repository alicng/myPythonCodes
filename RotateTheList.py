def rotate_by_one(lst):
    lst.insert(0,lst.pop())
    return lst

a= rotate_by_one([1, 2, 3, 4, 5])
print(a)