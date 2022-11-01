def profit_margin(cost_price, sales_price):
    
    return '{}%'.format(round((sales_price - cost_price) / sales_price *100,1))

a=profit_margin(28, 39)
print(a)

# "28.2%"