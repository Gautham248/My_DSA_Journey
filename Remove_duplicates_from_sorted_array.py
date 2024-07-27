def removeDuplicate(nums):
    # The array is already sorted.
    # Just check if the first element and the adjacent element are the same or not
    # Do the same for the second element and so on
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1

nums=[1,1,2,2,2,3,3,4,5]
k=removeDuplicate(nums)
for i in range(k):
    print(nums[i],end=" ")
