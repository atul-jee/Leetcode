from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        row, col = len(image), len(image[0])
        initialColor = image[sr][sc]
        q = [(sr, sc)]
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        while q:
            u, v = q.pop(0)
            image[u][v]=color
            for i, j in dirs:
                di, dj = u + i, v + j
                if 0 <= di < row and 0 <= dj < col and image[di][dj] == initialColor:
                    image[di][dj] = color
                    q.append((di, dj))
        
        return image
