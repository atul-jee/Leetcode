class Solution:
    def helper(self,grid,i,j):
        r=len(grid)
        c=len(grid[0])
        if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
            return 0
        grid[i][j]=0
        area=1
        area+=self.helper(grid,i-1,j)
        area+=self.helper(grid,i+1,j)
        area+=self.helper(grid,i,j+1)
        area+=self.helper(grid,i,j-1)
        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    a=self.helper(grid,i,j)
                    ans=max(ans,a)
        return ans

        