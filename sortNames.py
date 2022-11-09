def last_name_lensort(names):
    
    return sorted(names, key=lambda x: (len(x.split()[1]), x.split()[1]))

a=last_name_lensort([
  "Jennifer Figueroa",
  "Heather Mcgee",
  "Amanda Schwartz",
  "Nicole Yoder",
  "Melissa Hoffman"
])
print(a)