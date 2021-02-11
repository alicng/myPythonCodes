def solution(A):
    
    c=[i for i in range(min(A), max(A)+1)]
    d=''.join([str(i) for i in c if i not in A])
    e=min(A)-1
    f=max(A)+1
    return 1 if max(A)< 0 else int(d) if len(d) != 0 else e if e !=0 else f

a=solution([1,2,3,5,6])
print(a)
'''
Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''