from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return f'{self.val}'
        # return f'TreeNode(val: {self.val}, left:{self.left}, right:{self.right})'
    
def bfs_levels(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    print('Result = ', result)
    

def bfs(root):
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_iterative(root):
    if not root:
        return None
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
            

def dfs_recursive(root):
    if not root:
        return None
    
    print(root.val, end=' ')
    dfs_recursive(root.left)
    dfs_recursive(root.right)
    
# Create a sample tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("BFS Traversal:")
bfs(root)  # Output: 1 2 3 4 5

print('\nLEVELS BFS TRAVERSAL:')
bfs_levels(root)

print("\nDFS Iterative Traversal:")
dfs_iterative(root)  # Output: 1 2 4 5 3

print("\nDFS Recursive Traversal:")
dfs_recursive(root)  # Output: 1 2 4 5 3
    
