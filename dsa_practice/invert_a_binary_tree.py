def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively swap it's children if it has
        invertTree(root.left)
        invertTree(root.right)
    return root  

# time complexity: O(n), we will visit every Node
# space complexity: O(log n)[best case; balanced tree] or O(n)[worst case; inbalanced tree] 

