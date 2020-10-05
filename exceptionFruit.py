fruits = ['banana', 'mango', 'pear', 'apple', 'kiwi', 'grape']
for i, fruit in enumerate(fruits):
    print(f"({i}) {fruit}")
print("enter -1 to exit")
while True:
    selection = input("make a selection: ")
    try:
        print(fruits[int(selection)])
    except ValueError as e:
        print("You need to enter a number. Try again")
    except IndexError as e:
        print("No such fruit. keep trying")
    else:
        break