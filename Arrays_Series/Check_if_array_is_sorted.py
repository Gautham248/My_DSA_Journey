def checkSorted(nums):
    for i in range(0,len(nums)):
        if i==len(nums)-1:
            break
        if nums[i+1]<nums[i]:
            return False
    return True

nums=[1,2,3,5,4]
print(checkSorted(nums))    