# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def check(root1,root2):
            if root1==root2==None:
                return True
            if not root1 or not root2:return False
             
            return root1.val==root2.val and check(root1.left,root2.right) and check(root1.right,root2.left )
        return check(root.left,root.right)
            
        
        