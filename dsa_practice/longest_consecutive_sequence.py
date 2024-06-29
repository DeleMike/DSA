def longestConsecutive(self, nums: List[int]) -> int:
    """
    nums = [2,20,4,10,3,4,5]
    
    2-> 3-> 4-> 5-> x
    10-> x
    20-> x
    
    x means NULL
    2,10 and 20 have no left neighbours, hence they must be start of a sequence
    
    """
    numSet = set(nums) # remove repetition
    longest = 0
    
    for n in nums:
        # check if n is the start of a sequence
        # that is, if left neighbour does not exist, then it is the start of a sequence
        if (n-1) not in numSet:
            # if it is, check for consecutive sequence
            length = 0
            while (n + length) in numSet:
                # if right neighbour exist, keep increasing the length
                length += 1
            longest = max(longest, length)
    return longest


