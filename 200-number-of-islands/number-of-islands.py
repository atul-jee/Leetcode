class Solution:
    def dfs(self,grid,i,j,r,c):
        if i<0 or j<0 or i>=r or j>=c or grid[i][j]!='1':
            return 
        grid[i][j]='*'
        self.dfs(grid,i-1,j,r,c)
        self.dfs(grid,i,j+1,r,c)
        self.dfs(grid,i+1,j,r,c)
        self.dfs(grid,i,j-1,r,c)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j,r,c)
                    count+=1
        return count
        