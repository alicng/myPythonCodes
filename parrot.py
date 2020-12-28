import datetime
def parrot_trouble(talking, hour):
    now = datetime.datetime.now()

    return True if talking == True and hour == now.hour else False

a=parrot_trouble(True, 10)
print(a)