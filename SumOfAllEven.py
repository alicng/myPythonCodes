def sum_of_evens(lst):
    k=0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]%2==0:
                k=k+lst[i][j]
    return k
    #return sum([i for i in [ y for x in lst if len(x) > 2 for y in x ] if i % 2 == 0])

a=sum_of_evens([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
])
print(a)