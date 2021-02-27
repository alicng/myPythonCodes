def top_note(student):
    
    return {'name': student['name'], 'top_note': max (student['notes'])}

a=top_note({ "name": "John", "notes": [3, 5, 4] })
print(a)