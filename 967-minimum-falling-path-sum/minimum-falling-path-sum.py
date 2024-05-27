class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        for i in range(1,n):
            for j in range(m):
                left=mat[i-1][j-1] if j>0 else float('inf')
                top=mat[i-1][j]
                right=mat[i-1][j+1] if j+1<m else float('inf')
                mat[i][j]+=min(top,left,right)
        return min(mat[-1])
        