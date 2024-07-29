from typing import List, Union
def binary_search(data: list[Union[int, str]], target: int) -> int:
    """_summary_

    Args:
        data (List[int]): It has to be sorted. Same concept applies to List[String]
    """
    left = 0
    right = len(data) - 1
    
    while (left <= right):
        mid = (left + right) // 2
        
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print('We found it to be at position = ', binary_search([
    "Ayoola Gideon",
    "Christiana Iretiayo",
    "Boluwatife Peter",
    "Sunday John",
    "Akindele Michael",
    "OluwaSegun Olaniyi"
    ], "Boluwatife Peter"))
    