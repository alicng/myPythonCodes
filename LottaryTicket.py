def lottery(ticket, win):
    a = len([i for i in ticket if chr(i[1]) in i[0]])
    return 'Loser!' if a<win else 'Winner!'
    
   

a=lottery([["YYW", 89], ["WXK", 65], ["RPDI", 88]], 2)
print(a)