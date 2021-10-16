def assign_person_to_job(names, jobs):

    return {x:y for x,y in zip(names,jobs)}

a=assign_person_to_job(["Dennis", "Vera", "Mabel", "Annette", "Sussan"],
["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"])
print(a)