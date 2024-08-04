def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # WRONG CODE : ONLY PASSED FIRST TWO CASES
    dummy = ListNode(0)
    dummy.next = head
    curr = head
    prev = dummy

    # traverse through the linked list
    while n:
        prev = curr
        curr = curr.next
        n -= 1
    
    if curr:
        # skipping the node we wanna delete
        prev.next = curr.next
    

    # incase the node we wanna remove is just the first node, just shift the head pointer
    if curr == head:
        head = head.next
    
    
    return dummy.next if curr else curr

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # RIGHT CODE for # [1,2,3,4], n = 2, remove nth element
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # shift first pointer n times
    for _ in range(n+1):
        first = first.next
        
    # Your preference ?
    # while (n+1):
    #     first = first.next
    #     n-=1
    
    # now move the second pointer
    while first:
        first = first.next
        second = second.next
    # the second pointer should now be JUST BEFORE the node to remove
    
    # The trick overall is to maintain two pointers and update one with a delay of n steps.
    
    # skip that NODE
    second.next = second.next.next

    # dummy is a kind of placeholder, it holds ref to the head. as we adjsut the first and  second, head gets adjusted
    # so does dummy
    return dummy.next 
            
            