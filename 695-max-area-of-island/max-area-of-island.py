class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def dfs(i,j):
            nonlocal r,c
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
                return 0
            grid[i][j]=0
            area=1
            area+=dfs(i+1,j)
            area+=dfs(i-1,j)
            area+=dfs(i,j-1)
            area+=dfs(i,j+1)
            return area
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=max(ans,dfs(i,j))
        return ans

        