"""
Problem: Write a function that takes an array of integers and returns the maximum value in the array.

Example:
Input: [1, 5, 3, 9, 2]
Output: 9

Instructions:
Create a function called findMaxElement(arr) that accepts an array arr.
The function should iterate through the array and return the largest integer.
Assume the array is non-empty and contains at least one number.
-
Constraints:
Time Complexity should be O(n), where n is the number of elements in the array.
You should not use built-in methods like max() in Python or Math.max() in JavaScript.
-
Hints:
Use a variable to keep track of the maximum value while looping through the array.
"""

def findMaxElement(arr: list) -> int:
    max_num = 0
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

# print(findMaxElement([1, 5, 3, 9, 2]))   

def must_not_be_zero(val:int)->int:
    if val == 0:
        raise ValueError('Must not be 0')
    return int

def main_block():  
    try:
        must_not_be_zero(0)
    except ValueError as e:
        print(e)
        return # Exit the function early if validation fails
    
    print('I am running')
    
main_block()