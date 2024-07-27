"""
NORMAL APPROACH:
Find the smallest and largest element in the array in a single traversal
After this, we once again traverse the array and find an element that is just greater than the smallest element we just found.
Similarly, we would find the largest element which is just smaller than the largest element we just found
Indeed, this is our second smallest and second largest element.

def second_largest_in_array(nums):
      max=nums[0]
      second_largest=nums[0]
      for i in range(0,len(nums)):
            if nums[i]>max:
              max=nums[i]
      for i in range(0,len(nums)):
           if nums[i]>second_largest and nums[i]<max:
                second_largest=nums[i]
      return second_largest
           

nums=[1,2,3,4,5]
print(second_largest_in_array(nums))
"""

# BEST APPROACH => Do it all in a single traversal
def second_largest_in_array(nums):
      max=second_largest=float('-inf')
      for i in range(0,len(nums)):
            if nums[i]>max:
              second_largest=max
              max=nums[i]
            elif nums[i]>second_largest and nums[i]!=max:
                second_largest=nums[i]
      return second_largest
           

nums=[1,2,3,4,5]
print(second_largest_in_array(nums))