def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = [] # storing each level of the BFS
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        result.append(level)
    return result

# basically using the BFS algorithm. easy if you know BFS.
# time complexity: O(n)
# space complexity ~= O(n)
        