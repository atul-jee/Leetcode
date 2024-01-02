# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l=0
        r=0
        if root.left:
            l=self.minDepth(root.left)
        if root.right:
            r=self.minDepth(root.right)
        if not root.left or not root.right:
            return l+r+1
        return min(l,r)+1
        