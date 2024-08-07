def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev # prev will be the new head, curr will point to None


