# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        if not root:
            return []
        q=[(root,1)]
        while q:
            node,level=q.pop(0)
            if node!=None:
                d[level].append(node.val)
                q.append((node.left,level+1))
                q.append((node.right,level+1))
        ans=[]
        for k in d.keys():
            if k%2:
                ans.append(d[k])
            else:
                ans.append(d[k][::-1])
        return ans
