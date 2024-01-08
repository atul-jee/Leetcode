# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min1=root.val
        min2=float('inf')
        def helper(root):
            nonlocal min1,min2
            if not root:
                return

            if root.val<min1:
                min2=min1
                min1=root.val
            elif root.val!=min1 and root.val<min2:
                min2=root.val
            helper(root.left)
            helper(root.right)
        helper(root)
        if min2==float('inf'):
            return -1
        return min2
            