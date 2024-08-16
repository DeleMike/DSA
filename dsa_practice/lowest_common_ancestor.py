def lowestCommonAncestor(self, root, p, q):
    # we are dealing with a BST
    while root:
        if root.val < p.val and root.val < q.val:
            root = root.right # go right cos root is bigger than all values
        elif root.val > p.val and root.val > q.val:
            root = root.left # go left cos root is smaller than all values
        else:
            return root # once the condition is not satisfied then it must be the root. A root can also be a descendant.
# time complexity: O(log n)
# space complexity: O(1)

