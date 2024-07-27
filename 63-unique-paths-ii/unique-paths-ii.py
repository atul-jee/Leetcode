class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        if mat[0][0]==1:
            return 0
        m=len(mat)
        n=len(mat[0])
        dp=[[0]*(n) for _ in range(m)]
        dp[0][0]=1
        for i in range(1,n):
            if mat[0][i]:
                dp[0][i]=0
            else:
                dp[0][i]=dp[0][i-1]
        for i in range(1,m):
            if mat[i][0]:
                dp[i][0]=0
            else:
                dp[i][0]=dp[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j]:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        for ele in dp:
            print(ele)
        return dp[-1][-1]
        