import time


def check_time():
    # Record the start time
    start_time = time.time()

    # A linear operation on 100,000,000 records
    for i in range(100000000):
        j = i*i

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Time taken: {elapsed_time} seconds")
     
# check_time()

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
        return f'Node is {self.key} and its left is {self.left} and its right is {self.right}'
        

# must have 3 elements in left
# every subtree must have 3 elements else it is not a tree
# if it does not have 3 elements, then it must have 1 element
# tree_tuple = ((1,3, None), 2, ((None,3,4),5,(6,7,8)))
# print(tree_tuple)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print

def tree_to_tuple(node):
    if node is None:
        return None
    else:
        return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

print(tree_to_tuple(root))



def parse_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tree(data[0]) # recursive step
        node.right = parse_tree(data[2]) 
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

# tree2 = parse_tree(tree_tuple)        
# print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)