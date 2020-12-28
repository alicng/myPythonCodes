def sort_by_length(lst):
    
    return sorted(lst, key=len)

a=sort_by_length(["apple", "pie", "shortcake"])
print(a)