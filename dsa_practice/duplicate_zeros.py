"""EASY
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""

def get_length(nums):
    """This method gets the length of an array not capacity
    """  
    length = 0
    for num in nums:
        if num != None: length+=1
    return length

def duplicate_zeros(arr):
    for index in range(len(arr)):
        print(f'Checking {arr[index]}')
        if arr[index] == 0:
            # first step is shift all contents right.
            duplicate(index,arr)
        
            
    print(arr)

def duplicate(arr):
    zeroes = arr.count(0)
    n = len(arr)
    
    for i in range(n-1, -1, -1):
        if i + zeroes < n: # Check if the current position can be shifted to the right without going beyond the array bounds.
            arr[i + zeroes] = arr[i] # Shift the element to the right by zeroes positions.
        if arr[i] == 0:
            zeroes -= 1 # Decrement the remaining count of zeros.
            if i + zeroes < n:
                arr[i + zeroes] = 0 # Duplicate the zero in the appropriate position.
    print(arr)
           
    

        
duplicate([0,1,0,2,1,4])
# duplicate(0, [1,2,9,7,8,3,4,2])