
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1

    while (l <= r):
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[l] <= nums[mid]:
            # searching the left space
            if target > nums[mid] or target < nums[l]:
                l = mid + 1 # value should be in right space
            else:
                r = mid - 1 # value should be left space
        else:
            # searching the right space
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

print(search([4,5,6,0,1,2], 1))
        