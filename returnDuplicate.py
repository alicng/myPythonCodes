def duplicate_nums(nums):

    return sorted(set(i for i in nums if nums.count(i) > 1)) or None

a=duplicate_nums([1, 2, 3, 4, 3, 5, 6])
print(a)
# l=[]
# d=[]
# for i in nums:
# if i in l: d.append(i)
# else l.append(i)
# return sorted(d) or None