def optimal_solution_1():
    # solving with only one array
    result = [1] * len(nums)
    
    # prefix stage
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    # postfix stage
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix *= nums[i] 

    return result 

def optimal_solution_2():
    prefixes = [1] * len(nums)
    postfixes = [1] * len(nums)
    result = [1] * len(nums)

    # fill up prefixes
    prefix = 1
    for i in range(len(nums)):
        prefixes[i] = prefix
        prefix *= nums[i]
    print(prefixes)

    # fill up postfix
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        postfixes[i] = postfix
        postfix *= nums[i]
    print(postfixes)
    
    # get the result (prefix * postfix)
    for i in range(len(prefixes)):
        result[i] = prefixes[i] * postfixes[i]

    return result