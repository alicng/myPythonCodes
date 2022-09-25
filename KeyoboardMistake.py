def keyboard_mistakes(txt):

  di = {"4": "A",  "5": "S",  "0": "O",  "1": "I"}
  for k,v in di.items():
      txt =txt.replace(k, v)
  return txt

a=keyboard_mistakes("51NG4P0RE")
print(a)

#A is misinterpreted as 4
#S is misinterpreted as 5
#O is misinterpreted as 0
#I is misinterpreted as 1
