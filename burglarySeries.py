def most_expensive_item(products):

    return ''.join([k for k, v in products.items() if v == max(products.values())])

a=most_expensive_item({
  "tv": 30,
  "skate": 20,
  "stereo": 50,
})
print(a)
#return max(products, key=products.get)
#return max(products.keys(), key= lambda p: products[p])