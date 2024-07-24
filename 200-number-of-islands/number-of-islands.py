class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,m,n,grid):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!="1":
                return
            grid[i][j]="0"
            dfs(i-1,j,m,n,grid)
            dfs(i+1,j,m,n,grid)
            dfs(i,j-1,m,n,grid)
            dfs(i,j+1,m,n,grid)
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    
                    dfs(i,j,m,n,grid)
                    count+=1
                    
        return count

        