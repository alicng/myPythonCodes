def just_another_sum_problem(a, b):
   if a < b:
      return sum([i for i in range(a,b+1)])
   return sum([i for i in range(b,a+1)])
#return sum(range(min(a, b), max(a, b) + 1))
a=just_another_sum_problem(90, 45)
print(a)