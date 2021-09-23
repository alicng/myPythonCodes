def clean_up_list(lst):
    return [[ int(i) for i in lst if int(i) % 2 == 0],[ int(x) for x in lst if int(x) % 2 != 0]]
    



a=clean_up_list(["7", "4", "8"])
print(a)