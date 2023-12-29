
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,level,res):
        if root is None:
            return root
        if level not in res.keys():
            res[level]=[root.val]
        else:
            res[level].append(root.val)
        self.helper(root.left,level+1,res)
        self.helper(root.right,level+1,res)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return root
        res={}

        self.helper(root,1,res)
        return res.values()
        