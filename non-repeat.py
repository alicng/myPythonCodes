def a(n):
    d = {}
    for i in n:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
            b={x for (x,y) in d.items() if y == 1}
    return ',  '.join(b) 
                  
    
products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]
a=a(products)
print(a)