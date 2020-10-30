def total_distance(height, length, tower):

    return round((tower/height)*(height+length),1)

a=total_distance(0.2, 0.4, 100.0)
print(a)