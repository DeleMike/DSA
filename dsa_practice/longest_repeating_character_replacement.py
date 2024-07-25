def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    lengthOfSubString = 0
    l = 0
    count = {}

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        if (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        lengthOfSubString = max(lengthOfSubString, (r-l+1))
    return lengthOfSubString

# time complexity: O(n)
# space complexity: O(1)