def car_timer(n):

    return eval('+'.join(list(str(n//60)+str(n%60))))
    
a=car_timer(808)
print(a)
'''
A built-in timer inside your car can count the length of your ride in minutes and you have started your ride at 00:00.

Given the number of minutes n at the end of the ride, calculate the current time. Return the sum of digits that the digital timer in the format hh:mm will show at the end of the ride.

Examples
car_timer(240) ➞ 4
# 240 minutes have passed since 00:00, the current time is 04:00
# Digits sum up is 0 + 4 + 0 + 0 = 4
'''