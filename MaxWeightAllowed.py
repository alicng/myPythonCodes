def weight_allowed(car, p, max_weight):
    return (car + sum(p)) < max_weight * 2.2

a=weight_allowed(3000, [150, 201, 75, 88, 195], 1700)
print(a)
	
