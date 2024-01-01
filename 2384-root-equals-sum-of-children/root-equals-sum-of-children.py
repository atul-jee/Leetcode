# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Sum(self,root):
            if not root:
                return 0
            return root.val+self.Sum(root.left)+self.Sum(root.right)
        
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root or not root.left or not root.right:
            return False
        left_sum=self.Sum(root.left)
        right_sum=self.Sum(root.right)
        #print(root.val,left_sum,right_sum)
        return root.val==left_sum+right_sum
        