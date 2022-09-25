import socket 
def get_domain(ip_address):
    name, alias, addresslist = socket.gethostbyaddr(ip_address)
    return name, alias, addresslist

a=get_domain("206.190.36.45")
print(a)
#return socket.gethostbyaddr(ip_address)[0]