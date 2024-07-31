class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n=len(grid[0])
        m=len(grid)
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        visited=[[False]*n for _ in range(m)]
        q=[(0,0)]
        dirs=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        count=1
        grid[0][0]=1
        while q:
            for _ in range(len(q)):
                a,b=q.pop(0)
                if a==n-1 and b==n-1:
                    return count
                for u,v in dirs:
                    new_a,new_b=u+a,v+b
                    if 0<=new_a<m and 0<=new_b<n and grid[new_a][new_b]==0:
                        grid[new_a][new_b]=1
                        q.append((new_a,new_b))
            count+=1
        return -1
                

