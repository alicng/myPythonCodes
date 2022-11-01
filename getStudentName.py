def get_student_names(students):
    
    
    return sorted([i for i in students.values()])

a=get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
})
print(a)