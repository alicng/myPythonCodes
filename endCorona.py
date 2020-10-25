def end_corona(recovers, new_cases, active_cases):
    ac=active_cases
    count=0
    while ac > 0:
        ac -=(recovers - new_cases)
        count += 1
    return count
    a=end_corona(4000, 2000, 77000)
print(a)