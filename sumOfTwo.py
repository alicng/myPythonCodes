def sum_of_two(a, b, v):
    """for i in a:
        for j in b:
            if i+j == v:
                return True
            return False"""
    return any([i+j==v for i in a for j in b])

a=sum_of_two([1, 2], [4, 5, 6], 5)
print(a)