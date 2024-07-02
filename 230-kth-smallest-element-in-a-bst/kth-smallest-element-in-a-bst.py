# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=0
        def helper(root):
            nonlocal ans,k
            if root and k:
                if k:
                    helper(root.left)
                    if k>0:
                        k-=1
                        if k==0:
                            ans=root.val
                            return 
                    helper(root.right)
        helper(root)
        return ans