def oddeven(lst):
    odd=[i for i in lst if i % 2]
    even=[i for i in lst if i % 2 ==0]
    return True if len(odd)>len(even) else False


a=oddeven([13452394823795273847528572346])
print(a)