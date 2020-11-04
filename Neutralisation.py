def neutralise(s1, s2):

    
    return ''.join(['0' if i[0] != i[1] else '+' if i[0] and i[1] =='+' else '-'  for i in zip(s1, s2)])

a=neutralise("-++-", "-+-+")
print(a)
#return ''.join(a if a == b else '0' for a, b in zip(s1, s2))