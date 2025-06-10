def binary_search(items: list[int], target: int) -> int|None:
    """Binary search a list for a target value

    Args:
        items (list[int]): List of items to be searched. must be in ascending order
        target (int): target value to find in search space

    Returns:
        int|None: Returns target value position or NULL
    """
    low = 0
    high = len(items)-1
    
    while(low<=high):
        mid = (low+high)//2
        
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


item_list = [1,2,3,4,5]
print(binary_search(items=item_list, target=2))