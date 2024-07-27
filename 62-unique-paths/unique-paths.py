class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n) for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for i in range(n):
            dp[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                if i==j:
                    dp[i][j]=2*(max(dp[i-1][j],dp[i][j-1]))
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # for ele in dp:
        #     print(ele)
        return dp[-1][-1]

        