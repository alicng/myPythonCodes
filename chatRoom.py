def chatroom_status(users):
    if len(users)==0:
        return "no one online"  
    elif len(users)==1:
       return ''.join(users) +" "+ "online"
    elif len(users)==2:
        return users[0]+' '+'and'+' '+users[1]+' '+"online"
    else:
        return users[0]+', '+users[1]+' '+'and'+' '+ str(len(users)-2)+' '+'more online'

a=chatroom_status(['a','b','c','d'])
print(a)
#Write a function that returns the number of users in a chatroom based on the following rules:
#If there is no one, return "no one online".
#If there is 1 person, return "user1 online".
#If there are 2 people, return user1 and user2 online".
#If there are n>2 people, return the first two names and add "and n-2 more online".