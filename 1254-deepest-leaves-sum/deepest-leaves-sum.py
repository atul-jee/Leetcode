# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d=defaultdict(list)
        q=[(root,0)]
        while q:
            node,level=q.pop(0)
            if node!=None:
                d[level].append(node.val)
                q.append((node.left,level+1))
                q.append((node.right,level+1))
        s=0
        for ele in d.keys():
            s=max(s,ele)
        return sum(d[s])
