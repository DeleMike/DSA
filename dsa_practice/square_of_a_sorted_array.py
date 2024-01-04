"""EASY
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

[-4,-1,0,3,10]
[-7,-3,2,3,11]

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # [-4,-1,0,3,10]
    # [-7,-3,2,3,11]
    
    i = 0
    j = len(nums)-1
    n = len(nums)
    result = [None] * n # create an array which is the same length of the array we wanna sort
    
    
    for p in range(n-1,-1,-1): # count in decreasing fashion
        # if the number at the first pointer is greater than the one at the second pointer
        # then it has to go to position p 
        if abs(nums[i]) > abs(nums[j]):
            result[p] = nums[i] * nums[i]
            i+=1
        else:
            result[p] = nums[j] * nums[j]
            j-=1
            
    return result

# time complexity = O(n)
# space complexity = O(n)

print(sortedSquares([-3,7,11]))
print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))
