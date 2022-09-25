def upload_count(dates, month):

    return len([i for i in dates if month in i])

a=upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept")
print(a)
#return str(dates).count(month)