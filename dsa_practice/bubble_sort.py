def bubble_sort(nums):
    """This procedure will sort elements in a given order
    Time complexity: O(n^2)
    Space complexity: O(1)
    Args:
        nums (int): A list of numbers
    """
    print('Input Numbers: ', nums)
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            # perform swap
            if nums[j] < nums[j+1]: # ">" ascending order, "<" descending order
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

# take inputs and convert it to a list
# input will require a space between them
# e.g: 1 2 3 and not 123
data_list = list(map(int, input().split()))

# call the bubble sort function
sorted_list = bubble_sort(data_list)

# print the sorted list
print('Sorted array is: ', sorted_list)