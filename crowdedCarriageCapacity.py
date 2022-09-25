def find_a_seat(n, lst):
    d=([i for i in lst if int(i/(n // len(lst))*100) <= 50]) == []
    return -1 if d is True else lst.index([i for i in lst if int(i/(n // len(lst))*100) <= 50][0])

a=find_a_seat(200, [35, 23, 40, 21, 38])
print(a)
'''
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
'''