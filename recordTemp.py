def record_temps(records, currentWeek):
    return [[min(i[0],j[0]),max(i[1],j[1])] for i,j in zip(records,currentWeek)]


a=record_temps([[34, 82], [24, 82], [20, 89],  [5, 88],  [9, 88], [26, 89], [27, 83]],
            [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]])
print(a)