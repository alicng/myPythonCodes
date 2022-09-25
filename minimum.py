def solution(A):

    c=int(''.join(min([str(i) for i in range(min(A), max(A)+2) if i not in A])))
    return 1 if c < 0 else c

a=solution( [1, 2, 3, 7])
print(a)