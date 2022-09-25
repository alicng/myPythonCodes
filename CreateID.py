def create_id(firstname, lastname):
    return firstname[0].lower()+lastname[0].upper()+lastname[1:3].lower()



a=create_id("mary", "lamb")
print(a)



#"mLam"