def divisible_by_left(n):
    n=str(n)
    return [False] + [a != "0" and int(b) % int(a) == 0 for a, b in zip(n, n[1:])]

a=divisible_by_left(2026)
print(a)
#	return [False]+[False if str(n)[i-1]=='0' else int(str(n)[i])%int(str(n)[i-1])==0 for i in range(1,len(str(n)))]