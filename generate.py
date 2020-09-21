with open ('fruits.txt', 'w') as fruit:
    fruit.write('Banana')
    fruit.write('Orange')

with open ('fruits.txt', 'r') as fruit:
    print(fruit.read())
    


