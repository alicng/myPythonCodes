def journey_distance(n):

    return ((n-3)//2)+1 if n > 0 else 0

a=journey_distance(9)
print(a)
#A taxi journey costs $3 for the first kilometer travelled. 
# However, all kilometers travelled after that will cost $2 each.