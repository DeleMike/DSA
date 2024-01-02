# EASY
# Given a list [4,2,2] 
# where list[0] = root and list[1] = left child and list[2] = right
# we can say left + right = True because they are the same. This is an easy problem

def checkSum(nums):
    return nums[0] == nums[1] + nums[2]

print('Value for [4,2,2]', checkSum([4,2,2]))

# build multiple test cases