def sort_by_letter(lst):
    
    return sorted(lst, key=lambda x: sorted(x)[-1])
    #return sorted(lst,key=lambda x: [l for l in x if l.isalpha()])
    #return sorted(lst, key=lambda word: list(filter(str.isalpha, word)

a=sort_by_letter(["932c", "832u32", "2344b"])
print(a)