"""EASY
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return ' -> '.join(result)

def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    values = []

    # set the current head
    current = head

    # we check if the current head is not null, we get its value
    while current != None:
        values.append(current)
        current = current.next
    
    # get the mid value
    middle_node_value = values[len(values) // 2]
    return middle_node_value

    # Time complexity: O(n)
    # space complexity: O(1)

def betterMiddleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    middle = head
    end = head
    
    # we use two pointers
    # Still O(n)
    # space complexity is O(1)
    while (end!=None and end.next != None):
        middle = middle.next
        end = end.next.next
    
    return middle

    # Time complexity: O(n)
    # space complexity: O(1)
    


linked_list = ListNode(val=1, next=ListNode(val=2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
print(linked_list)
print(betterMiddleNode(linked_list))