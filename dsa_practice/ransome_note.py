"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    ransom_dict = {}
    magazine_dict = {}

    # parse ransomNote
    for char in ransomNote:
        ransom_dict[char] = ransom_dict.get(char, 0) + 1

    # parse magazine
    for char in magazine:
        magazine_dict[char] = magazine_dict.get(char, 0) + 1


    for char, count in ransom_dict.items(): # for each item in the dictionary
        if magazine_dict.get(char, 0) < count:
            return False # it cannot be constructed
    return True
    # return ransomNote in magazine
    
print(canConstruct('aa','aab'))