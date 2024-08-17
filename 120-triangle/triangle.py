class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        
        for i in range(1,len(tri)):
            for j in range(len(tri[i])):
                if j==0:
                    tri[i][j]+=tri[i-1][j]
                elif j==len(tri[i])-1:
                    tri[i][j]+=tri[i-1][j-1]
                else:
                    tri[i][j]+=min(tri[i-1][j],tri[i-1][j-1])
        return min(tri[-1])
                    
        