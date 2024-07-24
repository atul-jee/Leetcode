class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
                return 
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count+=1
                    #dfs(i,j)
        return count