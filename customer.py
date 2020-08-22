names = ["James", "John", "Emma"]
surnames = ["Oliver", "Smith", "Brown"]
birth_days = [15, 22, 8]
birth_months = [3, 6, 12]
birth_years = [1984, 1994, 2001]

name= input('Please enter your name: ')
if name.title() not in names:
    print('You are not a customer!')
if name.title() in names:
    surname=input('Please enter your surname: ')
    if surname.title() not in surnames:
        print('You are not a customer!')
    if surname.title() in surnames:
        a=names.index(name.title())
        print(a)
        b=surnames.index(surname.title())
        if a!=b:
            print('You are not a customer!')
        if a==b:
            birthday=input('Please enter your birthday (MM/DD/YYYY): ')
            c=birth_days.index(int(birthday.split('/')[0]))
            print(c)
            if c not in birth_days:
                print('You are not a customer!')
            d=birth_months.index(int(birthday.split('/')[1]))
            if d not in birth_months:
                 print('You are not a customer!')
            e=birth_years.index(int(birthday.split('/')[2]))
            if e not in birth_years:
                 print('You are not a customer!')
            print(e) 
            if c == d and d== e:
                print ('You are a customer!')
            else:
                print ('You are not a customer!')
# print(names.index('John'))
# and birthday.split('/')[0] in birth_months and birthday.split('/')[2] in birth_years: