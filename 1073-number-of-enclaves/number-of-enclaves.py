class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
                return 
            grid[i][j]=2
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
        for i in range(m):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][n-1]==1:
                dfs(i,n-1)
        for i in range(n):
            if grid[0][i]==1:
                dfs(0,i)
            if grid[m-1][i]==1:
                dfs(m-1,i)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
            
        return count

        