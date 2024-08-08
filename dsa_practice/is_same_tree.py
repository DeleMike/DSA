def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        
        
        
        # my intuition is to perform a pre-order(root-L-R) traversal through the root
        # and then compare the results of both traversals
#         order_p = []
#         order_q = []
#         self.preOrderTraversal(p, order_p)
#         self.preOrderTraversal(q, order_q)

#         return order_p == order_q

# def preOrderTraversal(self, root, dataList):
#     if root:
#         dataList.append(root.val)
#         self.preOrderTraversal(root.left, dataList)
#         self.preOrderTraversal(root.right, dataList)
#     else:
#         dataList.append(None) 

#     return dataList
    
    


        