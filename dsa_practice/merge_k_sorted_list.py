def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists:
        return None
    
    while len(lists) > 1:
        mergedList = []
        
        #  we want perform this operation an every log k step, hence this is why step is 2
        # we might have this [[1,4,5],[1,3,4],[2,6]]
        # we want to consider [1,4,5] & [1,3,4] separately, and then [2,6] & None
        # after sorting (which is O(n)) we will have [1,1,3,4,4,5] and [2,6]
        # repeat until one element is left in the 'lists'
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None

            # sort the list
            mergedList.append(mergeDataList(l1, l2))
        lists = mergedList
    return lists[0]

def mergeDataList(l1, l2):
    """
    Here we just apply the algorithm used to sort Two Sorted LinkedList
    """
    node = dummy = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    if l1:
        node.next = l1
    else:
        node.next = l2

    return dummy.next

# time complexity: n(log k)
# space complexity: O(1)


