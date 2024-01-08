# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,res,level,x,y,parent):
        if not root:
            return 
        if root.val==x or root.val==y:
            res[root.val]=(level,parent)
        self.helper(root.left,res,level+1,x,y,root)
        self.helper(root.right,res,level+1,x,y,root)
    

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res={}
        self.helper(root,res,1,x,y,None)
        return res[x][0]==res[y][0] and res[x][1]!=res[y][1]
        