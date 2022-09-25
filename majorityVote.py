def majority_vote(lst):
    for i in set(lst):
	    if lst.count(i) > len(lst) // 2:
             return i
    return None
    
a=majority_vote(["B", "C", "A", "A"])
print(a)
#(max(set(lst), key = lst.count))