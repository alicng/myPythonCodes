def char_at_pos(r, s):

        x = [v for i,v in enumerate(r) if i%2==["odd","even"].index(s)] 
        return''.join(x) if type(r)==str else x

a=char_at_pos("EDABIT", "odd")
print(a)
# i[0:] if s == "even" else i[::1]