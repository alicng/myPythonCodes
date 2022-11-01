def get_budgets(lst):
    
    return sum([i['budget'] for i in lst])

a=get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
])
print(a)