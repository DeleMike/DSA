def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    n = 0
    stack = []
    curr = root

    while stack or curr:
        n+=1
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        if n == k:
            return curr.val
        curr = curr.right
    

# time complexity: O(height of tree) = O(n) or O(log n)
# space complexity: O(n)
