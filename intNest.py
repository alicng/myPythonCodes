def print_all_groups():
   
    return ', '.join(i+j for i in '123456' for j in 'abcde')

a=print_all_groups()
print(a)
"""
def print_all_groups():
    	result = []
	for i in '123456':
		for x in 'abcde':
			result.append(i+x)
	return ', '.join(result)"""