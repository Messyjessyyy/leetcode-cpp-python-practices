class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recurse on children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
