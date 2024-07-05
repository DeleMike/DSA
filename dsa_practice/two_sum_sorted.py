def twoSumSortedArray(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # time: O(n), space: O(1)
    l, r = 0, len(numbers) - 1
    while (l < r):
        total = numbers[l]+ numbers[r]
        if total == target:
            return [(l+1), (r+1)]
        elif total > target:
            r -= 1
        elif total < target:
            l += 1
    return [-1,-1]