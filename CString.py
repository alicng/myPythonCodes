def cpp_txt(lst):

    return ''.join(lst[:-1])

a=cpp_txt(["J", "A", "V", "a", "\0"])
print(a)