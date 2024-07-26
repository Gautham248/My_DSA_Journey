


"""
We need to keep track of both the minimum and maximum products because of the properties of multiplication involving negative numbers :
- Negative number can change the products sign. A large positive number becomes a large negative number when multiplied by a negative number and vice versa
- The minimum product up to the current index can become the maximum product if multiplied by a negative number.


result , max_product and min_product are initialized to the starting element of the array.
We start iterating with the second element. If the number is a negative number, we swap the values of max_product and min_product.
Update the max_product by taking the max of the current element and the product of current element and the previous max_product
Update the min_product by taking the min of the current element and the product of the current element and the previous min product

update the result at each iteration to be the max of the previous result and the current max_product
"""

def maxProduct(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result
    
nums=[2,3,-2,4]
print(maxProduct(nums))