"""EASY
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_of_consecutive_ones = 0
    total_no_of_consecutive_ones = 0
    # [1,0,1,1,0,1]
    for num in nums:
        if num == 1:
            no_of_consecutive_ones += 1
            if no_of_consecutive_ones > total_no_of_consecutive_ones: 
                total_no_of_consecutive_ones=no_of_consecutive_ones     
        else:
            no_of_consecutive_ones = 0
            
    return total_no_of_consecutive_ones

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1]))
print(findMaxConsecutiveOnes([1,1,0,1,1,1,0,1]))
print(findMaxConsecutiveOnes([0,0,0]))
print(findMaxConsecutiveOnes([1,1,0,1,0,0,0,1,1,1,1,0,1]))
