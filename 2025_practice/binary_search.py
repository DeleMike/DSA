def binary_search(items: list[int], target: int) -> int|None:
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