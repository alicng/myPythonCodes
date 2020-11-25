def calc_bundled_temp(n, temp):

    total = int(temp[:-2]) 
    for i in range(n):
        total += total * 0.1
    return str(round(total, 1)) + "*C"

a=calc_bundled_temp(4, "6*C")
print(a)
#return str(round(int(temp.strip('*C'))*(1.1**n), 1))+'*C'