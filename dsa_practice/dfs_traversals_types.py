"""We are gonna implement depth first search with three algorithms 
pre-order(Root-L-R), in-order(L-Root-R) and post-order(L-R-Root)
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if root:
        print(root.data, end = ' ')
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def iterPreOrderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    
    while stack:
        curr = stack.pop()
        print(curr.data, end=' ')
        
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preOrderTraversal(root)
print('\n')
iterPreOrderTraversal(root)
            


def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.data, end=' ')
        inOrderTraversal(root.right)

print('\n')
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# inOrderTraversal(root)   
def iterativeInoderDFS(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()    
        print(curr.data, end=' ')
        curr = curr.right
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
iterativeInoderDFS(root)


def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.data, end=' ')

def iterPostOrderTraversal(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        print(curr.data, end=' ')
        curr = curr.left
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('\n')
postOrderTraversal(root)
print('\n')
iterPostOrderTraversal(root)
 