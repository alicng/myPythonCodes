import datetime

def get_days(date1, date2):

    return (date2 - date1).days
    
a=get_days(datetime.date(2018, 12, 29),datetime.date(2019, 1, 1))
print(a)
