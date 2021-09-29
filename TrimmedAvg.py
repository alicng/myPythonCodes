def trimmed_averages(lst):

    
    return round(sum(sorted(lst)[1:-1])/(len(lst)-2))
   



a=trimmed_averages([4, 5, 7, 100])
print(a)

#Given a list of numbers, remove the largest and smallest numbers, 
# and calculate the average of the remaining numbers.