class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        count=0
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            while q:
                x,y=q.popleft()
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
                    grid[x][y]='0'
                    q.extend([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    bfs(i,j)
        return count
        
        
        