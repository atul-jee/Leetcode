# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if (not root and targetSum>0) or not root:
            return False
        if not root and targetSum==0:
            return False
        q=deque()
        s=[root]
        _sum=[root.val]
        while s:
            t=s.pop()
            cur_sum=_sum.pop()
            if not t.left and not t.right:
                if targetSum==cur_sum:
                    return True
            if t.left:
                s.append(t.left)
                _sum.append(cur_sum+t.left.val)
            if t.right:
                s.append(t.right)
                _sum.append(cur_sum+t.right.val)
            
            
        return False
