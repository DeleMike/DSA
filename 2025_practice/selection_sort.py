def selection_sort(arr: list[int]) -> list[int]:
    new_arr = []
    copied_arr = list(arr)
    
    for i in range(len(copied_arr)):
        smallest_index = find_smallest(arr=copied_arr)
        new_arr.append(copied_arr.pop(smallest_index))
    return new_arr


def find_smallest(arr: list[int]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


item_list = [4,2,5,1,3,7,6]
print(selection_sort(arr=item_list))
