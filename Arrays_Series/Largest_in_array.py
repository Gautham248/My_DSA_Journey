def largest_in_array(nums):
    max=nums[0]
    for i in range(0,len(nums)):
        if nums[i]>max:
            max=nums[i]
    return max

nums=[1,2,3,4,5]
print(largest_in_array(nums))