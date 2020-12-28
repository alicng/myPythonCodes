def get_only_evens(nums):

    return [i for i in nums[::2] if i % 2 ==0]


a=get_only_evens([1, 3, 2, 6, 4, 8])
print(a)