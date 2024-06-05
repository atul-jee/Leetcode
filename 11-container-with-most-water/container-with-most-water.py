class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        mx=float('-inf')
        while l<r:      
            mx=max(mx,(r-l)*(min(height[r],height[l])))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return mx
        