def inclusive_list(start_num, end_num):

    return [i  for i in range(start_num, end_num +1)] if start_num < end_num else [start_num]

a=inclusive_list(17, 5)
print(a)
#list(range(startNum, endNum+1)) or [startNum]