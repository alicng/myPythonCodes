import json
def printWithAge(txt, age):
    
    # Opening JSON file
    with open('cubsRoster.json','r') as f:
    # returns JSON object as a dictionary
        data = json.load(f)
        # Iterating through the json list
        return [i for i in data]
        # for i in data:
        #     if data[age]==age:
        #         return(firstName, LastName)

a=printWithAge('cubsRoster.json', 35)
print(a)


