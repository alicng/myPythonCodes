def parse_list(lst):

    return [str(i) if type(i) == int else i for i in lst ]

a=parse_list([1, 2, 3, 17, 24, 3, "a", "123b"])
print(a)