def get_prices(lst):
    
    return [float(i.split('$')[1].split(')')[0]) for i in lst]

a=get_prices([
  "ice cream ($5.99)",
  "banana ($0.20)",
  "sandwich ($8.50)",
  "soup ($1.99)"
])
print(a)