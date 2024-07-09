# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx=[float('-inf')]
        def helper(node,mx):
            #nonlocal mx
            if node==None:
                return 0
            left=max(0,helper(node.left,mx))
            right=max(0,helper(node.right,mx))
            mx[0]=max(mx[0],left+right+node.val)
        
            return max(left,right)+node.val
        helper(root,mx)
        return mx[0]
        