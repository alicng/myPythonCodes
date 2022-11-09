def char_at_pos(r, s):
    
    return r[1::2] if s == "even" else r[0::2]
    #return lambda r,s:(r[::2],r[1::2])['e'in s]
            
a=char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd")
print(a)