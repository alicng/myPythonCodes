def rotate(nums, k):
    
    d = len(nums) - k   # 12 - 5 => d=7
    nums[:]=   nums[d:]  +  nums[0:d]  # 8,9,10,11,12 + 1234567
    return nums
        

a=rotate([1,2,3,4,5,6,7,8,9,10,11,12], 5)
print(a)