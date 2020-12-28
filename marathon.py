def marathon_distance(d):

    return sum(abs(i) for i in d) == 25

a=marathon_distance([-6, 15, 4])
print(a)