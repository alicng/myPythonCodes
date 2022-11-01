def happy_year(year):
    while True:
      year+=1
      if len(str(year))==len(set(str(year))):
          return year
      
      
a=happy_year(3991)
print(a)