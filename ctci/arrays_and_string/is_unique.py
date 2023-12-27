"""Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
cannot use additional data structures? 
Hints: #44, #117, #132 
"""

# on first thought, on every number we process, we need a looked set. 
# this set will be used to store only unique numbers so we don't visit a number more than once

def initial_soln(number_str) -> str :
    looked = set()
    for digit in number_str:
        if digit in looked: # check if the currently processed digit already exist, return False
            return False
        looked.add(digit)
                
    return is_unique


print(initial_soln('132444'))
print(initial_soln('132'))
print(initial_soln('3173'))
print(initial_soln('989'))
print(initial_soln('123456789'))

    