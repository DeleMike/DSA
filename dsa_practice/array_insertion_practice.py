def addToEndOfArray():
    """We are implemeting the `add` method in arrays.
    Hence, we will not use the `add` method of a list
    """
    # let's say we have an array of length 6
    nums = [None] * 6
    length = 0;

    # Add 3 elements to the Array
    for i in range(3):
        nums[length] = i;
        length+=1
    print(nums)
    
    # add to the end of the array
    nums[length] = 10;
    length+=1 # increment for the length pointer to point to the next empty space
    print(nums)
    # time complexity O(1)
    
    return nums
  
def get_length(nums):
    """This method gets the length of an array not capacity
    """  
    length = 0
    for num in nums:
        if num != None: length+=1
    return length
    
def addToStartOfArray(nums):
    """
    Add to the start of the array. time complexity: O(n)
    """
    # to insert to the start of an array, we must shift all elements one step to the right
    # get length of array not capacity
    
    length = get_length(nums)
    
    for index in range(length-1,-1,-1):
        nums[index + 1] = nums[index]
    print(nums)
    
    # the add to the start of the array
    nums[0] = 6
    print(nums)
    
    return nums

def addToAnyPosition(nums):
    """Add an element to any position of an array.
    This will add an element to any position of the array
    
    This is like the `insert` operation. some_list.insert(given_index, value)
    For now, we use a dummy position of 2. We are working with a list whose length is fixed at 6
    """
    given_index = 2
    length = get_length(nums)
    # first, we shift all elements from 2 to n-1  by one step
    for index in range(length-1,given_index-1,-1): # from 2 to n-1
        nums[index+1] = nums[index]
        # print(index) 
    # now, insert 39 at given_index
    nums[given_index] = 39
    print(nums)
    
    
numbers = addToEndOfArray()
start_nums = addToStartOfArray(numbers)
addToAnyPosition(start_nums)