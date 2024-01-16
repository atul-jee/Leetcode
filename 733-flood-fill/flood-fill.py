class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r=len(image)
        c=len(image[0])
        def dfs(i,j,initialColor,newColor):
            nonlocal r,c
            if i<0 or j<0 or i>=r or j>=c or image[i][j]!=initialColor:
                return
            image[i][j]=newColor
            dfs(i-1,j,initialColor,newColor)
            dfs(i+1,j,initialColor,newColor)
            dfs(i,j-1,initialColor,newColor)
            dfs(i,j+1,initialColor,newColor)
        initialColor=image[sr][sc]
        if initialColor!=color:
            dfs(sr,sc,initialColor,color)
        return image


