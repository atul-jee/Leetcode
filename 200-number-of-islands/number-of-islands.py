class Solution:
    def helper(self,grid,i,j):
        r=len(grid)
        c=len(grid[0])
        if i>=r or j>=c or i<0 or j<0 or grid[i][j]=='0':
            return 
        grid[i][j]='0'
        self.helper(grid,i-1,j)
        self.helper(grid,i+1,j)
        self.helper(grid,i,j-1)
        self.helper(grid,i,j+1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0

        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!='0':
                    count+=1
                    self.helper(grid,i,j)
        return count

    
        
        