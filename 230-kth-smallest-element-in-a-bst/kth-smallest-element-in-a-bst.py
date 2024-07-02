# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        def helper(root):
            nonlocal l
            if root:
                helper(root.left)
                l.append(root.val)
                helper(root.right)
        helper(root)
        print(l[k-1])

        return l[k-1]