def merge_sort(lst1, lst2):

    return sorted((lst1+lst2), reverse=True) if lst1[0] > lst1[1] else sorted((lst1+lst2), reverse=False)

a=merge_sort([120, 180, 200], [190, 175, 130])
print(a)