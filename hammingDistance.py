def hamming_distance(txt1, txt2):
   
    
    return len([i for i  in zip(txt1, txt2) if i[0] != i [1]])

a=hamming_distance("strong", "strung")
print(a)