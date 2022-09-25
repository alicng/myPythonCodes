from operator import itemgetter
def sort_drinks_by_price(drinks):

    return  sorted(drinks, key=itemgetter('price'))

drinks = [
  {"name": "lemonade", "price": 50},
  {"name": "lime", "price": 10}
]
a=sort_drinks_by_price(drinks)
print(a)
#return sorted(drinks,key=lambda x: x['price'])
