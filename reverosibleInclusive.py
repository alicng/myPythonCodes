def reversible_inclusive_list(start_of_range, end_of_range):
    start=[i for i in range(start_of_range,end_of_range+1)]
    end=[i for i in range(end_of_range, start_of_range+1)][::-1]
    return start if start_of_range < end_of_range else end

a=reversible_inclusive_list(10, 5)
print(a)