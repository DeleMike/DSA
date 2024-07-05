def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    
    for i, v in enumerate(nums):
        diff = target - v
        if diff in hashmap.keys():
            return [hashmap[diff], i]
        hashmap[v] = index
    return [-1,-1]