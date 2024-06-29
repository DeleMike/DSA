"""
A linked list is a fundamental data structure in computer science.
It consists of nodes where each node contains data and a reference (link) to the next node in the sequence. 
This allows for dynamic memory allocation and efficient insertion and deletion operations compared to arrays.

A linked list is a linear data structure that consists of a series of nodes connected by pointers.
Each node contains data and a reference to the next node in the list. 
Unlike arrays, linked lists allow for efficient insertion or removal of elements from any position in the list,
as the nodes are not stored contiguously in memory.
"""

# Singly Linked-List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Doubly Linked-List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

