# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,curr):
            if not node:
                return 0
            curr+=node.val
            if node.left==node.right==None:
                if targetSum==curr:
                    return True
            return dfs(node.left,curr) or dfs(node.right,curr)
        if not root:
            return None
        return dfs(root,0)
            
        