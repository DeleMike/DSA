def hasCycle(head: Optional[ListNode]) -> bool:
    hashset = set()
    curr = head
    while curr:
        if curr.val in hashset:
            return True
        hashset.add(curr.val)
        curr = curr.next
    return False

# time complexity: O(n)
# space complexity: O(n)

# ================== MININMIZE SPACE ===========================

def hasCycle(head: Optional[ListNode]) -> bool:
    # using LinkedList cycle detection algorithm with fast slow pointers
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# time complexity: O(n)
# space complexity: O(1)



