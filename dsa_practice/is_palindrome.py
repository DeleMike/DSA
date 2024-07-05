def isPalindromeV1(self, s: str) -> bool:
    # we achieve time complexity to be O(n) and space complexity to be O(n)
    modified_str = ''.join([char.lower() for char in s if char.isalnum()])
    return modified_str == modified_str[::-1]

def isPalindromeV2(self, s: str) -> bool:
    """Using Two Pointer Approach to save memory"""
    # we achieve time complexity to be O(n) and space complexity to be O(1)
    l,r = 0,len(s)-1
    while l < r:
        # check if
        while l < r and not isAlphaNumeric(s[l]):
            l += 1
        while r > l and not isAlphaNumeric(s[r]):
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    return True
   
def isAlphaNumeric(char):
    """Check if char is an alphanumeric character
    """
    return (
        ord('A') <= ord(char) <= ord('Z') or
        ord('a') <= ord(char) <= ord('z') or
        ord('0') <= ord(char) <= ord('9')
    )
    
