import datetime   
def weekday_dutch(date):
    d = {"Monday": "maandag", "Tuesday": "dinsdag", "Wednesday": "woensdag", "Thursday": "donderdag",
        "Friday": "vrijdag", "Saturday": "zaterdag", "Sunday": "zondag"}
    day = datetime.datetime.strptime(date, '%d %m %Y').strftime("%A")
    return d[day]

a=weekday_dutch("2 9 1945")
print(a)