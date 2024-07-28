def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    hashmap = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    stack = [''] * len(s)
    top = -1

    for c in s:
        if c in hashmap.values():
            # just push
            top += 1
            stack[top] = c
        elif c in hashmap.keys():
            popped_value = stack[top]
            
            if popped_value != hashmap[c]: # we don't have matching brackets
                return False

            # just pop
            stack[top] = ''
            top -= 1
    return top == -1

# time complexity: O(n) because we go through the whole string
# space complexity: O(n), usage of a stack data structure, which might be as long as the input string

