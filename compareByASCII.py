def ascii_sort(lst):
    x=sum([ord(i) for i in str(lst[0]) if i.isalpha()])
    y=sum([ord(i) for i in str(lst[1]) if i.isalpha()])
    return lst[0] if x < y else lst[1]

a=ascii_sort(["victory", "careless"])
print(a)