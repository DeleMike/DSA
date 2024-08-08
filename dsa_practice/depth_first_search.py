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
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preOrderTraversal(root)


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

inOrderTraversal(root)     


def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.data, end=' ')

print('\n')
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

postOrderTraversal(root)
 