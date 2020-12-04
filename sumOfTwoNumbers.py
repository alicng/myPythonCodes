def check_sum(lst, n):

    return any(n - i in lst for i in lst)

a=check_sum([4, 5, 6, 7, 8, 9], 13)
print(a)
# for i in lst:
        #for j in lst:
            #if i + j == n:
                #return True
    #return False