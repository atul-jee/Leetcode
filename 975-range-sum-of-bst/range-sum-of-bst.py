# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        q=[root]
        s=0
        while q:
            d=q.pop(0)
            if low<=d.val<=high:
                s+=d.val
            if d.left:
                q.append(d.left)
            if d.right:
                q.append(d.right)
        return s
        