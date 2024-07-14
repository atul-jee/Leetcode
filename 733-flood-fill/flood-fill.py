class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initialColor=image[sr][sc]
        def dfs(i,j,row,col,initialColor):
            nonlocal color
            if i<0 or i>=row or j<0 or j>=col or initialColor!=image[i][j]:
                return
            image[i][j]=color
            dfs(i+1,j,row,col,initialColor)
            dfs(i-1,j,row,col,initialColor)
            dfs(i,j+1,row,col,initialColor)
            dfs(i,j-1,row,col,initialColor)
        if image[sr][sc]!=color:
            dfs(sr,sc,len(image),len(image[0]),initialColor)
        return image

        