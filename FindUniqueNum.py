def find_single_number(numbers):

    return None if len(numbers)==0 else ''.join([str(i) for i in numbers if numbers.count(i) ==1])

a=find_single_number([])
print(a)