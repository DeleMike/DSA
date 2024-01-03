def bubble_sort(nums):
    """This procedure will sort elements in a given order
    Here, we prevent the loops from making redundant iterations.
    After each iteration of the outer loop, at least one element is already sorted 
    So no need to access all the elements to check if they are placed in order
    
    Time complexity is still O(n^2). We only reduce number of redundant iterations / comparison
    Space complexity: O(1)
    Args:
        nums (int): A list of numbers
    """
    print('Input Numbers: ', nums)
    for i in range(len(nums)-1):
        swapped = False
        for j in range(len(nums)-1-i):
            # perform swap
            if nums[j] > nums[j+1]: # ">" ascending order, "<" descending order
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        # if no element was swapped, simply terminate the loop cos we already have a sorted list
        if not swapped: 
            break
    
    return nums

# take inputs and convert it to a list
# input will require a space between them
# e.g: 1 2 3 and not 123
data_list = list(map(int, input().split()))

# call the bubble sort function
sorted_list = bubble_sort(data_list)

# print the sorted list
print('Sorted array is: ', sorted_list)