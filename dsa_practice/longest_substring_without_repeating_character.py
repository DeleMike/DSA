def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    l,r = 0,0
    runningLength = 0
    maxLength = 0
    hashSet = set()

    while r < len(s):
        if s[r] not in hashSet:
            hashSet.add(s[r])
            runningLength += 1
            maxLength = max(runningLength, maxLength)
            r+=1 # expand the window
        else:
            l += 1 # shrink the window
            r = l
            runningLength = 0
            hashSet.clear()
    return maxLength

# time complexxity = O(n): all characters might be unique
# space complexity = O(n): because of hashset




