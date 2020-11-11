def expensive_orders(orders, cost):

    return {i:v for i,v in orders.items() if v > cost}

a=expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000)
print(a)