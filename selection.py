fruits = ['banana', 'mango', 'pear', 'apple', 'kiwi', 'grape']
for i, fruit in enumerate(fruits):
    print(f"({i}) {fruit}")
tries = 3
while tries > 0:
    selection = input("make a selection: ")
    try:
        print(fruits[int(selection)])
    except ValueError as e:
        print("You need to enter a number.", end=" ")
    except IndexError as e:
        print("No such fruit.", end=" ")
    except Exception as e:
        print("How did you that?", end=" ")
    else:
        break
    tries-=1
    if tries>0:
        print("Try again", end=" ")
    print(f"(you have {tries} tries left)")