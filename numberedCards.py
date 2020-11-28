def win_round(you, opp):
    
    return sorted(you)[:2:-1] > sorted(opp)[:2:-1]

a=win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2])
print(a)
