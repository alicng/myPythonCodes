from time import strftime
from time import gmtime
def digital_clock(seconds):

    return strftime("%H:%M:%S", gmtime(seconds))

a=digital_clock(5025)
print(a)
#return '{:02}:{:02}:{:02}'.format(s//3600%24, s//60%60, s%3600%60)