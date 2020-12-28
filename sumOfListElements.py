def lst_ele_sum(args):

    return [sum(args[:i]+args[i+1:]) for i in range(len(args))]

a=lst_ele_sum([1, 2, 3, 2, 1])
print(a)