def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    minimum_val = float("inf")

    while (l < r):
        mid = (l+r) // 2
        minimum_val = min(minimum_val, nums[mid])

        if nums[mid] > nums[r]:
            # smallest value is in the right side, shift left pointer
            l = mid + 1
        else:
            # smallest value is in the left side, shift right pointer
            r = mid - 1
    return min(minimum_val, nums[l])

# time complexity: O(log n)
# space complexity: O(1)


        