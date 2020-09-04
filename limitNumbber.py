def limit_number(num, range_low, range_high):


    return range_low if range_low > num else range_high if range_high < num else num


a=limit_number(14, 1, 10)
print(a)