# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self,root1,root2):
        if root1==root2==None:
            return None
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1
        temp=TreeNode(root1.val+root2.val)
        temp.left=self.merge(root1.left,root2.left)
        temp.right=self.merge(root1.right,root2.right)
        return temp
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merge(root1,root2)
        