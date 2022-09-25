def age_difference(ages):
    
    return "No age difference between spouses." if sorted(ages)[-1]==sorted(ages)[-2] else \
        "1 year" if (sorted(ages)[-1])-(sorted(ages)[-2])==1 else "{} years".format((sorted(ages)[-1])-(sorted(ages)[-2])) 
    
                                  
     

a=age_difference([2, 4, 6, 32, 28])
print(a)