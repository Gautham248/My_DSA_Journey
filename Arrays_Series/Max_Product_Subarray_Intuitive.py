def maxProduct(nums):
    prefix=suffix=1
    answer=float('-inf')
    size=len(nums)
    for i in range(0,size):
        if prefix==0:
            prefix=1
        if suffix==0:
            suffix=1
        prefix=prefix*nums[i]
        suffix=suffix*nums[size-i-1]
        answer=max(answer,max(prefix,suffix))
    return answer

nums=[2,3,-2,4]
print(maxProduct(nums))