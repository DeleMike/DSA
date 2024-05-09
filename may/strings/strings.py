def trim_a_string(string):
    count = 0
    for str_ in string:
        if str_ != ' ' and str_ != '\t' and str_ != '\n':
            # this is how you replace a string at a position 
            # something like string[count] = 'x'
            # but we do string[:count] (count exclusive) + 'X' + string[count+1:]
            string = string[:count] + str_ + string[count+1:]
            count+=1
    string = string[:count] + '\0' + string[count+1:]
    return string  

# print(trim_a_string('Hello'))  

def reverse_string(string):
    return string[::-1]

def reverse_string_2(string):
    n = len(string)
    i, j = 0, n-1
    
    while i < j:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
        
    return "".join(string)


# print(reverse_string('abc'))
# print(reverse_string_2(list('abc')))

def left_rotate(string, d):
    d = d%len(string)
    """left rotate qwerty, d = 2
    we will have, ertyqw
    """
    
    string = string[d:] + string[:d]
    return string

def right_rotate(string, d):
    d = d%len(string)
    """right rotate qwerty, d = 2
    we will have, tyqwer
    """
    return left_rotate(string, len(string) - d)

def right_rotate_without_left_reverse(string, d):
    d = d%len(string)
    string = string[::-1] # reverse the whole string
    # reverse each section of the rotation
    # so for string qwerty, we had ytrewq
    # then we reverse (o-d exclusive) and also reversed (d-n)
    # this will give us our right rotated string
    string = string[:d][::-1] + string[d:][::-1]
    return string

# print(left_rotate('qwerty', 2))
# print(right_rotate('qwerty', 2))
# print(right_rotate_without_left_reverse('qwerty', 8)) # d should still be 2

def freq_of_character(string):
    """
    Given a string str, the task is to print the frequency of each of the characters of str in alphabetical order.
    
    Input: str = "aabccccddd"
    Output: a2b1c4d3 
    """
    char_map = {}
    ret_str = ''
    for char in list(string):
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1
    # sort the keys in lexicographically
    char_map = {k: char_map[k] for k in sorted(char_map)}
    # join the strings
    for char_, count in char_map.items():
        ret_str += f"{char_}{count}"
        
    return ret_str

# print(freq_of_character('abbc'))

def swap_characters_str(string, c, b):
    """
    Given a String S of length N, two integers B and C, the task is to traverse characters starting from the beginning,
    swapping a character with the character after C places from it, i.e. swap characters at position i and (i + C)%N.
    Repeat this process B times, advancing one position at a time. Your task is to find the final String after B swaps. 
    """
    n = len(string)
    c = c % n # to reduce number of swapping
    chars = list(string)
    for i in range(b):
        chars[i], chars[(i+c) % n] = chars[(i+c) % n], chars[i]
    return ''.join(chars)

# print(swap_characters_str('ABCDEFGH', 3, 4))

def can_make_all_same(bits_str):
    """
    Given a binary string, find if it is possible to make all its digits 
    equal (either all 0's or all 1's) by flipping exactly one bit. 
    """
    zeros = 0
    ones = 0
    
    for i in range(0, len(bits_str)):
        ch = bits_str[i]
        if ch == '0':
            zeros += 1
        else:
            ones += 1
            
    print('Zeros is now = ', zeros)
    print('Ones is now = ', ones)
        
    return (zeros == 1 or ones == 1)

print(can_make_all_same('010'))





    



