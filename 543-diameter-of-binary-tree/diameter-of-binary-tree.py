# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        def helper(root):
            if root is None:
                return 0
            else:
                l=helper(root.left)
                r=helper(root.right)
                nonlocal d
                d=max(d,l+r)
                return 1+max(l,r)
        helper(root)
        return d
        