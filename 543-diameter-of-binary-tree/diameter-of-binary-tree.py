# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        mx=0
        def helper(node):
            if node is None:
                return 0
            else:
                lh=helper(node.left)
                rh=helper(node.right)
                nonlocal mx
                mx=max(mx,lh+rh)
                return max(lh,rh)+1
        h=helper(root)
        return mx
        