def major_sum(lst):
    b= len([i for i in lst if i == 0])
    c= len([i for i in lst if i != 0])
    e= sum([i for i in lst if i > 0])
    f= sum([i for i in lst if i < 0])
    d= b if  b > c else e if e > abs(f) else f
    return d

a=major_sum([1, 2, 3, 4, 0, 0, -3, -2])
print(a)
#if lst.count(0) > lst.count(i != 0) else i