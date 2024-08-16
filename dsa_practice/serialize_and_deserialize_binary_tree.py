class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """ 
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        self.i = 0
        
        def dfs():
            if nodes[self.i] == "N":
                self.i+=1
                return None
            
            root = TreeNode(int(nodes[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            
            return root
        
        return dfs()
        

# time complexity: O(n)
# space complexity: O(n)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))