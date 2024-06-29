# we have say [1,1,4,5,5,5]
hashmap = {}
for num in nums:
    hashmap[num] = hashmap.get(num, 0) + 1
# we should have {1:2, 4:1, 5:3}

# initialise bucket list
# [[], [], [], ... ,[]]
# we wanna make the bucket as long as the items in the nums
bucket_list = [[] for idx in range(len(nums)+1)]

# fill in the bucket list
# for example, when value is 2, 
# we go to bucket list position 2 to add the key(main integer)
for key, value in hashmap.items():
    bucket_list[value].append(key)
# so we can have, for this example, [[],[4],[1],[5],[],[],[]] after it's run

# now we determine the top k element in list
# we traverse from end to start
top_ks = []
for i in range(len(bucket_list)-1,0,-1):
    for bucket in bucket_list[i]:
        top_ks.append(bucket)
        # check if length of top_ks is now up to k
        if len(top_ks) == k:
            return top_ks