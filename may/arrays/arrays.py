def reverse_arr(arr=[]):
    return arr[::-1]

# print(reverse_arr(arr=[1,2,3,4,5]))

def reverse_with_two_pointers(start, end, arr=[]):
    while start < end:
        arr[start], arr[end]  = arr[end], arr[start]
        start+=1
        end-=1
        
    return arr

# print(reverse_with_two_pointers(0, 4, arr=[1,2,3,4,5]))

def rotate_array(arr, d, N):
    """Rotate an array d times to the left [1, 2, 3, 4, 5, 6, 7],
    """
    d = d % N # incase d is bigger than N
    temp = [] # this will cause space complexity to be O(N)
    
    # copy the array from d to the end
    temp = arr[d:N]
    
    # add the first d elements the end of the array
    for i in range(0,d):
        temp.append(arr[i])
    
    return temp

# print(rotate_array([1, 2, 3, 4, 5, 6, 7], 20, len([1, 2, 3, 4, 5, 6, 7])))

def reverse_sub_arr(left, arr, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left , right = left + 1, right - 1
    return arr


def right_rotate_array(arr, k):
    """
    Given an Array of size N and a value K, around which we need to right rotate the array
    [1,2,3,4,5]
    """
    k = k % len(arr)
    arr = reverse_sub_arr(left=0, arr=arr, right=len(arr)-1)
    arr = reverse_sub_arr(left=0, arr=arr, right=k-1)
    arr = reverse_sub_arr(left=k, arr=arr, right=len(arr)-1)
    
    return arr
        
       
# print(right_rotate_array([1, 2, 3, 4, 5], 2))

def insert_element_to_right(arr, element, position):
    for i in range(len(arr)-1, position-1, -1):
       arr[i+1] = arr[i]
    
    arr[position] = element
    return arr
        
    
# print(insert_element_to_right([1, 2, 3, 4, 5, None], element=9, position=2))

def binary_search(arr, low, high, element):
    mid = (low + high) // 2 
    if element == arr[mid]: return mid
    
    if element < mid:
        return binary_search(arr, low, (mid-1), element)
    elif element > mid:
        return binary_search(arr, (mid+1), high, element)
    
    return -1 # not found

# print(binary_search(arr=[1,2,3,4,5,6,7,8,9], low=0, high=len([1,2,3,4,5,6,7,8,9]) - 1, element=5))


def array_sum(nums):
    """Given an integer array, nums, return an array containing its running sum at every index
    [1,2,3] -> [1,3,6]; [10]->[10]
    """
    # time complexity = O(n), space complexity = O(n): we created a new array 
    # sum = 0
    # new_arr = []
    # for index, num in enumerate(nums):
    #     sum += num
    #     new_arr.append(sum)
    # return new_arr

    # time complexity = O(n), space complexity = O(1) 
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

print(array_sum([10]))

    
        
 
    