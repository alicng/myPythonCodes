def back_to_home(directions):
    
    for i in directions:
        if directions.count('E') == directions.count('W') and directions.count('N') == directions.count('S'):
            return True 
        return False
    

a=back_to_home("NENESSWW")
print(a)